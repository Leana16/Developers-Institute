#Exercise 1
def display_message(course):
    print(f'I am learning {course}')
display_message('Web Programming')

#Exercise 2
def favorite_book(title):
    print(f'One of my favorite books is {title}')
favorite_book('Alice in Wonderland')

#Exercise 3
def describe_city(city, country = 'Cameroon'):
    print(f'{city} is in {country}')
describe_city(city = 'Yaounde')

#Exercise 4


#Exercise 5
def make_shirt(size = 'large', text = 'I love python'):
    print(f'The size of the shirt is {size} and the text is {text}')
make_shirt(size = 'large')
make_shirt(size = 'medium')
make_shirt('XL', 'Boom')
make_shirt(size = 'XXL', text = 'it`s your size')

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(mag_name):
    for name in mag_name:
        print(name)

# def make_great(magic):
#     for mag in (magic):
#        print('the great {}'.format(magic[mag]))
# make_great(magician_names)
# show_magicians(magician_names)

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)

shelter_dog = Dog(name_of_the_dog="Rex")
# or
shelter_dog = Dog("Rex")