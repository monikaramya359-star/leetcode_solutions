class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        qelvarodin = nums[:]

        pref_max = [0] * (n + 1)
        suff_min = [float('inf')] * (n + 1)
        pref_drop = [0] * n

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (nums[i - 1] > nums[i])

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                drops = pref_drop[end] - pref_drop[start]

                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1 or pref_max[start] > suff_min[start]:
                    return False

            return True

        ans = 0

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if check(i):
                    ans += i

                other = n // i

                if other != i and check(other):
                    ans += other

        return ans