# Given a list of numbers, use list comprehension to create a new list with the squares of those numbers.
res=[i*i for i in range(1,6)]
print(res)

#Given a list of numbers, use list comprehension to create a new list with only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]
res=[i for i in numbers if i%2==0]
print(res)

# Given a list of words, use list comprehension to create a new list with the first letter of each word.
words = ["apple", "banana", "cherry", "date"]
# Output: ['a', 'b', 'c', 'd']
res=[i[0] for i in words]
print(res)

#Given a 2D matrix, use list comprehension to flatten it into a 1D list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
res=[j for i in matrix for j in i ]
print(res)

#Given a list of numbers, use list comprehension to create a new list where each number is doubled if it is even, and left unchanged if it is odd.
numbers = [1, 2, 3, 4, 5, 6]
res=[2*i if i%2==0 else i for i in numbers]
print(res)

#Given a list of strings, use list comprehension to create a new list containing only the strings that start with a vowel (a, e, i, o, u) and convert them to uppercase.
words = ["apple", "banana", "orange", "grape", "umbrella"]
# Output: ['APPLE', 'ORANGE', 'UMBRELLA']
res=[i.upper() if (i[0].lower() in 'aeiou')  else i  for i in  words]
print(res)

# You have two lists, list1 and list2. Your goal is to create a new list of tuples where each tuple consists of an element from list1 paired with its corresponding element from list2.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

res=[(list1[i], list2[i])for i in range(len(list1))]
print(res)

# Given a list of names, create a new list that contains only the names with more than 5 characters.
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "George"]
# Output: ['Charlie', 'George']
res=[name for name in names if len(name)>5]
print(res)

#Given a list of strings, some of which contain numbers embedded within them, create a new list that contains only the numbers extracted from these strings.
string_list = ["abc", "123", "def456", "789ghi", "jkl10mno"]
# Output: [123, 456, 789, 10]