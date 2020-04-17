name = "this is global name"

def greet():
    name = "sammy"

    def hello():
        print("hello "+name)
    hello()
greet() #output hello  sammy
print(name) #output this is global name


#global keywords

x = 50

def func():
    global x #allows you to reassign the global varibales
    x = 1000

print ("before function call, x is : ",x)
func()
print ("after function call, x is : ",x)
