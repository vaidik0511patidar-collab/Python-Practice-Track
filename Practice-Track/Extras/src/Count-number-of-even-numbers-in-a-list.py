lst = []
n = int(input())

for i in range(n):
    num =  int(input())
    lst.append(num)

even_count = 0

for num in lst:
    if num % 2 == 0:
        even_count += 1

print("The count of even numbers in the given list is:",even_count)