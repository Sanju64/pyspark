
#1. Write a Python program to calculate the length of a string.  
from unittest import result


str1 = "Sanjusali"
a = len(str1)
print(a)

#2. Write a Python program to sum all the items in a list.  

list1 = [1,2,4,5,6,78,9]
b = sum(list1)
print(b)

#0.3. Write a Python program to multiplies each items in a list.  

l1 = [4,5,6,71,20]
for each in l1:
    each *= each
    print(each)


#3 Write a Python program to multiplies all the items in a list. 

pro = 1
mul1 = [1,2,3,4,5,4]
for i in mul1:
    pro*=i
print(pro)
    


#4. Write a Python program to get the largest number from a list. 

larg1 = [2,3,88,4,70,41,71,45]

#print("the lasrgest number is",max(larg1))

larg1.sort()

print("the largest number is",larg1[-1])


#5. Write a Python program to get the smallest number from a list.

larg2 = [2,3,88,4,70,41,71,45]

#print("the min number",min(larg2))

larg2.sort()

print("the minimum number is",larg2[0])

#6. Write a Python program to count the number of characters in a string\Sample String : 'google.com'

#count of the charecters

#1

from collections import Counter

char_count = input("Enter the charecters to Count")

my_counter = Counter (char_count)
print(my_counter)


#2
Count_string = 'Hello World This is the Python code'
print(Count_string.count(input('o')))


#3
# using lambda
test_str = "Python_classes"
count = sum(map(lambda x : 1 if 's' in x else 0, test_str))
  
# result 
print ("Count of s is : "   +  str(count))

#8.Write a Python program to count the number of strings where the string length is 2 or more and the first and last
#  character are same from a given list of strings.  

#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2


def count_words(str1):
    ctr1 = 0

    for each in str1:
        if len(each) >=3 and each [0] == each[-1]:
            ctr1 +=1 
    return ctr1

print(count_words(["cab","wheel","non","mem","1221","pop","mini"]))


#9. Write a Python program to get a list, sorted in increasing order
#  by the last element in each tuple from a given list of non-empty tuples. 

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

def last(n): 
    
    return n[-1]

def sort_end_list(tuples):
  return sorted(tuples, key=last)

print(sort_end_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(2,6)]))

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.  
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String





