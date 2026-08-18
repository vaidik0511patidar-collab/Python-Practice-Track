def count_frequency(sentence,target):
    count = 0
    for char in sentence:
        if char == target:
            count += 1
            
    return count

sentence = "I live in India and I love my India"
target = 'i'

sentence = sentence.lower()

res = count_frequency(sentence,target)
print(f"The frequency of {target} in the sentence {sentence} is: {res}")