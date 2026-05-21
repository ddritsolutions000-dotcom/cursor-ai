# AI Code Generator
# Using HuggingFace Transformers and StarCoder

from transformers import AutoModelForCausalLM, AutoTokenizer

class AICodeGenerator:
    def __init__(self, model_name="bigcode/starcoder-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_code(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    ai_generator = AICodeGenerator()
    prompt = "Write a Python function to calculate factorial"
    code = ai_generator.generate_code(prompt)
    print(code)