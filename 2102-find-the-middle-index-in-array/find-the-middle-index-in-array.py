class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        index=0
        for i in range(len(nums)):
            index=i
            f=nums[:index]
            l=nums[index+1:]
            if sum(f)==sum(l):
                return i
                break
        else:
            return -1
            
