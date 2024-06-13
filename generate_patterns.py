def get_neighbors(x, y, n, m):
    # Get all 8 possible moves from (x, y)
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            neighbors.append((nx, ny))
    return neighbors

def dfs(x, y, n, m, k, current_length, path, patterns, visited):
    if current_length == k:
        patterns.append(path[:])
        return

    for nx, ny in get_neighbors(x, y, n, m):
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            path.append((nx, ny))
            dfs(nx, ny, n, m, k, current_length + 1, path, patterns, visited)
            path.pop()
            visited.remove((nx, ny))

def generate_patterns(grid_size, k):
    n, m = grid_size
    all_patterns = []
    for j in range(m-1, -1, -1):
        for i in range(n):
            visited = set()
            visited.add((i, j))
            dfs(i, j, n, m, k, 1, [(i, j)], all_patterns, visited)
    return all_patterns


print("Helper Functions For Generating Patterns Loaded Successfully!")