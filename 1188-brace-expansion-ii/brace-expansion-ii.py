class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        ans = set()

        def dfs(s):
            close = s.find('}')

            if close == -1:
                ans.add(s)
                return

            open = s.rfind('{', 0, close)

            before = s[:open]
            inside = s[open + 1:close]
            after = s[close + 1:]

            for word in inside.split(','):
                dfs(before + word + after)

        dfs(expression)

        return sorted(ans)