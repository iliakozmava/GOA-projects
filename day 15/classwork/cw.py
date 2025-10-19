# 1
# == ნიშნავს უდრის
# != ნიშნავს არ უდრის

# == მაგალითები
print(5 == 5)
print(10 == 8)
print("hi" == "hi")

# != მაგალითები
print(5 != 3)
print(7 != 7)
print("dog" != "cat")

# 2
# Conditional Statement ნიშნავს როცა კოდი ამოწმებს რამე მართალია თუ არა

# keyword ები
# if ნიშნავს თუ
# elif ნიშნავს სხვა თუ
# else ნიშნავს სხვა შემთხვევაში

# 3
age = int(input("enter your age "))

if age > 18:
    print("you are an adult!")
elif age == 18:
    print("you are 18yo!")
else:
    print("you are teenager!")

# 4
i = 0
while i < 5:
    print("ilia")
    i = i + 1

# 5
sum = 0
for i in range(1, 7):
    print(i)
    sum = sum + i

print("total sum is", sum)

# 6
user_name = input("enter your name ")
my_name = "ilia"

if user_name == my_name:
    print("the names are the same")
else:
    print("the names are different")