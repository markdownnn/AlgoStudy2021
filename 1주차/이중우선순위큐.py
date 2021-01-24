import heapq as hq

def solution(operations):
    q = []
    def make_neg(q): # 시간 복잡도 N
        for i in range(len(q)):
            q[i] = -q[i] 
    for i in range(len(operations)): # 시간 복잡도 N^2, 더 빠른 방법으로 풀어야 함
        if operations[i][0] == "I":
            q.append(int(operations[i][2:]))
        elif len(q) > 0:
            if operations[i] == "D 1":
                make_neg(q)
                hq.heapify(q)
                hq.heappop(q)
                make_neg(q)
            else:
                hq.heapify(q)
                hq.heappop(q)
    if len(q) == 0:
        return (0, 0)
    else:
        return (max(q), min(q))