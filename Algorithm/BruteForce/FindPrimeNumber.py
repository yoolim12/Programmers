# 소수 찾기
# 파이썬 소수 개수 구하기 https://wikidocs.net/21638
# https://velog.io/@front/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%ED%8E%AB
# 순열로 나온 결과 문자열 형태로 이어 https://programmers.co.kr/learn/courses/4008/lessons/12836
import math
import itertools

def isPrime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for n in range(2,int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    pool = set()
    for i in range(1,len(numbers)+1):
        pool |= set(map(''.join, itertools.permutations(numbers, i)))
    for el in set(map(int,pool)):
        if isPrime(int(el)):
            answer += 1
    return answer