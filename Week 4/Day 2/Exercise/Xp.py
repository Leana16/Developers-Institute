# my_fav_numbers = set()
# my_fav_numbers = {5, 16, 26, 26}
# # my_fav_numbers.push()
# print(my_fav_numbers)

# my_fav_numbers.remove()
# print(my_fav_numbers)

#exercise 2
turple = (1, 2, 3, 4, 5, 6)
turple += (7, 8, 9)
print(turple)

#Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
print(basket)

basket.remove('Blueberries')
print(basket)

basket.append('Kiwi')
print(basket)

basket.insert(0, 'Apples')
print(basket)

print(len(basket[0:2]))

basket.clear()
print(basket)

#Exercise 4
#A float is a floating-point numbers meaning numbers that has a decimal point

 #a = 1
# lst = []
# for i in range(1,9):
#     a += 0.5
#     lst.append(a)
# print(lst)

# b = list(np.arange(1,5.5,0.5))
# print(b)

#Exercise 5
number = range(1, 21)
for num in number:
    print(num)
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# num = [i for i in range(1, 21+1) if i % 2 == 0]
# print(*num)

#Exercise 6
name = 'leana'
user = input('Enter your name: ')
while user != name:
    user = input('Enter your name: ')
else:
    print('Done!')

#Exercise 7
user = input('Input your favorite fruit(s): ')
users = user.split()
print(users)

ask = input('Input the name of any fruit: ')
if ask in user:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')

#Exercise 8
# topping = []
# while True:
#     toppings = input('Enter a series of toppings: ')
#     print(f'you’ll add that {} to their pizza')
    
#     if topping == 'quite':
#         print('')

#Exercise 10 & 11
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

sandwich_orders.extend(['pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich'])
print(sandwich_orders)
print('sorry the deli has run out of pastrami')

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)

for food in sandwich_orders:
    finished_sandwiches.append(food)
    print('I made your {}'.format(food))
print(finished_sandwiches)