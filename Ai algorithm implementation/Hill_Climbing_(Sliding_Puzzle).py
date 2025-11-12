class Puzzle:
    def __init__(self, board):
        self.board = [row[:] for row in board]
        self.h = 0
        goal = [[1,2,3],[4,5,6],[7,8,0]]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0 and self.board[i][j] != goal[i][j]:
                    self.h += 1

def get_neighbors(p):
    neighbors = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    x, y = 0, 0
    for i in range(3):
        for j in range(3):
            if p.board[i][j] == 0:
                x, y = i, j
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in p.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(Puzzle(new_board))
    
    return neighbors

def hill_climbing(start):
    while True:
        neighbors = get_neighbors(start)
        best = start
        for n in neighbors:
            if n.h < best.h:
                best = n
        if best.h >= start.h:
            break
        start = best
    return start

def print_board(p):
    for row in p.board:
        print(' '.join(map(str, row)))

start_board = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

start = Puzzle(start_board)
solution = hill_climbing(start)

print(f"Final heuristic: {solution.h}")
print_board(solution)
