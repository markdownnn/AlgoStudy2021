def solution(citations): # 깔끔하긴 하지만 시간 복잡도 O(NlgN)
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0