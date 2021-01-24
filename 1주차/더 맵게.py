import heapq

def solution(scoville, K):
    answer = 0
    q = [] # 빈 리스트를 힙으로 사용
    
    for i in range(len(scoville)):
        heapq.heappush(q, scoville[i]) # 시간 복잡도 O(N), 인자를 (우선 순위, 값) 튜플로 넘겨줄 수 있음
    
    while True:
        food = heapq.heappop(q)
        if food >= K:
            return answer
        elif len(q) == 0:
            return -1
        else:
            food += heapq.heappop(q) * 2
            heapq.heappush(q, food)
            answer += 1