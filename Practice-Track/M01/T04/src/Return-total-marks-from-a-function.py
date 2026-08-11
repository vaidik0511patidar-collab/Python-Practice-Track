def calculate_total(first_mark, second_mark):
    # Calculate and return the total marks
    total_marks = first_mark + second_mark

    return total_marks

mark1 = int(input())
mark2 = int(input())

# Call the function and store the returned value
total = calculate_total(mark1, mark2)

# Print the returned value
print(total)