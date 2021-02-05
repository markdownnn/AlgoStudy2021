def solution(s):
    answer = 99999999999999
    for div in range(1, len(s)+1):
        prev, now = "", ""
        answer_temp = 0
        count = 0
        for i in range(0, len(s), div):
            if i + div <= len(s):
                now = s[i:i+div]
            else:
                now = s[i:]
            if i == 0:
                prev = now
                answer_temp += len(now)
            else:
                if prev != now:
                    prev = now
                    answer_temp += len(now)
                    if count >= 1:
                        answer_temp += len(str(count))
                    count = 0
                else:
                    if not count:
                        count += 2
                    else:
                        count += 1
        if count >= 1:
            answer_temp += len(str(count))
        answer = min(answer, answer_temp)
    return answer