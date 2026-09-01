from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total_litter = len(litter)
        if total_litter == 0:
            return 0

        target = (1 << total_litter) - 1
        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask
                    if (nr, nc) in litter:
                        idx = litter[(nr, nc)]
                        nmask |= (1 << idx)

                    
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1