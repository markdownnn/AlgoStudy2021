def dfs(position, check, n, computers):
    for i in range(n):
        if computers[position][i] and not check[i]:
            check[i] = 1
            dfs(i, check, n, computers)

def solution(n, computers):
    check, answer = [0] * n, 0
    for i in range(n):
        if not check[i]:
            dfs(i, check, n, computers)
            answer += 1
    return answer