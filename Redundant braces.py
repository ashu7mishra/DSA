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