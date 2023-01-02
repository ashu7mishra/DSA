class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        stack = []
        stack.append(B)
        for i in range(A):
            if C[i] != 0:
                stack.append(C[i])
            else:
                stack.pop()
        return stack.pop()
