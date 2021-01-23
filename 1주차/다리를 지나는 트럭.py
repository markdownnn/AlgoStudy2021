def solution(bridge_length, weight, truck_weights):
    trucks = [[truck_weights[i], 0] for i in range(len(truck_weights))] # zip을 사용하려 했으나 zip-tuple은 값 수정이 불가능
    total_weight, on_board = 0, 0
    answer = 0
    
    while trucks:
        if on_board < len(trucks) and trucks[on_board][0] + total_weight <= weight: # 마지막 인덱스 밖은 체크하면 안 됨
            total_weight += trucks[on_board][0]
            on_board += 1
        for i in range(on_board):
            trucks[i][1] += 1
        if trucks[0][1] >= bridge_length:
            total_weight -= trucks[0][0]
            on_board -= 1
            trucks.pop(0)
        answer += 1
            
    return answer + 1