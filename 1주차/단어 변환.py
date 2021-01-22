def solution(begin, target, words):
    visited = [0] * len(words)
    
    def check(word1, word2): # 단어 체크하는 함수
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if diff:
                    return 2
                diff += 1
        return diff
    
    q = []
    for i in range(len(words)):
        if check(begin, words[i]) == 1:
            visited[i] = 1
            q.append((i, 1)) # 튜플을 저장
    
    while q:
        e = q.pop(0) // 이렇게 하면 큐처럼 쓸 수 있음
        if words[e[0]] == target:
            return e[1]
        for i in range(len(words)):
            if not visited[i]:
                if check(words[e[0]], words[i]) == 1:
                    visited[i] = 1
                    q.append((i, e[1]+1))
                
    return 0