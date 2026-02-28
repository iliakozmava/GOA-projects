# 1
def remove_chars(words, chars):
    result = []
    i = 0
    while i < len(words):
        word = words[i]
        new_word = ""
        j = 0
        while j < len(word):
            letter = word[j]
            found = False
            k = 0
            while k < len(chars):
                if letter == chars[k]:
                    found = True
                k = k + 1
            if found == False:
                new_word = new_word + letter
            j = j + 1
        result.append(new_word)
        i = i + 1
    return result

words = ["ilia", "jemala", "lika"]
chars = "wasd"
print(remove_chars(words, chars))


# 2
favorites = ["warriors", "tea", "short cake", "nature", "sports"]
print(favorites)

favorites.append("tea")
favorites.remove("warriors")

print(favorites)


# 3
numbers = (7, 14, 3, 28, 19)
print(numbers)

print(numbers[1])

print(numbers[4])

print(10 in numbers)


# 4
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)

my_set.add(6)
my_set.remove(2)
my_set.discard(99)

print(my_set)