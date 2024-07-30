def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    T = int(input())
    for i in range(T):
        N = int(input())
        new = reverse(N)
        print(N%10,new%10)

    return 0

def reverse(x):
    new = 0
    while x:
        new = new*10
        new = new + (x%10)
        x = x//10
    return new

if __name__ == '__main__':
    main()