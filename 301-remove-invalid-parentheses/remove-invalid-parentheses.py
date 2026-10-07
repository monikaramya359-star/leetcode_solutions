class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0
        right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()
        n = len(s)

        def dfs(i, left, right, open_count, close_count, current):
            if i == n:
                if left == 0 and right == 0:
                    ans.add(current)
                return

            if n - i < left + right:
                return

            if open_count < close_count:
                return

            ch = s[i]

            if ch == '(' and left > 0:
                dfs(i + 1, left - 1, right,
                    open_count, close_count, current)

            elif ch == ')' and right > 0:
                dfs(i + 1, left, right - 1,
                    open_count, close_count, current)

            if ch == '(':
                dfs(i + 1, left, right,
                    open_count + 1, close_count,
                    current + ch)

            elif ch == ')':
                if open_count > close_count:
                    dfs(i + 1, left, right,
                        open_count, close_count + 1,
                        current + ch)

            else:
                dfs(i + 1, left, right,
                    open_count, close_count,
                    current + ch)

        dfs(0, left, right, 0, 0, "")

        return list(ans)