class Solution:
    def reverse(self, x: int) -> int:
        y=abs(x)
        z=str(y)
        r=int(z[::-1])
        if r>2**31-1:
            return 0
        if x<0:
            return -1*r
        else:
            return r
            