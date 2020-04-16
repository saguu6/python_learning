#check wether 1,2,3 is present in the list
#ex-1
def arrayCheck(nums):
    a = [1,2,3]
    for i in a:
        z = i in nums
    print(z)



arrayCheck(nums=[1,2,3,1])
arrayCheck(nums=[1,2,4,1])
arrayCheck(nums=[1,2,1,2,3])

#ex-2
#from given string get new string

def stringBits(str):
    print(str[::2])

stringBits('Hello') #==> 'Hlo'
stringBits('Hi') #==> 'H'
stringBits('Heeololeo') #==> 'hello'

#ex3
#given 2 strings find any string at the end of the other string retuen true

def end_other(a,b):
    #return(b.endswith(a) or a.endswith(b))
    #return a[-(len(b)):] == b or a == b[-len(a):]
    c = len(a)
    d = len(b)
    if c > d:
        e = c - d
        f = a[e:]
        print(f.lower() == b.lower())
    else:
        e = d - c
        f = b[e:]
        print(f.lower() == a.lower());


end_other('Hibc','abc')
end_other('AbC','HiaBc')
end_other('abc','abXabc')

#ex4
#in given string double the characters eg 'the' ==> 'tthhee'

def doubleChar(str):
    result = ''
    for char in str:
        result += char*2
    print(result)

    """
    i = 0
    z = len(str)
    str1 = ''
    while i < z:
        str1 = str1 + str[i]+str[i]
        i = i+1
    print(str1)
"""


doubleChar('The')
doubleChar('AAbbcc')
doubleChar('Hi-There')


#ex5
#sum of the integers . if the numbers come under teen then take it as 0 i.e fropm 13 to 19 excpet 15 and 16

def no_teen_sum(a,b,c):
    """
    l = [0,0,0]
    l[0] = a
    l[1] = b
    l[2] = c
    sum = 0
    a = [13,14,17,18,19]
    for i in l:
        if i in a:
            fix_teen(i)
        else:
            sum = sum + i
    print(sum)
"""
return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    #print(n)
    if n [13,14,17,18,19]:
        return 0
    return n

no_teen_sum(1,2,15)
no_teen_sum(2,13,1)
no_teen_sum(2,1,14)

#ex6
#find the even integer in the given listd

def count_even(num):
    count = 0
    for i in num:
        if(i%2==0):
            count = count + 1
    print(count)

count_even([2,1,2,3,4])
count_even([2,2,0])
count_even([1,3,5])
