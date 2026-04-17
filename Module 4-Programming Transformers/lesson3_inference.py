# Lesson 3: Using Pre-Trained Models
# Training a Transformer from scratch requires millions of dollars in server costs. 
# The modern workflow involves downloading a "pre-trained" model that already understands language, and using it for your specific task.

from transformers import pipeline

# The pipeline function is a high-level wrapper that handles tokenization and the model automatically
generator = pipeline("text-generation", model="gpt2")

prompt = "In the future, artificial intelligence will"

# Generate text
output = generator(prompt, max_length=30, num_return_sequences=1)

print("Generated Text:")
print(output[0]['generated_text'])