class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()

        def _mark_as_safe(i, j):
            board[i][j] = 'S'
            q.append((i, j))

        # mark all the safe O's to initialize the queue for the BFS
        for c in range(len(board[0])):
            if board[len(board) - 1][c] == 'O':
                _mark_as_safe(len(board) - 1, c)
            if board[0][c] == 'O':
                _mark_as_safe(0, c)

        for r in range(len(board)):
            if board[r][0] == 'O':
                _mark_as_safe(r, 0)
            if board[r][len(board[r]) - 1] == 'O':
                _mark_as_safe(r, len(board[r]) - 1)

        # mark all nodes reachable from the safe O's as safe since they are connected
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr = r + dr
                    nc = c + dc
                    if nr not in range(len(board)) or nc not in range(len(board[nr])):
                        continue
                    if board[nr][nc] != 'O':
                        continue
                    board[nr][nc] = 'S'
                    q.append((nr, nc))
        
        # flip safe O's to original O, and flip all unsafe O's to X's
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'