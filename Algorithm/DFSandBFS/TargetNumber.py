answer = 0
def dfs(idx, numbers, target, summ):
    global answer
    
    if idx == len(numbers):
        if summ == target:
            answer += 1
            return
        else:
            return
    
    v = numbers[idx]
    dfs(idx+1,numbers, target, summ + v)
    dfs(idx+1,numbers, target, summ - v)

def solution(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    
    return answer