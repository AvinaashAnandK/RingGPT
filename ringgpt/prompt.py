class Prompt:
    def __init__(self, instruction, output_format, example=None):
        if not instruction:
            raise ValueError("Instruction is a mandatory parameter.")
        if example:
            if not isinstance(example, list) or not all(isinstance(e, dict) and 'Input' in e and 'Output' in e for e in example):
                raise ValueError("""Examples is not in expected format. Please pass examples in the format 
                [{"Input":"Sample corpus 1", "Output":"Expected output 1 in the specified format"},
                {"Input":"Sample corpus 2", "Output":"Expected output 2 in the specified format"}]""")
        if not output_format:
            raise ValueError("Output format is a mandatory parameter.")
        
        self.instruction = instruction
        self.output_format = output_format
        self.example = example
