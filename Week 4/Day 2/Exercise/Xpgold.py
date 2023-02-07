import random
#Exercise 1
con = ['Daphne', 'Hillary']
cat = ['Sonia', 'Marie']

con.extend(cat)
print(con)

#Exercise 2

for a in range(1500, 2501):
    if a % 5 == 0 and a % 7 == 0:
     print(a)
    
#Exercise 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input('Enter your name: ')
if user in names:
    print(names.index(user))

#Exercise 4
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
print('the largest number is', max(a, b, c))

# largest = ''
# if a > b and a > c :
#     largest = a
# elif b > a and b > c :
#     largest = b
# else :
#     largest = c
#     print('The largest number is', largest)

#Exercise 5
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vow = ['a', 'e', 'i', 'o', 'u']

for cons in alpha:
    if cons in vow:
        print(f'{cons} is a vowel')
    else:
        print(f'{cons} is a consonant')

#Exercise 6
user = input('Input 7 words: ')
words = user.split()
print(words)

letter= input('Input a single character: ')

#Exercise 7
million = range(1, 1000001)
print(min(million))
print(max(million))
print(sum(million))

#Exercise 8
num  = 34,67,55,33,12,98
list = list(num)
print(list)

tuple = tuple(num)
print(tuple)

#Exercise 9
num = random.randint(1, 9)

while True:
    user = int(input('Input a number from 1 to 9: '))
    if user == num:
      print('Winner')
    elif user != num:
      print('better luck next time')
    elif user == 0:
        print('Quite')