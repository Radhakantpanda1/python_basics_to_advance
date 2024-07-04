"""
Square of Numbers:
Create a list of squares of numbers from 1 to 20.

Even Numbers:
Create a list of even numbers from 1 to 50.

Filter Words:
Given a list of words, create a new list that only contains words that are longer than 4 characters.

Uppercase Letters:
Given a list of words, create a list of these words converted to uppercase.

Conditional Square:
Create a list of squares of even numbers from 1 to 20.

Common Elements:
Given two lists, create a new list that contains only the common elements between the two lists.

Dictionary Keys:
Given a dictionary, create a list of its keys.

Flatten List:
Given a list of lists, flatten it into a single list.

String Lengths:
Given a list of strings, create a list of the lengths of those strings.

Reverse Strings:
Given a list of strings, create a list with each string reversed.


"""
# 1ans
res=[i*i for i in range(1,21)]
print(res)

#2ans
res=[i for i in range(1,51) if i%2==0]
print(res)

#3ans
words=['apple','mango','tomato','pyaj','hippo','gopi']
res=[word for word in words if len(word)>4]
print(res)

# 4ans
res=[word.upper() for word in words ]
print(res)

#5 ans
res=[num*num for num in range(21) if num%2==0]
print(res)

#6ans
listA=['app','bpp','cpp','dpp']
listB=['bpp','xpp','cpp','fpp']
res=[i for i in listA for j in listB if i==j]
print(res)

# 7 ans


# 8ans
list_User=[['1','2','3'],['a','b','c'],['x','y','d','p']]
res=[j for i in list_User for j in i]
print(res)

# 9ans
res=[len(word) for word in words ]
print(res)

# 10ans
res=[word[::-1]for word in words]
print(res)