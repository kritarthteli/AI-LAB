import heapq

class PuzzleNode:
    def __init__(self, board, parent=None, move="", g=0, h=0):
        self.board = board       # 1D tuple of length 9 representing the 3x3 grid (0 is empty)
        self.parent = parent     # Pointer to parent node
        self.move = move         # The direction moved to reach this state
        self.g = g               # Path cost from start to current node
        self.h = h               # Heuristic cost from current node to goal
        self.f = g + h           # Total estimated cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def get_manhattan_distance(board, goal):
    distance = 0
    for i in range(9):
        tile = board[i]
        if tile != 0:  # Skip the empty tile
            current_row, current_col = divmod(i, 3)
            goal_index = goal.index(tile)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(node, goal):
    neighbors = []
    zero_index = node.board.index(0)
    row, col = divmod(zero_index, 3)
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    for dr, dc, move_name in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            new_board = list(node.board)
            new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
            new_board_tuple = tuple(new_board)
            g_score = node.g + 1
            h_score = get_manhattan_distance(new_board_tuple, goal)

            neighbors.append(PuzzleNode(new_board_tuple, node, move_name, g_score, h_score))

    return neighbors

def solve_8_puzzle(start_board, goal_board):
    start_tuple = tuple(start_board)
    goal_tuple = tuple(goal_board)
    initial_h = get_manhattan_distance(start_tuple, goal_tuple)
    root = PuzzleNode(start_tuple, None, "", 0, initial_h)
    open_list = []
    heapq.heappush(open_list, root)
    visited = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.board == goal_tuple:
            path = []
            moves = []
            total_cost = current_node.g
            while current_node:
                path.append(current_node.board)
                if current_node.move:
                    moves.append(current_node.move)
                current_node = current_node.parent
            return path[::-1], moves[::-1], len(visited), total_cost

        visited.add(current_node.board)
        for neighbor in get_neighbors(current_node, goal_tuple):
            if neighbor.board in visited:
                continue
            heapq.heappush(open_list, neighbor)

    return None, None, len(visited), None

def print_grid(board):
    for i in range(0, 9, 3):
        print(f"[ {board[i]} {board[i+1]} {board[i+2]} ]")
    print()

def get_user_input(prompt):
    print(prompt)
    user_in = input("Enter 9 numbers separated by space (0 for empty space): ")
    return [int(x) for x in user_in.strip().split()]

if __name__ == "__main__":
    try:
        initial_state = get_user_input("--- Enter Initial State ---")
        goal_state = get_user_input("--- Enter Goal State ---")
        
        if len(initial_state) != 9 or len(goal_state) != 9:
            raise ValueError("Both states must contain exactly 9 elements.")

        states_path, moves_sequence, states_visited, total_cost = solve_8_puzzle(initial_state, goal_state)

        print("\n--- OUTPUT ---")
        print("Initial State:")
        print_grid(initial_state)

        print("Final State:")
        print_grid(goal_state)

        if total_cost is not None:
            print(f"Number of states visited: {states_visited}")
            print(f"Total Cost: {total_cost}")
        else:
            print(f"No solution found. Number of states visited: {states_visited}")
    except Exception as e:
        print(f"Error processing inputs: {e}. Please run again and make sure to input 9 space-separated integers.")
