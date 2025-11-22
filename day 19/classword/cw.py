#1
fruits = ["Apple" "Banana" "Orange"]

print(fruits[0])
print(fruits[-1])

new_ting = ["Mango"]
fruits = fruits + new_ting

fruits[2] = "Kiwi"

print(fruits)



#2
nums = [1, 2, 3, 4, 5, 6, 7]

print(nums[0:3])
print(nums[-2:])
print(nums[2:6])
print(nums[::2])



#3
lastname = "kozmava"

turn = lastname[::-1]

print(turn)



#4
# slicing გვიღებს ნაწილს
# mutable ნიშნავს რომ list იცვლება



#5
numbers = [1, 2, 5, 8, 11, 14, 17]

zero = 0

for n in numbers:
    if n % 2 == 1:
        zero = zero + n

print(zero)