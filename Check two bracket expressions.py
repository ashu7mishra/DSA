# Problem Description
# Given two strings A and B. Each string represents an expression consisting of lowercase English alphabets, '+', '-', '(' and ')'.
#
# The task is to compare them and check if they are similar. If they are identical, return 1 else, return 0.
#
# NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’, and every operand appears only once.
#
# Problem Constraints
# 1 <= length of the each String <= 100

# Input Format
# The given arguments are string A and string B.
#
#
#
# Output Format
# Return 1 if they represent the same expression else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = "-(a+b+c)"
#  B = "-a-b-c"
# Input 2:
#
#  A = "a-b-(c-d)"
#  B = "a-b-c-d"
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B.
# Explanation 2:
#
#  Both the expression are different.
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        lenA = len(A)
        lenB = len(B)
        GlobalA = [True]
        GlobalB = [True]
        signA = [True]*26
        signB = [True]*26
        self.parse(A,lenA,GlobalA,signA)
        self.parse(B,lenB,GlobalB,signB)
        #print(signA)
        #print(signB)
        for i in range(26):
            if signA[i] != signB[i]:
                return 0
        return 1

    def parse(self,string,n,global_sign,sign):
        for i in range(n):
            if string[i] == '+' or string[i] == '-':
                continue
            elif string[i] == '(':
                if string[i-1] == '-':
                    global_sign.append(False == global_sign[-1])
                else:
                    global_sign.append(True == global_sign[-1])
                #print(global_sign)
            elif string[i] == ')':
                global_sign.pop()
            else:
                local_sign = True
                if i>0:
                    if string[i-1] == '-':
                        local_sign = False
                index = ord(string[i]) - ord('a')
                #print(index)
                sign[index] = global_sign[-1] == local_sign

obj = Solution()
A = "-(-(-(-a+b)-d+c)-q)"
B = "a-b-d+c+q"
print(obj.solve(A,B))
