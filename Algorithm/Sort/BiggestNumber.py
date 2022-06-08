# https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98

def solution(numbers):
    num3 = [str(x) * 3 for x in numbers]
    sortnum3 = sorted(num3, reverse=True)
    answer = ''
    for el in sortnum3:
        answer += el[:int(len(el)/3)]
    return str(int(answer))

# 다른 분 풀이
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

'''
< 여기서 쓰이는 기법(?) >
1. 숫자를 문자열로 변환한 것의 비교 --> 숫자 자체의 크기로 비교하지 않고, 맨 앞의 숫자로 우선 먼저 비교한뒤, 맨 앞자리 숫자가 같으면 그 다음 자리로 비교한다.
예) '20' > '6' (거짓) --> 맨 앞자리 숫자끼리 비교했을 때 2보다 6이 더 크니까
'99' > '900' (참)

2. numbers = list(map(str, numbers)) --> numbers 배열 안의 요소들을 str 형태로 바꾼다.

3. numbers.sort(key=lambda x: x*3, reverse=True) --> numbers 배열 내의 요소 자체를 바꾸는게 아니라, 요소*3을 하였다고 할 때 그거 기준으로 정렬하라는것

4. answer 값을 int로 바꿨다가 다시 str으로 변환하는 이유 
--> [0,0,0,0]의 경우 답이 0으로 나와야하는데, 그냥 바로 return answer를 하게 되면 0 네개를 join한 "0000"이 리턴된다.
그걸 방지하기 위해 int로 바꾼 뒤에, 리턴을 문자열 형태로 해야되므로 다시 str으로 바꾼 것이다.
'''