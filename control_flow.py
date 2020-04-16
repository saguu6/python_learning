# #operators
#
# 2 > 1
#
# 1 < 2
#
# 2 >= 1
#
# 1 <= 2
#
# 1 != 2
#
# #there is not data type equality in python i.e ===
#
# 1 == 1 # return true
#
# 1 == "1" #returns false

#logical orperators
# in python logical operators are 'and' and 'or' keywords

# (1 > 2) and (2 > 3)
#
# (1 > 2) or (2 > 3)


#if statments
#in python therte is no need of brackets after if statements, it will get to know the code block by indentation

if 1 < 2:                   #colon indicates the code block
    print("true")


if 1 > 2:
    print("true")
else:
    print("false")

#else if is written in shortcut form as "elif"

if 2 < 1:
    print("if statements")
elif 2 == 2:
    print("elif statement")
else:
    print("else statement")


#loops

seq = [1,2,3,4,5,6]
# item name cane be any name

for item in seq:
    print item

for abc in seq:
    print abc

#for loop in dictionary

d = {"key1":1,"key2":2}

for item in d:
    print item #goin to print the keys -- > output is key1 key2

for k in d:
    print(k)
    print(d[k]) #prints the values

#looping tuples inside the lists
mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print (item) #prints the tuples (1,2),(3,4),(5,6)

#unpacking the tuples

for t1,t2 in mypairs:
    print(t1)
    print(t2) #output 1 2 3 4 5 6

#while loops
i = 1

while i < 5 :
    print ("i is : {}".format(i) )
    i = i + 1

#RANGE FUNCTIONS
#to get the value from 1 to 5
#[1,2,3,4,5]
range(1,5) #output [1, 2, 3, 4] not including 5
list1=list(range(0,5))
print(list1)  #output [0, 1, 2, 3, 4]

list_even = list(range(0,20,3))
print(list_even) #output [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] without including 20

for a in range(10):
    print(a) #output prints 0 to 9 not including 10


#list comprehension

x =[1,2,3,4]
out = []
for num in x:
    out.append(num) #appends all the number into out
print(out)

out = [num for num in x] #one more way of for loop 

print out
