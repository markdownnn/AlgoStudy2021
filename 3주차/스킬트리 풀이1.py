def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill) # list 함수로 문자열을 리스트로 만들 수 있음 
        for s in skill_tree:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else: # for/else : break가 되지 않고 끝까지 실행되었을 때
            answer += 1
    return answer