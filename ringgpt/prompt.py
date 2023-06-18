from enum import Enum

class Instruction(Enum):
    UNSTRUCTURED_TO_STRUCTURED = "Unstructured to structured"
    SUMMARISE = "Summarise"
    CLASSIFICATION = "Classification"
    NAMED_ENTITY_RECOGNITION = "Named Entity Recognition"

class Prompt:
    entity = {
        "Person": "Names of people",
        "PersonType": "Job types or roles held by a person",
        "Location": "Natural and human-made landmarks, structures, geographical features, and geopolitical entities",
        "Organization": "Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type",
        "Event": "Historical, social, and naturally occurring events",
        "Product": "Physical objects of various categories",
        "Address": "Full mailing address",
        "PhoneNumber": "Phone numbers",
        "Email": "Email addresses",
        "URL": "URLs to websites",
        "DateTime": "Dates and times of day in the format dd/mm/yyyy hh:mm:ss",
        "Quantity": "Numbers and numeric quantities"
    }

    instructions = {
        Instruction.UNSTRUCTURED_TO_STRUCTURED: {
            'prompt': '### INSTRUCTION ### Extract the below attributes based on the text in context below. Follow additional instructions when available for an attribute, mentioned after the colon. Use only "N/A" wherever the value for an attribute is unavailable in the context below.',
            'expected_output': '### DESIRED FORMAT OF OUTPUT ### \n<attribute_name>: <extracted_value>'
        },
        Instruction.SUMMARISE: {
            'prompt': '### INSTRUCTION ### I want you to act as an AI summariser. I will give you context, and you will provide a summary of that context. Your summary should be informative and factual, covering the most important aspects of the context.',
            'expected_output': '### DESIRED FORMAT OF OUTPUT ### \n<summary_text>'
        },
        Instruction.CLASSIFICATION: {
            'prompt': '### INSTRUCTION ### Classify the text in context below into one of the following categories. The output should be all applicable categories from the list below.',
            'expected_output': '### DESIRED FORMAT OF OUTPUT ### \n<comma_separated_list_of_category_names>'
        },
        Instruction.NAMED_ENTITY_RECOGNITION: {
            'prompt': '### INSTRUCTION ### Classify the text in context below into one of the following categories. A substring of the input context can only belong to one of the categories from the list below.',
            'expected_output': '### DESIRED FORMAT OF OUTPUT ### \n<category_name>: <comma_separated_list_of_substrings_from_text>'
        }
    }

    def __init__(self, instruction, instruction_categories=None, example=None):
        if instruction not in Instruction.__members__:
            raise ValueError("""Instruction not recognised. Ring can only take the following instructions:
            1. Unstructured to structured
            2. Summarise
            3. Classification
            4. Named Entity Recognition""")

        if instruction_categories:
            if not isinstance(instruction_categories, list) or not all(isinstance(cat, str) for cat in instruction_categories):
                raise ValueError("Instruction categories must be a list of strings.")

        if instruction in [Instruction.UNSTRUCTURED_TO_STRUCTURED, Instruction.CLASSIFICATION, Instruction.NAMED_ENTITY_RECOGNITION] and not instruction_categories:
            raise ValueError(f"Instruction categories is mandatory for '{instruction.value}' instruction.")

        if instruction == Instruction.NAMED_ENTITY_RECOGNITION and instruction_categories:
            unique_entity_names = set(self.entity.keys())
            if not set(instruction_categories).issubset(unique_entity_names):
                raise ValueError(f"Instruction categories can only have values from the list of unique entity names for '{instruction.value}' task.")

        if example:
            if not isinstance(example, list) or not all(isinstance(e, dict) and 'input' in e and 'output' in e for e in example):
                raise ValueError("""Examples is not in the expected format. Please pass examples in the format:
                [{"input": "Sample corpus 1", "output": "Expected output 1 in the specified format"},
                 {"input": "Sample corpus 2", "output": "Expected output 2 in the specified format"}]""")

        self.instruction = instruction
        self.instruction_categories = instruction_categories
        self.example = example
        self.instruction_categories = [e.value for e in Instruction]
        
        if example:
            self.instruction_prompt = self.instructions[instruction]['prompt'] + " Refer to the examples which define expected outputs for given contexts.\n"
        else:
            self.instruction_prompt = self.instructions[instruction]['prompt']
        
        if instruction in [Instruction.UNSTRUCTURED_TO_STRUCTURED, Instruction.CLASSIFICATION, Instruction.NAMED_ENTITY_RECOGNITION]:
            self.instruction_prompt += "\n### CATEGORIES ###\n"
            if instruction == Instruction.NAMED_ENTITY_RECOGNITION:
                for category in instruction_categories:
                    self.instruction_prompt += f"{category}: {self.entity.get(category, 'N/A')}\n"
            else:
                self.instruction_prompt += "\n".join(instruction_categories) + "\n"

    def get_instruction_prompt(self):
        return self.instruction_prompt
    
    def get_example(self):
        return self.example
    
    def get_instruction_categories(self):
        return self.instruction_categories
