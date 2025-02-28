def find_combinations(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []

    def dfs(i, j, current_sum, path, visited):
        if current_sum == 10:
            result.append(path.copy())
            return
        if current_sum > 10 or len(path) >= 4:
            return
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                # 总和不超过10
                new_sum = current_sum + matrix[x][y]
                if new_sum > 10:
                    continue
                visited[x][y] = True
                new_path = path + [(x, y)]
                dfs(x, y, new_sum, new_path, visited)
                # 重复使用当前数字
                # visited[x][y] = False

    for i in range(rows):
        for j in range(cols):
            # 如果已经使用，跳过
            if visited[i][j]:
                continue
            visited[i][j] = True
            dfs(i, j, matrix[i][j], [(i, j)], visited)
            # 重复使用当前数字
            # visited[i][j] = False

    return result


matrix = [
    [1, 6, 4, 1, 3, 3, 1, 1, 1, 1, 1, 1, 4],
    [3, 3, 3, 1, 3, 6, 1, 7, 2, 7, 2, 5, 4],
    [1, 6, 3, 8, 2, 3, 8, 1, 2, 1, 2, 1, 4],
    [1, 2, 1, 2, 2, 5, 1, 3, 3, 5, 3, 7, 2],
    [1, 7, 6, 3, 5, 2, 1, 2, 1, 3, 2, 1, 6],
    [2, 3, 3, 5, 5, 2, 1, 8, 1, 2, 7, 2, 1],
    [1, 1, 3, 1, 3, 3, 1, 2, 1, 4, 2, 1, 1],
    [3, 6, 2, 2, 1, 6, 7, 2, 1, 5, 2, 1, 6],
    [5, 2, 2, 6, 1, 1, 1, 2, 2, 5, 1, 5, 1],
    [3, 4, 2, 1, 3, 5, 4, 4, 2, 3, 2, 4, 5]
]
matrix2 = [
    [3, 1, 3, 1, 1, 6, 8, 2, 6, 1, 2, 7, 2],
    [5, 1, 1, 4, 2, 2, 1, 1, 2, 7, 5, 2, 1],
    [4, 3, 6, 5, 7, 2, 3, 5, 2, 5, 4, 2, 1],
    [1, 2, 6, 2, 3, 1, 2, 1, 6, 1, 6, 2, 2],
    [1, 1, 2, 5, 5, 4, 2, 3, 4, 3, 1, 4, 4],
    [6, 2, 2, 2, 1, 6, 1, 2, 1, 2, 4, 1, 1],
    [2, 2, 2, 1, 1, 3, 5, 1, 6, 2, 1, 3, 5],
    [2, 4, 2, 6, 6, 1, 1, 5, 1, 2, 2, 5, 1],
    [3, 3, 4, 2, 6, 1, 4, 1, 6, 1, 7, 1, 4],
    [6, 4, 6, 1, 2, 1, 5, 3, 1, 6, 3, 1, 5]
]
combinations = find_combinations(matrix2)
print("找到的组合：")
for combo in combinations:
    print(combo)
