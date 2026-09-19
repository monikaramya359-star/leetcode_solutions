class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        m=len(nums)//2
        if len(nums)%2!=0:
            return nums[m]
        else:
            return (nums[m]+nums[m-1])/2        