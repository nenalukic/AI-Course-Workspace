# The Task:
# This is your final portfolio project. You will build an AI script that acts as an automated review moderator. 
# It will take a list of movie reviews, tokenize them manually, 
# pass them through a PyTorch-based Transformer model specifically fine-tuned for sentiment analysis, 
# and output whether each review is POSITIVE or NEGATIVE, along with the AI's confidence score.

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

print("Loading pre-trained Transformer model...")
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the PyTorch Model (Safetensors disabled for macOS stability)
model = AutoModelForSequenceClassification.from_pretrained(model_name, use_safetensors=False)

# A mock dataset of movie reviews
movie_reviews = [
    "This movie was an absolute masterpiece! The acting was phenomenal.",
    "Terrible plot, awful acting. A complete waste of my time and money.",
    "It was okay. The special effects were good, but the story was a bit boring.",
    "I would highly recommend this film to anyone who loves sci-fi!"
]

print("\n--- Starting Sentiment Analysis ---\n")

# Process each review
for review in movie_reviews:
    # 1. Tokenize the text and convert to PyTorch tensors
    inputs = tokenizer(review, return_tensors="pt", truncation=True, padding=True)
    
    # 2. Pass the inputs through the Transformer model
    with torch.no_grad(): 
        outputs = model(**inputs)
    
    # 3. Get the raw output scores (logits)
    logits = outputs.logits
    
    # 4. Convert logits to probabilities using Softmax
    probabilities = F.softmax(logits, dim=1)
    
    # 5. Get the highest probability class
    predicted_class_id = torch.argmax(probabilities).item()
    confidence_score = probabilities[0][predicted_class_id].item() * 100
    
    # 6. Map the ID to the actual label
    labels = ["NEGATIVE", "POSITIVE"]
    sentiment = labels[predicted_class_id]
    
    # Print the results
    print(f"Review: '{review}'")
    print(f"AI Sentiment: {sentiment} (Confidence: {confidence_score:.2f}%)\n")

print("Pipeline Complete. Ready for production deployment!")