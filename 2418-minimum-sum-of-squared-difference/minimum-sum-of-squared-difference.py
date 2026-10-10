class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(0, x - mid) for x in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        ans = 0
        remaining = k

        for x in diff:
            reduce = max(0, x - left)
            ans += (x - reduce) ** 2
            remaining -= reduce

        ans -= remaining * (2 * left - 1)

        return ans