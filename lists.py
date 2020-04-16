#lists is nothing but array in other languages

a = ['a',1,2,"sagar",[1,2,3,4]];
print(a)
print(a[-1])
print(a[1])
print(a[3])
print(a[4])
#slicing
print(a[2:]) #starting from index 2
print(a[:3]) #strating from 0 to 2
a[0] = "shetty" #replaces the the index 0 with shetty
print(a)

#appending the items in the lists
a.append('abc') #appending at the end
print(a)
a.append([0,9,8]) #appends this list at the end of the lists
print(a)

a.extend("a")
print(a)
b = ['x',"abc",1,2]
a.extend(b) #extends the lists
print(a)

#removing item from the listd
# c = a.pop(); #removes last item
# print(c)

c = a.pop(1) #removes the item of index 0
print (c)

# d = [5,1,8,2,3,4];
# d.reverse() #permanently reverses the list
# print(d)
#
# d.sort() #permanently sorts the list in ascending order
# print(d)

#nested list

d = [1,2,['x','y','z']]
print(d[2][1])

#lisst comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix] #row[0] means 0th index in each row of row in matrix
print(first_col) #output 1,4,7
sec_col = [row[1] for row in matrix]
print(sec_col); #output 2 5 8
