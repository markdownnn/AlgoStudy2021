import sys

N, M = map(int, sys.stdin.readline().split())

# strip 함수 알아두기, 특정 문자열에서 제거할 때 쓰임
info = [(sys.stdin.readline().rstrip(), i) for i in range(N)]
quest = [sys.stdin.readline().rstrip() for _ in range(M)]

info_dict = dict(info) # 튜플, 리스트 형태의 자료를 딕셔너리로 변환이 가능

for i in range(M):
    if quest[i].isdigit():
        print(info[int(quest[i])-1][0])
    else:
        print(info_dict[quest[i]]+1) # O(1)
