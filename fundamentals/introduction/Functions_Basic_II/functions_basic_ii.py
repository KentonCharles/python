#1 - Countdown
list = []
def countdown(num):
    for i in range(num):
        list.append(num)
        num -=1
countdown(5)
print(list)

#2 - Print and Return
def print_and_return(a,b):
    print(a)
    return b
message = print_and_return(1,3)
print(message)

#3 - First Plus Length
def first_plus_length(list):
    x = len(list)
    sum = (list[0]) + x
    print(sum)
first_plus_length([1,2,3,4,5])

#4 - Values Greater than Second
new_list = []
def values_greater_than_second(list) :
    count = 0
    for i in range(len(list)):
        if(list[i] > list[1]):
            count += 1
            new_list.append(list[i])
    print(count)     
    return(new_list)
    
list2 = values_greater_than_second([5,2,3,1,4])
print(list2)

#5 - This Length, That Value
def length_and_value(size,value):
    new_list2 = []
    for i in range(size) :
        new_list2.append(value)
    return(new_list2)

x = length_and_value(6,2)
print(x)