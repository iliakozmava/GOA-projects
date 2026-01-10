#2
def hello():
    print("Hello")

#3
def count_even(numbers):
    count = 0
    for x in numbers:
        if x % 2 == 0:
            count = count + 1
    return count

#4
def greet(name, surname):
    return "Hello " + name + " " + surname

#5
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
#6
# print აჩვენებს ტექსტს ეკრანზე
# return აბრუნებს მნიშვნელობას ფუნქციიდან

# print ვერ გამოიყენება სხვა კოდში
# return შეიძლება შეინახო ცვლადში