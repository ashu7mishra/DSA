def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    x = input().split()
    A = int(x[0])
    B = int(x[1])
    hcf = lcm(A, B)
    print("HCF - ",hcf)

    print((A*B)//hcf)

def lcm(A, B):
    A, B = max(A, B), min(A, B)
    # B = min(A, B)
    # print(A, B)

    if A%B == 0:
        return B
    return lcm(A%B, B)

    return 0

if __name__ == '__main__':
    main()