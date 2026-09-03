class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()

        if nums1[0] % 2 == 1:
            return True

        for i in range(1, len(nums1)):
            if nums1[i] % 2 == 1:
                return False

        return True