#passing info to a function
def hello(username):
    print("Hello ",username)
hello('Daphne')

#Accepts more than one argument
def hello(username, language):
    if language == "EN":
        print("Hello ", username)
    elif language == "FR":
        print("Bonjour ", username)
    else:
        print('this language is not supported')
hello('Leana', 'FR')

def hello(name, age):
    print(f'Salut {name}, tu as {age} ans')
hello('Solange', 40)

#return a value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

def Division(num):
 return num/3

div = Division(9)
print(div)

#returning multiple values with turple
def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

first, last = format_name("kunchu", "leana")
print(first)
print(last)

#exercise
def calculation(a, b):
    return (f' The sum is {a + b}, and the sub is {a - b}')

rest = calculation(40, 20)
print(rest)

#passing a list as a function argument
def greeting(users):           
    for user in users:              
        print("Hello " + user.title() ) 

usernames = ["steve", "daphne", "modest"]
greeting(usernames)

#Modifying A List In A Function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

while len(unprinted_designs) != 0:    
    current_design = unprinted_designs.pop() 

    print("Printing model: " + current_design)    
    completed_models.append(current_design)    

# print("\nThe following models have been printed:") 
# for completed_model in completed_models:    
    print(completed_models)