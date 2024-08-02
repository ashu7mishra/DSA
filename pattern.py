def main():
    N = int(input())
    for i in range(N-1):
        if i == 0:
            print('*' * N)
        else:
            # If 1st row or 1st column or last column print star else print space
            print('*', end = '')
            print(' '* (N - i - 2), end = '')
            print('*', end = '')
            print()
    print('*')
    return 0

main()