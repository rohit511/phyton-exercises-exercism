def spiral_matrix(size):
    spiral = []
    for r in range(size):
        spiral.append(size * [0])
    y = x = 0
    dx, dy = 1, 0
    for i in range(size**2):
        spiral[y][x] = i + 1
        x1, y1 = x + dx, y + dy
        if x1 < 0 or x1 >= size or y1 < 0 or y1 >= size or spiral[y1][x1] != 0:
            dx, dy = -dy, dx
            x1, y1 = x + dx, y + dy
        x, y = x1, y1
    return spiral