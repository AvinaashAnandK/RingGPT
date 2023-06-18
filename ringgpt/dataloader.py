import pandas as pd
import os

class DataLoader:
    def __init__(self, file, chunking_type='chunk', data_column_name=None):
        self.file = file
        self.chunking_type = chunking_type
        self.data_column_name = data_column_name
        self.dataframe = None

        self.load_data()

    def load_data(self):
        # Validate chunking_type
        valid_chunking_types = ['truncate', 'chunk']
        if self.chunking_type not in valid_chunking_types:
            raise ValueError("Invalid chunking_type. Supported values are 'truncate' and 'chunk'.")

        # Load data from the file or Python list
        if isinstance(self.file, list):
            self.dataframe = pd.DataFrame(self.file)
        elif isinstance(self.file, str):
            _, file_extension = os.path.splitext(self.file)
            if file_extension not in ['.csv', '.txt']:
                raise ValueError("Unsupported raw data format. Supported formats are .csv, .txt files, and Python lists.")

            if file_extension == '.csv':
                # Read data from a CSV file
                if self.data_column_name is None:
                    raise ValueError("Data column name is required for .csv files.")
                self.dataframe = pd.read_csv(self.file)
                if self.data_column_name is not None and self.dataframe.dtypes[self.data_column_name] != 'object':
                    raise ValueError("Only strings are supported in the data column.")
            elif file_extension == '.txt':
                # Read data from a text file
                with open(self.file, 'r') as f:
                    content = f.read()
                self.dataframe = pd.DataFrame([content], columns=[self.data_column_name])

        else:
            raise ValueError("File argument should either be a file path or a Python list.")
        
    def get_data(self):
        return self.dataframe
        
    def get_data_column_name(self):
        return self.data_column_name
