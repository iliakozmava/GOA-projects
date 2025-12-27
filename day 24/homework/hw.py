# 1
s = input()
print(s.upper())
print(s.lower())

# 2
s = input()
print(len(s))

# 3
numbers = [10, 20, 30, 40]

new_num = 50
numbers.append(new_num)

numbers.pop()

print(numbers)

# 4
fruits = ["aple", "bananana", "aple", "orenge"]

count = 0
for fruit in fruits:
    if fruit == "apple":
        count = count + 1

print(count)

# 5
s = input()

new_s = ""
for c in s:
    if c.isupper():
        new_s = new_s + c.lower()
    else:
        new_s = new_s + c.upper()

print(new_s)

# 6
numbers = [10, 20, 30, 40, 20, 50]

num_to_remove = int(input())

if num_to_remove in numbers:
    numbers.remove(num_to_remove)

print(numbers)