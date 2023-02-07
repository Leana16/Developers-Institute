from functools import reduce
#arg
# s is a tuple of args
def check_arguments(*args):
    print(f"These are the arguments {args}")
(check_arguments(1, 2, 'hey', 'hello', 'bjr'))

def check_multiple(*args):
    return sum(args)

check = check_multiple(5, 11, 12, 16, 17, 26, 29 )
print(f'The sum is {check}')

#kwargs is a dictionary of args
def  check_keyword(**kwargs):
    print(kwargs)

check_keyword(name="Sarah", age=24)

def check_keyword(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

check_keyword(name="Sarah", age=24)

#args and kwargs together
def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments_keywordedarguments("required argument")
check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)

def check(*args,**kwargs):
    print('*args', args)
    print('**kwargs', kwargs)

check_arguments_keywordedarguments(10,20,30,name='John',surname='Doe')

# starred parameter & double-starred parameter
def check(a, *numbers, **person):
    print('Greetings : ', a)

    #iterate through all the items in tuple
    for num in numbers:
        print('num - ', num)

    #iterate through all the items in dictionary    
    for key, value in person.items():
        print(key + ': ' + value)


check("hello", 1,2,3,name="John",surname="Doe")

# Passing *Args And **Kwargs As Arguments
def check(a, b, c):
    print(a, b, c)

a = [1,2,3]
check(*a)

a = {'a':'Sarah', 'b':24, 'c': 180}
check(**a)

#maps
def upper_string(s):
       return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object))

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5, 6]
squared = map(square, numbers)
print(list(squared))

#filter(selects a paticular letter or num)
def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))

#Functools.reduce()

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
map_pple = map(lambda p: p.lower(), people)
print(list(map_pple))

filter_pple = filter(lambda p: len(p) <= 4, people)
print( 'hello', list(filter_pple))