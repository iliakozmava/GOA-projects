# 1
score = int(input("შეიყვანე ქულა "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 2
num = int(input("შეიყვანე რიცხვი "))

if num > 0:
    print("დადებითი")
elif num < 0:
    print("უარყოფითი")
else:
    print("ნული")

# 3
num1 = int(input("პირველი რიცხვი "))
num2 = int(input("მეორე რიცხვი "))

if num1 > num2:
    print("პირველი ნომერი მეტია მეორეზე")
else:
    print("მეორე ნომერი უფრო მეტიო პირველზე")

# 4
num = int(input("შეიყვანე რიცხვი "))

if num % 2 == 0:
    print("ლუწი")
else:
    print("კენტი")

# 5
temp = int(input("შეიყვანე ტემპერატურა ცელსიუსში "))

if temp < 0:
    print("ცივი ❄️")
elif temp <= 30:
    print("ნორმალური 🌤️")
else:
    print("ცხელი ☀️")
