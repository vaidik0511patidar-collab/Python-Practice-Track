value_count = int(input())
original_list = []

# Read and store all values using append()
for i in range(value_count):
    original_list.append(int(input()))

# Create an alias and a shallow copy
alias_list = original_list
shallow_copy = original_list.copy()

alias_position = int(input())
alias_value = int(input())

copy_position = int(input())
copy_value = int(input())

alias_position = alias_position - 1
copy_position = copy_position - 1

# Update one value through the alias
alias_list[alias_position] = alias_value

# Update one value in the copied list
shallow_copy[copy_position] = copy_value

different_positions = 0

for i in range(value_count):
    if original_list[i] != shallow_copy[i]:
        different_positions += 1

# Compare both lists position by position
if shallow_copy == original_list:
    check = "Yes"
else:
    check = "No"

# Display all results
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Copied List: {shallow_copy}")
print(f"Alias Shares Storage: {check}")
print(f"Different Positions: {different_positions}")