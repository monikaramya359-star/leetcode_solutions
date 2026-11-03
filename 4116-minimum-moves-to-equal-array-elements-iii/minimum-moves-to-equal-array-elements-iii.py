class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        l=[]
        for i in range(0,len(nums)):
            l.append(m-nums[i])
        return sum(l)