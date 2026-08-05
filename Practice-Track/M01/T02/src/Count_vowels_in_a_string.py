text = input()

vowel_count = 0

# Iterate directly over the string and count the vowels
for char in text:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")