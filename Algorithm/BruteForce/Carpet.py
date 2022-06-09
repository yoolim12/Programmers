# 카펫
# 파이썬 약수 구하기
# https://minnit-develop.tistory.com/16
def solution(brown, yellow):
    answer = []
    totalS = brown + yellow
    for el in range(totalS - 1, int(totalS ** 0.5) - 1, -1):
        if totalS % el == 0:
            width = el
            height = totalS // el
            cntyellow = (width - 2) * (height - 2)
            cntbrown = totalS - cntyellow
            if cntyellow == yellow:
                answer.append(width)
                answer.append(height)
                break
    return answer

# 이렇게 둘레를 이용해서 풀 수도 있다
# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]