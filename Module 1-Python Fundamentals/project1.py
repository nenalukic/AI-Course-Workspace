reviews = [
    {"user": "Alice", "score": 5, "text": "Loved it!"},
    {"user": "Bob", "score": 2, "text": "Broke after a week."},
    {"user": "Charlie", "score": 4, "text": "Pretty good."},
    {"user": "Diana", "score": 1, "text": "Terrible customer service."},
    {"user": "Evan", "score": 5, "text": "Perfect."}
]

# 1. Create a variable to hold the total score
total_score = 0

# 2. Create an empty list to hold negative reviews
negative_reviews = []

# 3. Loop through the reviews list
for review in reviews:
    # Add the current review's score to the total
    total_score += review["score"]
    
    # Check if the score is less than 3
    if review["score"] < 3:
        # Append the user's name to the negative_reviews list
        negative_reviews.append(review["user"])

# 4. Calculate the average
average_score = total_score / len(reviews)

# 5. Print the results
print(f"Average Review Score: {average_score}")
print(f"Users who left negative reviews: {negative_reviews}")