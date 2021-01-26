def solution(numbers):
    numbers = list(map(str, numbers)) # list(map(함수, 리스트)) 여러 개의 데이터를 다른 형태로 변환하기 위해 사용
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) # '' 리스트를 문자열로 원소 사이에 빈 문자열 위치