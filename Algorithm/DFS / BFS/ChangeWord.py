from collections import deque

def countdiff(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt

def bfs(target, words, w, visited):
    visited[w] = True
    queue = deque([(w,0)])
    
    while queue:
        wordpop, cnt = queue.popleft()
        if wordpop == target:
            return cnt
        for el in words:
            if el != wordpop and countdiff(wordpop, el) == 1 and not visited[el]:
                queue.append((el,cnt+1))
                visited[el] = True

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = {word: False for word in words}
    cnt = bfs(target, words, begin, visited)
    return cnt