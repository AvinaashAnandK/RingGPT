class Prompt:
    def __init__(self, instruction, output_format, example=None):
        self.instruction = instruction
        self.output_format = output_format
        self.example = example

    # Add your methods here