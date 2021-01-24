import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville) # 시간 복잡도 O(N) 이것도 가능함
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer