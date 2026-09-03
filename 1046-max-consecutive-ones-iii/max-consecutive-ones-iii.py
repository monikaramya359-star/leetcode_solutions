class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=0
        zero=0
        maxl=0
        while r<=n-1:
            if nums[r]==0:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero<=k:
                maxl=max(maxl,r-l+1)
                r=r+1
        return maxl
        