def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(0,len(nums)):
            if isprime(i):
                a+=nums[i]
            else:
                b+=nums[i]
        return abs(a-b)
        