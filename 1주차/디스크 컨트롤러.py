import heapq as hq
import math

def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs_length = len(jobs)
    time = 0
    answer = 0
    q = []
    working, start, duration = False, 0, 0
    
    while True:
        if len(jobs) > 0 and jobs[0][0] <= time:
            hq.heappush(q, jobs.pop(0)[::-1])
        if not working:
            if len(q) > 0:
                duration, start = hq.heappop(q)
                working = True
            if len(q) == 0 and len(jobs) == 0 and duration == 0:
                return math.floor(answer / jobs_length)
        duration -= 1
        time += 1
        if duration == 0:
            answer += time - start
            working = False