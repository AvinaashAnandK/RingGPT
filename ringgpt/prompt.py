from enum import Enum

class Instruction(Enum):
    UNSTRUCTURED_TO_STRUCTURED = "Unstructured to structured"
    SUMMARISE = "Summarise"
    TRANSLATE = "Translate"
    QA = "QA"
    SENTIMENT_ANALYSIS = "Sentiment Analysis"
    SPEECH_RECOGNITION = "Speech Recognition"


class Prompt:
    def __init__(self, instruction, output_format, example=None, output_check=None):
        if not Instruction[instruction]:
            raise ValueError("""Instruction not recognised. Ring can only take the following instructions:
            1. Unstructured to structured
            2. Summarise
            3. Translate
            4. QA
            5. Sentiment Analysis
            6. Speech Recognition""")
        if example:
            if not isinstance(example, list) or not all(isinstance(e, dict) and 'Input' in e and 'Output' in e for e in example):
                raise ValueError("""Examples is not in expected format. Please pass examples in the format 
                [{"Input":"Sample corpus 1", "Output":"Expected output 1 in the specified format"},
                {"Input":"Sample corpus 2", "Output":"Expected output 2 in the specified format"}]""")
        if not output_format:
            raise ValueError("Output format is a mandatory parameter.")
        if output_check and not isinstance(output_check, list):
            raise ValueError("Output check must be a list of strings.")
        
        self.instruction = Instruction[instruction]
        self.output_format = output_format
        self.example = example
        self.output_check = output_check

    # Add your methods here
