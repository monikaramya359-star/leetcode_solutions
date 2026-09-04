class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maxi=nums[0]
        for i in range(n):
            maxi=max(maxi,nums[i])
            mini=min(nums[i:])
            if maxi-mini<=k:
                return i
        return -1

        