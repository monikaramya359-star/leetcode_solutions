class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
                break
        else:
            return -1

        