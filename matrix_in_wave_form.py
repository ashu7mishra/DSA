# import copy
# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     n = int(input())
#     arr = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         x = input().split()
#         for j in range(n):
#             arr[i][j] = copy.copy(x[j])

#     j = 0
#     i = 0
#     while i < n:
#         if i == n:
#             break
#         while j<n:
#             print(arr[j][i], end=' ')
#             j += 1
#         i += 1
#         if i == n:
#             break
#         while j > 0:
#             j -= 1
#             print(arr[j][i], end=' ')
#         i += 1
#     return 0

# if __name__ == '__main__':
#     main()

def main():
    # DO NOT CHANGE THE CODE BELOW.
    global ii
    n = inp[ii: ii + 1][0]
    ii += 1
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = inp[ii: ii + 1][0]
            ii += 1
    # DO NOT CHANGE THE CODE ABOVE
    
    # YOUR CODE GOES BELOW HERE.
    # USE THE GIVEN MATRIX mat FOR ALL THE OPERATIONS.
    for i in range(n):
        x = input().split()
        for j in range(n):
            mat[i][j] = copy.copy(x[j])
    
    j = 0
    i = 0
    while i < n:
        if i == n:
            break
        while j<n:
            print(arr[i][j], end=' ')
            j += 1
        i += 1
        if i == n:
            break
        while j > 0:
            j -= 1
            print(arr[i][j], end=' ')
        i += 1
    return 0
    
    return 0

if __name__ == '__main__':
    main()