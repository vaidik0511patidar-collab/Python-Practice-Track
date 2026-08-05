number = int(input())
sum_of_digits = 0

# Extract and add each digit using a while loop
while number > 0:
    last_digit = number % 10
    number //= 10
    sum_of_digits += last_digit

# Display the sum of digits
print(f"Sum of digits: {sum_of_digits}")