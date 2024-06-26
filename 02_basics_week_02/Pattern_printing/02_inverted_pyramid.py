def print_pattern(n):
    for i in range (0,n):
        for j in range(0,i):
            print(" ",end='');
        for k in range (0,2*n-1-2*i):
            print('*',end='')
        print('\r')
def main():
    n=int(input('Enter the height-'))
    print_pattern(n)

main()