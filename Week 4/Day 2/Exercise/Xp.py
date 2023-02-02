# my_fav_numbers = set()
# my_fav_numbers = [1, 4, 6, 9, 16, 26]
# print(my_fav_numbers)

# my_fav_numbers.push()
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
#num = list(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
#print(num)

#Exercise 5
number = range(1, 21)
for num in number:
    print(num)

num = [i for i in range(1, 21+1) if i % 2 == 0]
print(*num)

#Exercise 6
user = input('Enter your name:')
 while user =='leana'
