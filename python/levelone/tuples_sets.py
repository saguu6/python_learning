#tuples are immutable

t = (1,2,3)

print(t[0])
print(t[-1])

#t[0] = 4 #canot assaign a new value like strings
#it doesnt have any methods

#sets
#are undordered list
a = set([])

a.add(1)
a.add(2)
a.add(3)
a.add(3)
print(a)

y = set([1,2,2,3,3,1,4])
print(y)
