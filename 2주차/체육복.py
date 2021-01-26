def solution(n, lost, reserve): # 시간 복잡도 O(N)
    clothes, answer = [0] * n, 0
    for i in range(len(lost)):
        clothes[lost[i]-1] -= 1
    for i in range(len(reserve)):
        clothes[reserve[i]-1] += 1
    
    for i in range(n):
        if clothes[i] == -1:
            if i >= 1 and clothes[i-1] == 1:
                clothes[i] = 0
                clothes[i-1] = 0
            elif i <= n - 2 and clothes[i+1] == 1:
                clothes[i] = 0
                clothes[i+1] = 0
    
    for i in range(n):
        if clothes[i] >= 0:
            answer += 1
    
    return answer