def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    N = int(input())
    print(factors(N))
    return 0

def factors(x):
    i = 1
    count = 0
    while i*i <= x:
        if i*i == x:
            count += 1
        elif x%i == 0:
            count += 2
        i += 1
    return count

if __name__ == '__main__':
    main()