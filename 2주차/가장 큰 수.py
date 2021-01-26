class Num:
    def __init__(self, n):
        self.n = n
        temp = 0
        if n < 10:
            temp = n * 111111
        elif n < 100:
            temp = n * 10101
        elif n < 1000:
            temp = n * 1001
        else:
            temp = n
        self.new_n = temp
    def __lt__(self, other):
        return self.new_n < other.new_n
    def __le__(self, other):
        return self.new_n <= other.new_n
    def __gt__(self, other):
        return self.new_n > other.new_n
    def __ge__(self, other):
        return self.new_n >= other.new_n

def solution(numbers):
    arr, answer = [], ""
    for i in range(len(numbers)):
        arr.append(Num(numbers[i]))
    arr.sort(reverse=True)
    for i in range(len(arr)):
        answer += str(arr[i].n)
    return str(int(answer))