#1
letters = ['a','b','c','d','e','f','g','h']

print(letters[0])
print(letters[1])
print(letters[2])
print(letters[3])

#2
num = [10,20,30,40,50,60,70,80,90,100]
num[2] = 111
num[1] = 222
print(num)

#3
numbers = list(range(1,21))
even_list = []

s = 0
for n in numbers:
    if n % 2 == 0:
        s = s + n
        even_list.append(n)

print(s)
print(even_list)

#4
nums = [1,2,3,4,5,6,7,8]

print(nums[2:6]) 
print(nums[-3:])

#5
letters = list("wasdwasdwasd")
print(letters[1::2])

#6
lst = [1,2,3,4,5,6,7]

for x in lst:
    if x % 2 == 0:
        print("number evan")
    else:
        print("number od")

#7
l = [1,2,3,2,1]
if l == l[::-1]:
    print("same backwerds")
else:
    print("not same backwerds")

#8
mix = ["hi", 5, 7.5, 3, 9.2, "ok"]
floats = []

for x in mix:
    if type(x) == float:
        floats.append(x)

print(floats)

#9
nums = [1,2,3,4,5,6,7,8,9,10]
nums_moer = nums[::-1]
print(nums_moer)