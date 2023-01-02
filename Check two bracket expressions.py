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
