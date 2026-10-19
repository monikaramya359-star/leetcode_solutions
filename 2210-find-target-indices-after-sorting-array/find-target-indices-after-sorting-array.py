class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        l=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
        