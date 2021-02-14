import sys
from itertools import combinations

N, K = list(map(int, sys.stdin.readline().split()))

words = []

for i in range(N):
    words.append(set(sys.stdin.readline().replace('a', '').replace('c', '').replace('i','').replace('n','').replace('t','').rstrip()))

if K <= 4:
    print(0)
else:
    letters = []
    for i in range(len(words)):
        for j in range(len(list(words[i]))):
            letters.extend(list(words[i])[j])
            
    choice = K - 5
    if choice >= len(set(letters)):
        choice = len(set(letters))

    comb = list(combinations(list(set(letters)), choice))

    answer = 0

    for s in comb:
        s = set(s)
        result = 0
        for i in range(len(words)):
            if words[i].issubset(s):
                result += 1
        answer = max(answer, result)

    print(answer)

