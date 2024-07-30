def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    T = int(input())
    for i in range(T):
        N = int(input())
        # print(factors(N)-N)
        print("YES" if N == factors(N)-N else "NO")
    return 0

def factors(x):
    i = 1
    sum = 0
    while i*i <= x:
        if i*i == x:
            sum += i
        elif x%i == 0:
            sum += i
            sum += (x//i)
        i += 1
    return sum

if __name__ == '__main__':
    main()