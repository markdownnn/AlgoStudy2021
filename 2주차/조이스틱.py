def count_A(name):
    count = 0
    for i in range(len(name)):
        if name[i] != 'A':
            return count
        count += 1
    return 0

def up_down(letter):
    return min(abs(ord(letter) - ord('A')), abs(ord('Z')-ord(letter)+1))
        
def solution(name):
    answer = -1
    i = 0
    left_A, right_A = 0, 0
    if name == "A":
        return 0
    while name.count('A') < len(name):
        answer += 1
        if name[i] != 'A':
            answer += up_down(name[i])
            name = name[:i] + 'A' + name[i+1:]
        right_A = count_A(name[i+1:]+name[:i])
        if i == 0:
            left_A = count_A(name[-1:i:-1])
        else:
            left_A = count_A(name[i-1::-1]+name[-1:i:-1])
        if left_A < right_A:
            i -= 1
            if i < 0:
                i = len(name) - 1
        else:
            i += 1
            if i >= len(name):
                i = 0
    
    return answer