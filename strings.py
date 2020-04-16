#strings

#basics of strings
#strings can be written in sigle quotes or double quotes
#'hello' "hello"

# a = 'hello'
# b = "hello"
# print(a)
# print(b)

#indexing of strings

# my_string = 'sagar shetty';
# print(my_string[0]) #first letter 's'
# print(my_string[-1]) #last letter 'y'
# print(my_string[4]) #middle

#slicing of strings

# my_string = 'abcdefg';
# print(my_string[2:]) #from index 2 and slice
# print(my_string[:4]) #slice upto 3 but not including 4
# print(my_string[2:6]) #slicing start from index 2 to 5 but not 6
# print(my_string[::]) #grabs whole string
# print(my_string[::1])#grabs whole string
# print(my_string[::2]) #emits 1 ,3 , 5 index letters
# print(my_string[::3]) #emits 1,2,4,5
# #converting string to upper case
# x = my_string.upper()
# print(x)
# #converting string to lower case
# y = x.lower()
# print(y)
#
# z = y.capitalize() #returns first letter capitailzed
# print(z)
#
# my_name = "sagar shetty"
#
# c = my_name.split() #by default splits from space make lists (some what like array in php) ['sagar', 'shetty']
# print(c)
#
# #d = my_name.split('a') #splits the string into listd of 3 items ['s', 'g', 'r shetty']
# #print(d)
#
# #we can max size of the split
# d = my_name.split('a',1); #splits the string into listd of 2 items ['s', 'gar shetty']
# print(d)

#string formating

x = "insert item here {}".format("insert me") #inserts 'insert me' inside the curly braces
print(x); # output ---> insert item here insert me
y = "item one : {} item two : {}".format("cat","dog") #inserts in place of curly braces
print(y) #output item one : cat item two : dog

z = "item one : {y} item two : {x}".format(x="cat",y="dog") #inserts in place of curly braces
print(z) #output item one : dog item two : cat
