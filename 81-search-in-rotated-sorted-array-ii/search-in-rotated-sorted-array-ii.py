class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(0,len(nums)):
            if nums[i]==target:
                return True
                break
        else:
            return False



