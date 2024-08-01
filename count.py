T = int(input())

for i in range(T):
    A = input().split()
    odd = 0
    even = 0
    for j in A:
        if int(j)%2:
            odd += 1
        else:
            even += 1
    print(even-odd if even > odd else odd-even)

