class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ""
        for i in range(0,len(A)):
            ans = ans + A[i]
            temp = (ord(A[i]) - ord('a') + 1)
            # Adding ascii value of A[i] in ans
            ans = ans + str(temp)
        return ans
    
obj = Solution()
print(obj.solve("azd"))