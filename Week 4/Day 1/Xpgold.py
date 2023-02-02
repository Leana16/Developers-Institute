#Exercise 1
print('Hello World\n'*4 + 'I love python\n'*4)

#Exercise 2
month = int(input('Enter a month 1 to 12:'))
if(month >= 3 and month <= 5):
   print('Spring')
elif(month >= 6 and month <= 8):
    print('Summer')
elif(month >= 9 and month <= 11):
    print('Autumn')
elif(month <= 2 or month == 12):
    print('Winter')

#Exercise 3
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum." 
print(len(my_text))

#Daily challenge
import random
user = input('Input a string of 10 characters')
length = len(user)

if length < 10:
    print('string not long enough')
elif length > 10:
    print('string too long')
else:
    print('the first string is' + user[0], 'and' 'the last string is' + user[-1])

x = " "
for name in range(1, len(x) + 1):
    print(x[:name])

len = " "
for name in user:
    len += name
    print(len)

shuffle = " "
for name in user:
    shuffle += name
    s = list(shuffle)
    random.shuffle(s)
    print("".join(s))
