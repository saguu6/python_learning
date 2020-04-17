#regular expression is used to search for patterns in the stringBits
import re   #reqular expression

patterns = ['term1','term2']

text = 'this is a string term1, not the other! term2'
"""
for p in patterns:
    print("searching for :"+p)

    if re.search(p,text): #re function
        print("match")
    else:
        print("no match")
"""

match = re.search('term1',text)

print(match.start()) #it will return the starting index number from where the pattern matching starts

split_term = '@'

email = 'user@gamil.com'

print(re.split(split_term,email)) #splits the string at @

#lenth of the list -> given how many times match is present
print(len(re.findall('match','text phare match is match'))) #find the how many time match is present in the string and lists it

## reputation syntax

def multi_re_find(patterns,pharse):
    for pat in patterns:
        print("searching for patterns{}".format(pat))
        print(re.findall(pat,pharse))
        print('\n')

test_pharse = 'sdsd..sssddd..sdddsddd....dsds...dsssss....sddddd'

test_patterns = ['sd*'] #this means search for pattern s follwed by d* [*menas 0 or more]
test_patterns1 = ['sd+']#+ means 1 or more d
test_patterns2 = ['sd?'] #? means 0 or 1  time d
test_patterns3 = ['sd{3}'] #follwed by 3 ds
test_patterns4 = ['sd{2,3}'] #follwed by 2 or 3 ds
test_patterns5 = ['s[sd]+']#s follwed by one or more s or d

#exclusion

test_p = 'This is a string ! but is has. how we remove? 123 456'
#test_pat = ['[^!.?]+'] #since there is a ^ symbol it removes those charcters and splits the string into listins
# test_pat = ['[A-Z]+'] #retuens upper case letters
# test_pat = ['[a-z]+']
test_pat = [r'\d+'] #finding digits r is used for literals
#\D not digits
#\s spaces
#\S not spaces
#\w letters and digits
#\W special charcters with spaces
multi_re_find(test_patterns,test_pharse)
multi_re_find(test_patterns1,test_pharse)
multi_re_find(test_patterns2,test_pharse)
multi_re_find(test_patterns3,test_pharse)
multi_re_find(test_patterns4,test_pharse)
multi_re_find(test_patterns5,test_pharse)

multi_re_find(test_pat,test_p)
