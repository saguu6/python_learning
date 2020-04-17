
import one

print("Top level two.py")

one.func()

if __name__ == '__main__':  #used to check whether the file is being imported or directlt runing
    print("two.py is being run directly")
else:
    print("two.py has been imported")
