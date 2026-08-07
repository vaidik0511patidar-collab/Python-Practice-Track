sentence = input()
position = int(input())

# Remove outer spaces and convert the sentence to lowercase
cleaned = sentence.strip().lower()

# Replace the required punctuation marks with spaces
for p in ".,!?;:":
    cleaned = cleaned.replace(p,"")

# Split the sentence into words and rebuild the cleaned sentence
words = cleaned.split()
joined = " ".join(words)
count = len(words)

# Extract the required words and slices
first_word = words[0]
last_word = words[-1]
selected_word = words[position-1]

first_prefix = first_word[:3]
last_suffix = last_word[-3:]

# Display the complete analysis
print(f"Cleaned Sentence: {joined}")
print(f"Word Count: {count}")
print(f"First Word: {first_word}")
print(f"Last Word: {last_word}")
print(f"Selected Word: {selected_word}")
print(f"First Prefix: {first_prefix}")
print(f"Last Suffix: {last_suffix}")