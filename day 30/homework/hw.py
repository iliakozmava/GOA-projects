# 3
data = ("ilia", "13", "tbilisi")

name, age, city = data

print(name + " is " + age + " years old and lives in " + city)

# 4 join clone
def join_clone(sy, arr):
    res = ""
    for x in arr:
        res = res + x + sy
    return res[0:len(res)-1]

print(join_clone("$", ["ilia", "gabo", "barbare"]))


# split clone
def split_clone(txt, ch):
    res = []
    w = ""
    for let in txt:
        if let != ch:
            w = w + let
        else:
            res = res + [w]
            w = ""
    res = res + [w]
    return res

print(split_clone("gamarjoba rogor xar", " "))