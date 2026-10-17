class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
        pos = {num: i for i, num in enumerate(arr)}
        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i]:
                continue

            j = i
            count = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                count += 1

            ans += max(0, count - 1)

        return ans