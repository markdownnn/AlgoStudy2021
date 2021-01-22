def solution(genres, plays):
    music = [[genres[i], plays[i], i] for i in range(len(genres))]
    music.sort(key=lambda x: (x[0], -x[1], x[2]))
    answer = []

    if len(music) == 1:
        answer.append(music[0][2])
        return answer

    start, plays_sum = 0, 0
    for i in range(len(music)-1):
        plays_sum += music[i][1]
        if music[i][0] != music[i+1][0]:
            for j in range(start, i+1):
                music[j][0] = plays_sum
            if i == len(music) - 2:
                music[i+1][0] = music[i+1][1]
            start = i + 1
            plays_sum = 0
        elif i == len(music) - 2:
            plays_sum += music[i+1][1]
            for j in range(start, i+2):
                music[j][0] = plays_sum

    music.sort(key=lambda x: -x[0])

    max_two = 1
    answer.append(music[0][2])

    for i in range(1, len(music)):
        if music[i-1][0] != music[i][0]:
            max_two = 0
        if max_two < 2:
            answer.append(music[i][2])
            max_two += 1

    return answer