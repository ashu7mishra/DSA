
import copy
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = input().split()
    n = int(a[0])
    m = int(a[1])
    mat = [[0]*m]*n
    for i in range(n):
        x = copy.deepcopy(input().split())
        for j in range(m):
            print(int(x[j]), end=' ')
        print()

    return 0


if __name__ == '__main__':
    main()