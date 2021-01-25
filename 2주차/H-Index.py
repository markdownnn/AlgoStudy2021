def solution(citations): # 기수 정렬 이용, 시간 복잡도 O(N)
    arr = [0] * 10001
    for i in range(len(citations)):
        arr[citations[i]] += 1
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    
    for i in range(len(citations)):
        h = len(citations) - i
        if arr[h-1] <= h and arr[-1]-arr[h-1] >= h:
            return h
    return 0