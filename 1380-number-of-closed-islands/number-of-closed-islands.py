
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1

            a = dfs(i + 1, j)
            b = dfs(i - 1, j)
            c = dfs(i, j + 1)
            d = dfs(i, j - 1)

            return a and b and c and d

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count
