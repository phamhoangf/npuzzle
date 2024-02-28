class PuzzleNode:
    def __init__(self, board) -> None:
        self.board = board
        self.g = 0
        self.h = 0

def hamming_distance(state, goal):
    #Tổng số ô bị lệch khỏi vị trí chính xác
    n = len(state)
    distance = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                distance += 1
    return distance

def generate_children(node):
    #Tạo các node mới khi tráo vị trí ô trống với các ô cạnh nó
    puzzleNodes = []
    n = len(node.board)
    for i in range(n):
        for j in range(n):
            if node.board[i][j] == 0:
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        child_board = [row[:] for row in node.board]
                        child_board[i][j], child_board[ni][nj] = child_board[ni][nj], child_board[i][j]
                        puzzleNodes.append(PuzzleNode(child_board))
    return puzzleNodes

def a_star(initial_board, goal_board):
    #tập hợp các node chưa xét
    openSet = [PuzzleNode(initial_board)]
    #các node đã kiểm tra
    closedSet = set()

    while openSet:
        currentNode = min(openSet, key = lambda x : x.h + x.g)
        openSet.remove(currentNode)
        closedSet.add(tuple(map(tuple, currentNode.board)))

        if currentNode.board == goal_board:
            return currentNode.g
        
        for child in generate_children(currentNode):
            if tuple(map(tuple, child.board)) not in closedSet:
                child.g = currentNode.g + 1
                child.h = hamming_distance(child.board, goal_board)
                openSet.append(child)
    
    return -1

if __name__ == "__main__":
    n = int(input("Nhập kích thước ô số (n < 10): "))
    initial_state = []
    print(f"Nhập ma trận {n}x{n}:")
    for _ in range(n):
        row = list(map(int, input().split()))
        initial_state.append(row)

    goal_state = [[i * n + j for j in range(n)] for i in range(n)]

    print(a_star(initial_state, goal_state))
    