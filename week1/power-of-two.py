class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = 0 
        for i in range(n):
            if result >= n:
                return False 
            else:
                result = 2 ** i
                if result == n:
                    return True 