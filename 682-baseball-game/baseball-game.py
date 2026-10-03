class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for ch in operations:
            if ch!="C" and ch!="D" and ch!="+":
                stack.append(int(ch))
            if ch=="C":
                stack.pop()
            if ch=="D":
                stack.append(stack[-1]*2)
            if ch=="+":
                stack.append(stack[-1]+stack[-2])
        return sum(stack)