# 1
name = input("name ")
print(name.capitalize())
print(name.upper())

# 2
text = input("text ")
print(text.swapcase())

# 3
items = [1, "a", True, 5.5]
print(len(items))

# 4
text = input("text ")
print(len(text))

# 5
colors = ["red" "blue" "green" "black" "white"]
colors.pop(3)
colors.append("purpl")
colors.pop(len(colors) // 2)
print(colors)

# 6
cars = ["bmw", "audi", "toiota", "fiti", "fordi", "hiundai"]
cars.insert(4, "nisani")
print(cars)

# 7
words = ["aple", "banana", "orenge"]

for word in words:
    print(word.upper())