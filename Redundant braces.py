# Problem Description
# Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
#
# Check whether A has redundant braces or not.
#
# NOTE: A will be always a valid expression and will not contain any white spaces.
#
#
#
# Problem Constraints
# 1 <= |A| <= 105
#
#
#
# Input Format
# The only argument given is string A.
#
#
#
# Output Format
# Return 1 if A has redundant braces else, return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = "((a+b))"
# Input 2:
#
#  A = "(a+(a+b))"
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
#  ((a+b)) has redundant braces so answer will be 1.
# Explanation 2:
#
#  (a+(a+b)) doesn't have have any redundant braces so answer will be 0.


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in A:
            if i == '(' or i == '+' or i == '-' or i == '*' or i == '/':
                stack.append(i)
            elif i == ')':
                x = stack.pop()
                if x == '(':
                    return 1
                else:
                    while(len(stack)>0 and x != '('):
                        x = stack.pop()
        if len(stack) == 0:
            return 0
        else:
            while len(stack) != 0:
                x = stack.pop()
                if x == '(' or x == ')':
                    return 1
            return 0