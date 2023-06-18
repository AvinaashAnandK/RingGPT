import logging
import os
import random
import pandas as pd
from itertools import cycle
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken

class Ring:
    def __init__(self, llm_list, max_attempts=5, retry_delay=5, throttle_delay=5, log_enabled=True, wip_save=True):
        # Validate the llm_list
        if not llm_list:
            raise ValueError("Failed initializing Ring, llm_list is not declared by the user")
        if not isinstance(llm_list, list) or not all(isinstance(llm, dict) for llm in llm_list):
            raise ValueError("""Failed initializing Ring, llm_list does not align with the expected format. Please pass llm_list in the format:
                [{"service": "OpenAIChat", 
                  "access_token": "enter-your-token-here",
                  "identifier": "identifier-for-the-account-used-for-the-token"},
                 {"service": "BardChat", 
                  "access_token": "enter-your-token-here",
                  "identifier": "identifier-for-the-account-used-for-the-token"},
                 {"service": "EdgeChat"}]""")
        for llm in llm_list:
            if 'service' not in llm:
                raise ValueError("Failed initializing Ring, service attribute is not declared by the user in the dictionaries passed in llm_list")
            if llm['service'] in ["OpenAIChat", "BardChat"] and (not llm.get('access_token')):
                raise ValueError("Failed initializing Ring, access_token attribute is not declared by the user in the dictionaries passed in llm_list for OpenAIChat or BardChat")
        
        self.llm_list = llm_list
        self.max_attempts = max_attempts
        self.retry_delay = retry_delay
        self.throttle_delay = throttle_delay
        self.log_enabled = log_enabled
        self.wip_save = wip_save
        self.output_dataframe = None

        # Set up logging
        if self.log_enabled:
            logging.basicConfig(filename='ring_log.log', filemode='a', level=logging.INFO, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
            logging.info("Ring initialized")

        self.llm_iterator = cycle(llm_list)
        self.text_chunker = RecursiveCharacterTextSplitter(
            chunk_size=350,
            chunk_overlap=20,
            length_function=self.tokenizer_len,
            separators=['\n\n', '\n', ' ', '']
        )
        self.tokenizer = tiktoken.get_encoding('cl100k_base')

    def example_picker(self, example):
        if not example:
            return ""

        if len(example) == 1:
            return f"### EXAMPLE ###\nContext: {example[0]['input']}\nOutput: {example[0]['output']}"

        selected_example = example[0]
        unselected_examples = example[1:]
        if len(unselected_examples) > 0:
            selected_example_index = random.randint(0, len(unselected_examples) - 1)
            selected_example = unselected_examples.pop(selected_example_index)

        output = f"### EXAMPLES ###\n\nExample 1\nContext: {selected_example['input']}\nOutput: {selected_example['output']}\n\n"

        if unselected_examples:
            output += "Example 2\n"
            second_example = random.choice(unselected_examples)
            output += f"Context: {second_example['input']}\nOutput: {second_example['output']}"

        return output

    def tokenizer_len(self, text):
        tokens = self.tokenizer.encode(
            text,
            disallowed_special=()
        )
        return len(tokens)

    def process_data(self, file, chunking_type, data_column_name=None):
        import pandas as pd
        import os

        if isinstance(file, list):
            self.dataframe = pd.DataFrame(file)
        elif isinstance(file, str):
            _, file_extension = os.path.splitext(file)
            if file_extension not in ['.csv', '.txt']:
                raise ValueError("Unsupported raw data format. Supported formats are .csv, .txt files, and Python lists.")
            if file_extension == '.csv':
                if data_column_name is None:
                    data_column_name = 0
                self.dataframe = pd.read_csv(file, usecols=[data_column_name])
            elif file_extension == '.txt':
                self.dataframe = pd.read_csv(file, sep='\n', header=None)
        else:
            raise ValueError("File argument should either be a file path or a Python list.")

        prompt_length = self.tokenizer_len(self.instruction_prompt)
        chunk_size = 2000 - prompt_length
        self.dataframe['chunk'] = self.dataframe[data_column_name].apply(lambda x: self.text_chunker.split_text(x, chunk_size, 20))
        self.dataframe = self.dataframe.explode('chunk')
        self.dataframe.reset_index(drop=True, inplace=True)

        # Repeat other columns for each row
        self.dataframe = self.dataframe.reindex(self.dataframe.index.repeat(len(self.dataframe.columns) - 1)).reset_index(drop=True)
        self.dataframe[data_column_name] = self.dataframe['chunk']
        self.dataframe.drop(columns=['chunk'], inplace=True)
