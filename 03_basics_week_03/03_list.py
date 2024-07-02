# taking input from user in list
list_user=[]
for i in range(5):
    list_user.append(int(input("Enter data")))
print(list_user)

# string comprehension
# [expression for item in iterable if condition]
print([i for i in 'radhakant'])
result=[i for i in 'sinu' ]
print(result)

r=[i for i in range(10) if i%2==0]
print(r)

rrr=[x**2 for x in range(10)]
print(rrr)

rem=[r%2 for r in range(1,11)]
print(rem)

odd_or_even=['Even' if x%2==0 else 'Odd' for x in range(1,10) ]
print(odd_or_even)

# nested list
temp_list=[]
for i in range(3):
    temp_list.append([])
    for j in range(3):
        temp_list[i].append(j)

print(temp_list)

# using list comprehension
print([[j for j in range(3) ]for i in range(3)])

# nested if 
print([i for i in range(10) if i%2==0 if i%3==0])

print(["Yes" if i==1 else '2' if i==2 else "Bruh" for i in range(10)])

    