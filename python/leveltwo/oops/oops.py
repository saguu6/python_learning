class Sample():
    pass

x = Sample()

print(type(x))

#class with atributes and methods

class Dog():
    #class obect attribute
    species = "mammal"
        #this function is called automatically when a class is being initiated
        #slef indicates the current instance of the class and used to access tyhe vaariables of that class ---> its name can be anything
    def __init__(self,breed,name):  #init is initialization .. self is its parameter
        self.breed = breed
        self.name = name

mydog = Dog(breed="lab",name="sammy")
mydog1 = Dog("huskie","jhon")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
print(mydog1.breed)
print(mydog1.name)


#classes with actual methods
class Circle():
    pi = 3.14 #object level attibute

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        """
        #self key says that its the method of this class
        #self.radius is used because it will get confused which radius to call whether the radius defined from other places
        #self tells the function to look into the radius defined in the class
        #Cricle.pi is used because its object level attribute
        """
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
print (myc.area()) #output 28.26
print(myc.radius) #ouput 3
myc.radius = 100
print (myc.area()) #output 31400.0

myc.set_radius(10)
print(myc.area()) #output 314.0

#inheritence

class Animal():
    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        print("dog creted")

    def bark(self):
        print("woof")

    def eat(self): #overiding
        print("dog eating")

mya = Animal()
mya.whoAmI()
mya.eat()

myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()

#special methoads

class Book():
    def __init__(self,title,author,page):
        self.title = title
        self.author = author
        self.page = page

    def __str__(self): #string representation of the object
        return "title : {}, author : {}, pages : {}".format(self.title,self.author,self.page)

    def __len__(self): #when built in function len is called with the obejct of the class this function will be executed
        return self.page

    def __del__(self): #when del function is called
        print("a book is destroyed")

b = Book("python","sagar",500)
print(b) #__str__ is called
print(len(b)) #__len__ function is called
del b  #__del__ function is called
