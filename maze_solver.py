"""
Project 1: Maze Solver using A* Search
Syntecxhub AI Internship - Week 1 Task

- Maze/grid ko nodes ki tarah model kiya gaya hai
- A* search with Manhattan distance heuristic
- Shortest path return karta hai
- Agar goal tak rasta na ho to "No path found" batata hai
- Console par search aur final path dono dikhata hai
"""

import heapq


# Maze: '#' = wall, '.' = open path, 'S' = start, 'G' = goal
MAZE = [
    "##########",
    "#S...#...#",
    "#.##.#.#.#",
    "#.#..#.#.#",
    "#.#.##.#.#",
    "#.......G#",
    "##########",
]


def manhattan(a, b):
    """Manhattan distance heuristic: |x1-x2| + |y1-y2|"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_points(grid):
    """Start (S) aur Goal (G) ki position dhoondo."""
    start = goal = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "G":
                goal = (r, c)
    return start, goal


def neighbours(pos, grid):
    """Ek cell ke 4 neighbours (up, down, left, right) jo wall na hon."""
    rows, cols = len(grid), len(grid[0])
    r, c = pos
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            yield (nr, nc)


def a_star(grid, start, goal):
    """
    A* search.
    Returns: (path list, explored set) ya (None, explored) agar rasta na mile.
    """
    open_list = []  # heap of (f_score, counter, node)
    counter = 0
    heapq.heappush(open_list, (manhattan(start, goal), counter, start))

    came_from = {}          # node -> previous node (path banane ke liye)
    g_score = {start: 0}    # start se is node tak ki cost
    explored = set()

    while open_list:
        _, _, current = heapq.heappop(open_list)
        if current in explored:
            continue
        explored.add(current)

        if current == goal:
            # Path wapas banao: goal se start tak
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, explored

        for nb in neighbours(current, grid):
            new_g = g_score[current] + 1
            if nb not in g_score or new_g < g_score[nb]:
                g_score[nb] = new_g
                f_score = new_g + manhattan(nb, goal)
                came_from[nb] = current
                counter += 1
                heapq.heappush(open_list, (f_score, counter, nb))

    return None, explored  # goal tak koi rasta nahi


def show(grid, path=None, explored=None):
    """Maze print karo: '*' = final path, 'o' = explored cells."""
    path_set = set(path) if path else set()
    explored_set = set(explored) if explored else set()
    for r, row in enumerate(grid):
        line = ""
        for c, ch in enumerate(row):
            if (r, c) in path_set and ch not in ("S", "G"):
                line += "*"
            elif (r, c) in explored_set and ch not in ("S", "G"):
                line += "o"
            else:
                line += ch
        print(line)


def main():
    print("=== Maze Solver using A* Search ===\n")
    print("Original Maze:")
    show(MAZE)

    start, goal = find_points(MAZE)
    path, explored = a_star(MAZE, start, goal)

    print("\n--- Result ---")
    if path is None:
        print("No path found! Goal tak pahunchna mumkin nahi (unreachable).")
        print(f"Explored cells: {len(explored)}")
    else:
        print(f"Shortest path mil gaya! Length: {len(path) - 1} steps")
        print(f"Explored cells: {len(explored)}")
        print("\nSolved Maze ('*' = path, 'o' = explored):")
        show(MAZE, path, explored)


if __name__ == "__main__":
    main()
