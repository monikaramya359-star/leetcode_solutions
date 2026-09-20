class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans=0
        for row in grid:
            for num in row:
                if num<0:
                    ans+=1
        return ans