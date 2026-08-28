class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if nums[l]==nums[mid]:
                l=l+1
                continue
            if nums[l]<nums[mid]:
                if target>=nums[l] and target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target>=nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False


