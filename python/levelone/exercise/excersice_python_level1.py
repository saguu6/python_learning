#given string

s = 'django'

#using index print
#'d'
print(s[0])
# o
print(s[-1])
#djan
print(s[:4])
#jan
print(s[1:4])
#go
print(s[4:])
#reverse the string
print(s[::-1])


#given list

l = [3,7,[1,4,'hello']]

#reassign hello to good bye

l[2][2] = "good bye"
print(l)

#using key value and indexing grab hello

d1 = {"simple":"hello"}

d2 = {"k1":{"k2":"hello"}}

d3 = {"k1":[{"nest_key":['this deep',['hello']]}]}

print(d1['simple'])
print(d2['k1']['k2'])

print(d3['k1'][0]['nest_key'][1][0])


#use set to get unique values in listd
mylist = [1,1,1,1,2,2,2,2,3,3,3]
a = set(mylist)
print(a)


#given 2 string varuables

# name = "sammy"
# age = 4

#formate the string
#hello my dog name is sammy and he is 4 years old

x = "hello my dog name is {name} and he is {age} years old".format(name="sammy",age="4")
print(x)
