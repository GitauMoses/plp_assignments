def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price based on the discount applied
if discount_percentage >= 20:
    print("The final price after the discount is:", final_price)
else:
    print("No discount was applied. The original price is:", original_price)