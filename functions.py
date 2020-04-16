#functions
#functions in python use def keywords
#function name is in snake case
#def my_func(param1 = 'default value');

def my_func():
    print("my first function")

my_func() #calling the function

def my_new(param1='default'):
    """
        This is the doc string
        its like the comment-->  what the function does..
        its good use
    """
    print("my firt function {}".format(param1))

my_new();
#returning the data
def return_data():
    return "hello"

result = return_data()
print(result)

#functions with some operations

def my_op(num1,num2):
    return num1 + num2

r = my_op(1,2)
print (r) #output -- > 3

r1 = my_op("1","2")
print(r1) #output 12

r2 = my_op("hello","")
print(r2) #ourput hello

print(type(r2)) #output will be <type 'str'> or <class 'str'>

def addNum(num1,num2):
    if type(num1)==type(num2):
        return num1 + num2
    else:
        return "sorry"

r4 = addNum(1,"2")
print(r4) #output sorry



#lambda experssion

#filter

mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

even = filter(even_bool,mylist)
#filter function takes 2 parameters function name and sequence or tuples or sets
print(list(even))

#lamba functions is a small anonymous functions

evens = filter (lambda num:num%2 == 0,mylist)
print (list(evens))

#to find whether the value is present in the listd

print('x' in [1,2,3,4]) #output false
print('x' in [1,2,3,4,'x','y']) #output true
