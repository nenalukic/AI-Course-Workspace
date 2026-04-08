# Lesson 4: Functions and Exceptions
def calculate_discount(price, discount_percent):
    """Calculates the final price after a discount."""
    try:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    except TypeError:
        return "Error: Please provide numbers, not text."

# Using the function
print(calculate_discount(100, 20))  # Output: 80.0
print(calculate_discount("One Hundred", 20)) # Output: Error message