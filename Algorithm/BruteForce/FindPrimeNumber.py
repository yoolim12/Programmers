# 소수 찾기
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