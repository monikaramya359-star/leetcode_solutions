class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        x = i + dr
                        y = j + dc

                        if 0 <= x < n and 0 <= y < n:
                            if img1[i][j] == 1 and img2[x][y] == 1:
                                count += 1

                ans = max(ans, count)

        return ans
        