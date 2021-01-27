def solution(triangle):
    h = len(triangle) - 1
    while h:
        for i in range(h):
            triangle[h-1][i] += max(triangle[h][i], triangle[h][i+1])
        h -= 1
    return triangle[0][0]