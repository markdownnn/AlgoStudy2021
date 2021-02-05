def is_ok(skill, skill_tree):
    idx = 0
    for i in range(len(skill_tree)):
        if skill_tree[i] in skill: # we can use 'in' when using string
            if skill_tree[i] == skill[idx]:
                idx += 1
            else:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        answer += is_ok(skill, skill_trees[i])
    return answer