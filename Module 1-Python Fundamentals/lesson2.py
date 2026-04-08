# Lesson 2: Control Flow and Loops
customer_rating = 4.5

# Decision making
if customer_rating >= 4.5:
    print("Excellent review! Show prominently.")
elif customer_rating >= 3.0:
    print("Average review.")
else:
    print("Poor review. Flag for customer support.")

# Repetition
print("Applying discount to next 3 items:")
for i in range(1, 4):
    print(f"Item {i} processed.")