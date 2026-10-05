import random

def calculate_heuristic(state):
    """Calculates the number of mutually attacking pairs of queens.
    In this representation, index is column and value is row.
    """
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row (values are equal) or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(state):
    """Generates all neighbors by moving each queen within her column, and returns the best neighbor."""
    n = len(state)
    current_h = calculate_heuristic(state)
    best_neighbor = list(state)
    best_h = current_h

    # Generate all possible board variations (neighbors)
    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            # Create neighbor state
            neighbor = list(state)
            neighbor[col] = row
            neighbor_h = calculate_heuristic(neighbor)

            # If this neighbor has a better heuristic, keep it
            if neighbor_h < best_h:
                best_h = neighbor_h
                best_neighbor = neighbor

    return best_neighbor, best_h

def hill_climbing_4_queens(initial_state):
    """Solves 4-Queens using Hill Climbing search where state index is column and value is row."""
    current_state = list(initial_state)
    current_h = calculate_heuristic(current_state)
    
    print(f"Initial state: {current_state} | Heuristic (Conflicts): {current_h}")
    
    step = 0
    while True:
        neighbor, neighbor_h = get_best_neighbor(current_state)
        
        # If no neighbor is better, we have reached a local or global optimum
        if neighbor_h >= current_h:
            break
            
        current_state = neighbor
        current_h = neighbor_h
        step += 1
        print(f"Step {step}: Move to state {current_state} | Heuristic (Conflicts): {current_h}")
    
    return current_state, current_h

def print_board(state):
    """Prints the 4x4 chessboard layout.
    state[col] = row indicates the row position of the queen in that column.
    """
    # Create an empty 4x4 grid
    grid = [[" . "] * 4 for _ in range(4)]
    for col in range(4):
        row = state[col]
        grid[row][col] = " Q "
    
    for r in range(4):
        print("".join(grid[r]))
    print()

# --- Main Execution ---
if __name__ == "__main__":
    try:
        print("--- 4-Queens Hill Climbing Search (Column-based Input) ---")
        user_input = input("Enter initial state as 4 space-separated row indexes (0-3) for each column (0-3): ")
        initial_state = [int(x) for x in user_input.strip().split()]
        
        if len(initial_state) != 4 or any(x < 0 or x > 3 for x in initial_state):
            raise ValueError("State must contain exactly 4 integers, each between 0 and 3.")
        
        print("\nInitial Chessboard:")
        print_board(initial_state)
        
        final_state, final_h = hill_climbing_4_queens(initial_state)
        
        print("\nFinal State reached:")
        print_board(final_state)
        
        if final_h == 0:
            print("Success! A solution with 0 conflicts was found.")
        else:
            print(f"Stuck at a local maximum or flat local minimum with {final_h} conflicts.")
            
    except Exception as e:
        print(f"Input Error: {e}. Please run the cell again with valid row indexes (0-3).")
