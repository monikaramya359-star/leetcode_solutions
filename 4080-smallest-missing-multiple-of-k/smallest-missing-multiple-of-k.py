class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)+2):
            if k*i not in nums:
                return k*i