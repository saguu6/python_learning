#errors
# f = open('simple.txt','r')
# f.write("test write to simple text")
# print("hello world")
try:
    f = open('simple.txt','r')
    f.write("test write to simple text")
# if excpetion error is not specified then it will throw same error message for any exception
# except:
#     print("Error : could not find file or read data")
except IOError: # except is a keyword excpetion is IOError
    print("Error : could not find file or read data")

#if no exception error then else will be executed
# else:
#     print("success")
#     f.close()

#finally will be executed at anycost
finally:
    print("I always work")
