class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        l=0
        r=k-1
        sums=0
        for i in range(l,r+1):
            sums=sums+nums[i]
            maxi=sums
        while r<n-1:
            sums=sums-nums[l]
            l=l+1
            r=r+1
            sums=sums+nums[r]
            maxi=max(maxi,sums)
        avg=maxi/k
        return avg    