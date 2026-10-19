class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected=sorted(heights)
        c=0
        for i in range(0,len(heights)):
            if expected[i]!=heights[i]:
                c=c+1
        return c
