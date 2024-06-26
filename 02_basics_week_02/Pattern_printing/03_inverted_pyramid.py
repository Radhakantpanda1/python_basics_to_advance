def print_pattern(n):
    for i in range (0,n+1):
        for j in range(0,i):
            print(" ",end='')
        for k in range(0,n+1-i):
            print('* ',end='')
        print('\r')
print_pattern(2)