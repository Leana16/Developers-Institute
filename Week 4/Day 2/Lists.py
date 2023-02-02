
#Modify
my_hobbies=["Food", "Sleep", "Code"]
my_hobbies[2] ='TV'
print(my_hobbies)

#Add
my_hobbies=["Food", "Sleep", "Code"]
my_hobbies.append('Football')
print(my_hobbies)

#Remove
my_hobbies=["Food", "Sleep", "Code"]
my_hobbies.remove('Sleep')
print(my_hobbies)

#Adding two lists
my_hobbies=["Food", "Sleep", "Code"]
my_hobbies2 =["TV", "Footbal"]
print(my_hobbies + my_hobbies2)

#Others
num = [3, 5, 1, 2]
print(sorted(num))

print(sum(num))

print(len(num))

#inserting at beginning and last position
food = ['spaghetti', 'pizza', 'hambuguer']
food.insert(1, 'kok')
print(food)

food.insert(4, 'sanga')
print(food)

#inserting several elements at the end
food = ['spaghetti', 'pizza', 'hambuguer']
food.extend(['riz', 'noddles'])
print(food)

#Lists
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1[3])

list1[3]  = 200
print(list1)

#Turples
a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)

#Sets(remove duplicates)
this = set()
this = {"banana", "apple", "cherry", "apple"}
print(this)

#Range
number = range(6, 27)
for num in number:
    print(num)

#lists in array
num = list(range(6, 27))
print(num)


user = int(input("Enter a number"))
for num in range(1, 11):
    print(str(num) + '*' + str(user) + '=' + str(num * user))
    print(num * user)

#while loop
i = 1
while i <= 9:
    print(i)
    i += 1

password = ''
while password != 'hello-world-123':
  password = input('What is the top secret password? ')

print('You guessed the right password!')