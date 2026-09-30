class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0

        for ch in seq:
            if ch == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)

        return ans