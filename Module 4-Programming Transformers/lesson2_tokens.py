# Lesson 2: Tokenization
# Neural networks cannot read text; they only understand numbers. 
#Tokenization is the process of chopping text into pieces (tokens) and mapping them to unique ID numbers.

from transformers import AutoTokenizer

# Load a pre-trained tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

text = "AI programming is fascinating!"

# Convert text to tokens and IDs
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print(f"Original Text: {text}")
print(f"Tokens: {tokens}")
print(f"Token IDs: {token_ids}")

# The model needs 'tensors', which the tokenizer can create automatically:
encoded_input = tokenizer(text, return_tensors="pt") # "pt" stands for PyTorch
print(f"\nReady for PyTorch:\n{encoded_input}")