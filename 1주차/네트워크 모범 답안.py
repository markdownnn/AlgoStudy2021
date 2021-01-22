def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)] # 이렇게도 초기화 가능
    def dfs(computers, visited, start): # 함수에서 함수 선언 가능
        stack = [start]
        while stack:
            j = stack.pop() # 리스트를 스택처럼 사용
            if visited[j] == 0: # 이건 필요 없습니다.
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited: # in을 이용해서 조건 체크
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer