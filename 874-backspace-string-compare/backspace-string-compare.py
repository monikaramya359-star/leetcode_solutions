class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for ch in s:
            if ch!="#":
                stack1.append(ch)
            elif stack1:
                stack1.pop()
        for ch in t:
            if ch!="#":
                stack2.append(ch)
            elif stack2:
                stack2.pop()
        return stack1==stack2