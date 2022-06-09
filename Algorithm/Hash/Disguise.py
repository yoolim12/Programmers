# 위장
# https://velog.io/@ourlife/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%EC%9E%A5-%EA%B2%BD%EC%9A%B0%EC%9D%98-%EC%88%98%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%92%80%EC%9D%B4
def solution(clothes):
    answer = 1
    types = [y for x,y in clothes]
    clothescnt = [types.count(el) for el in set(types)]
    for e in clothescnt:
        answer *= e + 1
    return answer - 1