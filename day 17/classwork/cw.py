# 1)
number = (input("input number: "))

if number > 0:
    print("the number is +")
elif number < 0:
    print("the number is -")
else:
    print("the number is 0")

# 2)
weather = input("input weather: ")

if weather == "sun":
    print("put on sunglasses")
elif weather == "rain":
    print("get a umbrella")
elif weather == "cold":
    print("put on coat")
elif weather == "snow":
    print("stay home to be warm")
else:
    print("idk this weather")

    # 3)
age = int(input("input age: "))
ticket = input("do you have ticket?(yes/no): ")

if age >= 18 and ticket == "yes":
    print("you can enter")
elif age < 18 and input("are you with parent? (yes/no): ") == "yes":
    print("you can enter")
else:
    print("you cant enter")