# 1
print(True and False)   # False
print(True or False)    # True

# 2
name = input("input your name ")
print("correct" * (name == "ilia") + "incorrect" * (name != "ilia"))

# 3
number = int(input("input number "))
print("greater than 50" * (number > 50) + "less than 50" * (number <= 50))

# 4
toy = input("input your favorite toy ")
my_toy = "lego"
print("we like the same toy" * (toy == my_toy) + "we don't like the same toy" * (toy != my_toy))

# 5
print(True and False and True or False and True and False and True and False or True and False or True or False)

# 6
print(2 > 1)      # True
print(3 < 1)      # False
print(5 == 5)     # True
print(4 != 3)     # True
print(6 >= 6)     # True

# 7
print(5 > 2 and 3 < 4)         # True
print(1 == 2 or 2 == 2)        # True
