#key value pair
my_stuff = {"key1":"value1","key2":"value2"}

print(my_stuff)
print(my_stuff['key1'])

my_stuff1 = {"key1":"value1","key2":"value2","key3":{"1":"value3","2":[1,2,3,"sagar"]}}

print(my_stuff1['key3']['2'][2])
print(my_stuff1['key3']['2'][3].upper())

#adding the stuffs in dictionaries
food = {"lunch":"pizza","bf":"eggs"}
food['lunch'] = "burger" #reassigns the lunch  key value
food['dinner'] = "rice" #adding new item
print(food)
