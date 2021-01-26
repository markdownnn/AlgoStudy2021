def isPrime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check(total, selected, saved):
    result = 0
    if selected != "":
        if int(selected) not in saved:
            result = isPrime(int(selected))
            saved.append(int(selected))
    for i in range(len(total)):
        result += check(total[:i]+total[i+1:], selected+total[i], saved)
    return result

def solution(numbers):
    answer = 0
    answer = check(numbers, "", [])
    return answer