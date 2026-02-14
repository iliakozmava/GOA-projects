# 1
def my_join(lst, sep):
    result = ""
    for i in range(len(lst)):
        result = result + lst[i]
        if i != len(lst) - 1:
            result = result + sep
    return result

print(my_join(["hello", "world"], " "))


# 2
def my_split(string, sep):
    result = []
    current = ""
    for c in string:
        if c == sep:
            result.append(current)
            current = ""
        else:
            current = current + c
    result.append(current)
    return result

print(my_split("hello world", " "))


# 3
names = ("ilia", "cotne", "lasha")
a, b, c = names
print(a)
print(b)
print(c)


# 4
age = 13
nums = (1,2,3,4,5,6,7,8)
nums = nums[:4] + (age,) + nums[5:]
print(nums)


# 5
# * ოპერატორი unpacking-ისთვის გამოიყენება
# მაგ: სიიდან ან tuple-იდან მნიშვნელობების გადანაწილება ცვლადებზე


# 6
items = (1,2,3,4,5,6,7,8,9,10)

v1, v2, *v3, v4, v5 = items

print("v1 =", v1)
print("v2 =", v2)
print("v3 =", v3)
print("v4 =", v4)
print("v5 =", v5)