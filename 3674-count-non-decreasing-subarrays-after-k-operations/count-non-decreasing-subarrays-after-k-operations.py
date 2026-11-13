from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        cost = 0
        ans = 0
        j = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            count = 1

            while dq and dq[-1][0] < nums[i]:
                val, cnt = dq.pop()
                count += cnt
                cost += (nums[i] - val) * cnt

            dq.append((nums[i], count))

            while cost > k:
                val, cnt = dq.popleft()
                cost -= val - nums[j]
                j -= 1

                if cnt > 1:
                    dq.appendleft((val, cnt - 1))

            ans += j - i + 1

        return ans