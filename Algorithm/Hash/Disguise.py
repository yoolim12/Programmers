# 위장
def solution(clothes):
    answer = 1
    types = [y for x,y in clothes]
    clothescnt = [types.count(el) for el in set(types)]
    for e in clothescnt:
        answer *= e + 1
    return answer - 1