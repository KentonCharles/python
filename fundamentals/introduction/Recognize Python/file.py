num1 = 42 #variable declaration, data type - number, integer
num2 = 2.3 # variable declaration, data type - number, float
boolean = True #variable declaration, data type - boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#variable declaration, data type - composite list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable delaration, data type - composite list, dictionary
fruit = ('blueberry', 'strawberry', 'banana')
#variable declaration, data type - composite list, tuples
print(type(fruit)) #output: tuples
print(pizza_toppings[1]) #output: 'sausage'
pizza_toppings.append('Mushrooms') #appends 'mushrooms' to pizza toppings list
print(person['name']) #output: 'John'
person['name'] = 'George' #changes name to 'George' in dictionary
person['eye_color'] = 'blue' #appends 'eye_color': 'blue' to dictionary
print(fruit[2]) #output: 'banana'

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
    #conditional, output: "It's lower"

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    #conditional, output:"Just right!"

for x in range(5):
    print(x) #output:5, for loop
for x in range(2,5):
    print(x) #output: 2,5, for loop
for x in range(2,10,3):
    print(x) #output: 2,10,3, for loop

x = 0
while(x < 5):
    print(x)
    x += 1 #output: 0,1,2,3,4, while loop

pizza_toppings.pop() #pizza_toppings =['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']
pizza_toppings.pop(1) #pizza_toppings = ['Pepperoni', 'Jalepenos', 'Cheese']

print(person) #output: George, Salt Lake, 37, blue
person.pop('eye_color') #output: blue
print(person) #output: George, Salt Lake, 37

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    #for loop, output: 'After 1st if statement'

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
    #function, output: 'Hello'

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
    #function, output: 'Hello', 'Hello', 'Hello', 'Hello'

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #function, output: 'Hello','Hello','Hello','Hello','Hello','Hello','Hello','Hello','Hello','Hello'
print_hello_x_or_ten_times(4) #function, output: 'Hello','Hello','Hello','Hello'


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)