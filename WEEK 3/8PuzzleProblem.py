MOVES = [
    (-1, 0),   # Up
    (1, 0),    # Down
    (0, -1),   # Left
    (0, 1)     # Right
]


def get_neighbors(state):
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    neighbors = []
    
    for dr, dc in MOVES:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors


def dfs(start, goal):
    stack = [start]
    visited = set()
    count = 0

    while stack:
        state = stack.pop()
        if state in visited:
            continue
        
        if state == goal:
            return count
        visited.add(state)
        count += 1
        
        for next_state in get_neighbors(state):
            if next_state not in visited:
                stack.append(next_state)
    return count


def depth_limited_search(state, goal, depth, path, counter):
    counter[0] += 1

    if state == goal:
        return True

    if depth == 0:
        return False

    for next_state in get_neighbors(state):
        if next_state not in path:
            path.add(next_state)
            found = depth_limited_search(
                next_state,
                goal,
                depth - 1,
                path,
                counter
            )
            if found:
                return True
            path.remove(next_state)
    return False


def ids(start, goal, max_depth):
    total_states = 0
    
    for depth in range(0, max_depth + 1):
        path = {start}
        counter = [0]
        found = depth_limited_search(
            start,
            goal,
            depth,
            path,
            counter
        )
        total_states += counter[0]
        print(
            "Depth", depth,
            "-> States visited:", counter[0]
        )
        if found:
            return total_states, depth
    return total_states, -1


print("Enter Initial State:")
start = tuple(map(int, input().split()))

print("Enter Goal State:")
goal = tuple(map(int, input().split()))

print("Enter Maximum Depth for IDS:")
max_depth = int(input())

print("\n======================================")
print("              8 PUZZLE")
print("======================================")

print("\nInitial State:")

for i in range(0, 9, 3):
    print(start[i:i + 3])

print("\nGoal State:")

for i in range(0, 9, 3):
    print(goal[i:i + 3])

dfs_states = dfs(start, goal)

ids_states, ids_depth = ids(
    start,
    goal,
    max_depth
)

print("\n======================================")
print("                RESULT")
print("======================================")

print("DFS - Number of states visited:", dfs_states)

if ids_depth != -1:
    print("IDS - Number of states visited:", ids_states)
    print("IDS - Goal found at depth:", ids_depth)
else:
    print("IDS - Goal not found within maximum depth")
    print("IDS - Number of states visited:", ids_states)
