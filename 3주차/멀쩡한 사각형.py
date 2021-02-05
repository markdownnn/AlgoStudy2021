import math

def gcd(x, y):
    while y:

def get_gcd(max_l, min_l):
    gcd = math.gcd(max_l, min_l) // math 모듈의 gcd 만약 이걸 이용하지 못하면
    new_max_l, new_min_l = max_l / gcd, min_l / gcd
    return int(gcd), int(new_max_l), int(new_min_l)

def solution(w,h):
    gcd, max_l, min_l = get_gcd(max(w, h), min(w, h))
    result = w * h
    crossed_squares = 0
    for i in range(min_l):
        crossed_squares += math.ceil((i + 1) * max_l / min_l) - math.floor(i * max_l / min_l)
    return result - gcd * crossed_squares