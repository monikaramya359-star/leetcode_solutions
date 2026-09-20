class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False;
        return (n & (n - 1)) == 0
'''
    The main condition n & (n - 1)) == 0 works because every power of 2 has only one 1 in its binary form. For example, 8 is 1000 in binary, and 7 is 0111. When we perform 1000 & 0111, the result is 0000. Therefore, if n & (n - 1) gives 0, only if the number is power of 2. For a number like 10 (1010), 9 is 1001, and 1010 & 1001 = 1000, which is not zero, so 10 is not a power of 2.
'''
    