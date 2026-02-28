# -1
# list: იცვლება შეიძლება განმეორდეს ნამიმდევრობა აქვს []
# tuple: არ იცველბა შეოძლება განმეორდეს Nამიმდევრობა აქვს ()
# set: იცვლება განმეორდება არ შეიძლება თანმიმდევრობა არ აქვს {}

# 0
# add(): ერთი ელემენტი ემატება
# update(): ბევრი ელემენტი ერთდროულად ემატება
# remove(): შლის ელემენტს (თუ არ არსებობს)
# discard(): შლივ ელემენტს (თუ არ არსებობს)
# union(): ორ set-ს აერთებს ახალ set-ს ქმნის

# 1
group1 = set()
group2 = set()

# 2
group1.add(50)

# 3
group2.update([10, 20, 30, 40, 50])

# 4
group1.remove(50)

# 5
group2.discard(99)

# 6
group3 = group1.union(group2)

# 7
print("group1:", group1)
print("group2:", group2)
print("group3 (union):", group3)

# 8
numbers = (7, 2, 8, 2, 9, 4, 2, 11, 7, 5)

# 9
print("element 3", numbers[2])
print("element 7", numbers[6])

# 10
print(numbers[1:6])

# 11
print(numbers.count(2))

# 12
print(numbers.index(9))

# 13
numbers2 = (3, 3, 1)
all_numbers = numbers + numbers2
print(all_numbers)