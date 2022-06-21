#find the first repeated character of a given string where the index of first occurrence is smallest ?

# str2 = {}

# string1 = "SBaamdKLK"

# for i in string1:
#     if i in str2:
#         print(i, string1.index(i))
#     else:
#         str2[i]=0
#         print("none")



def repeted_char(str1):
  temp = {}
  for each in str1:
    if each in temp:
      return each, str1.index(each)
    else:
      temp[each] = 0
  return 'None'
print(repeted_char("sbavadacabc"))
print(repeted_char("bscascb"))
print(repeted_char("abczcvdasacc"))
print(repeted_char("ballssacxxy"))
print(repeted_char("dafebfbc"))


# A Python program to print all
# combinations of a given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3,4,5,6,7,8], 3)

# Print the obtained combinations
counter = 0 
for i in list(comb):
    counter+=1
print(counter)


# print all permutations with given repetition number of given string ?

per_str = combinations(["a","b","c","d","e","m"],3)

counter = 0 
for i in list(per_str):
    counter+=1
print(counter)