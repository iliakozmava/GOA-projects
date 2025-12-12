# 1)
surname = "kozmava"
print(surname.find("m"))


# 2)
letters = ["k","o","z","m","a","v","a"]
count = 0

for x in letters:
    print(x)
    count = count + 1

print(count)


# 3)
name = input()

# 1
print(name.upper())

# 2
print(name.lower())

# 3
print(name.capitalize())

# 4
mid = len(name) // 2
print(mid)

# 5
print(name[::-1].upper())

# 6
print(name.swapcase())