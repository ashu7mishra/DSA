import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count_prime = 0
        arr = []
        if A == 1:
            return count_prime
        for i in range(2,A+1):
            if self.check_prime(i):
                count_prime += 1
                k = 1
                while i*k <= A:
                    if i*k not in arr:
                        arr.append(i*k)
                    k += 1
        return count_prime
        
    def check_prime(self, x):
        if x == 2 or x == 3:
            return True
        for i in range(2, math.ceil(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True