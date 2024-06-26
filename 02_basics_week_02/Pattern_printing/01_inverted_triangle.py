height_of_triangle=int(input("Enter the height"))
for i in range (0,height_of_triangle):
    for j in range (0,i):
        print(" ",end='')
    for k in range(0,height_of_triangle-i):
        print("* ",end='')
    print('\r')
        