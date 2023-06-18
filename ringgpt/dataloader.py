import pandas as pd
import os

class DataLoader:
    def __init__(self, file, chunking_type, data_column_name=None):
        self.file = file
        self.chunking_type = chunking_type
        self.data_column_name = data_column_name
        self.dataframe = None

        self.load_data()

    def load_data(self):
        # If the data is a Python list
        if isinstance(self.file, list):
            self.dataframe = pd.DataFrame(self.file)
        # If the data is a file path
        elif isinstance(self.file, str):
            # Check the file extension
            _, file_extension = os.path.splitext(self.file)
            if file_extension not in ['.csv', '.txt']:
                raise ValueError("Unsupported raw data format. Supported formats are .csv, .txt files, and Python lists.")

            # Load the appropriate file type
            if file_extension == '.csv':
                if self.data_column_name is None:
                    raise ValueError("Data column name is required for .csv files.")
                self.dataframe = pd.read_csv(self.file, usecols=[self.data_column_name])
            elif file_extension == '.txt':
                self.dataframe = pd.read_csv(self.file, sep='\n', header=None)

            # Check the type of the data in the data column
            if self.data_column_name is not None and self.dataframe.dtypes[self.data_column_name] != 'object':
                raise ValueError("Only strings are supported in the data column.")
        else:
            raise ValueError("File argument should either be a file path or a Python list.")
