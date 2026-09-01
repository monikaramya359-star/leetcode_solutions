from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)

        if total == 0:
            return 0

        full_mask = (1 << total) - 1

        best = [[[-1 for _ in range(1 << total)]
                 for _ in range(n)] for _ in range(m)]

        sr, sc = start

        best[sr][sc][0] = energy

        q = deque()
        q.append((sr, sc, 0, energy, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    index = litter[(nr, nc)]
                    new_mask |= (1 << index)

                if classroom[nr][nc] == 'R':
                    ne = energy

                if new_mask == full_mask:
                    return moves + 1

                if ne > best[nr][nc][new_mask]:
                    best[nr][nc][new_mask] = ne
                    q.append((nr, nc, new_mask, ne, moves + 1))

        return -1
        