import sys
from collections import deque

def bfs(graph, visited, isPrison, v, distance):
    visited[v] = True
    displus = 0
    cnt = 0
    queue = deque([v])

    while queue:
        displus += 1
        popv = queue.popleft()
        for el in graph[popv]:
            if not visited[el]:
                if displus > distance:
                    return cnt
                else:
                    visited[el] = True
                    if isPrison[el] == 1:
                        cnt += 1
                    queue.append(el)
    return cnt
        

def main():
    ans = []

    T = int(sys.stdin.readline())

    for tnum in range(T):
        N, K = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(N+1)]

        for i in range(N-1):
            v1, v2 = map(int, sys.stdin.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        isPrison = [-1] + list(map(int, sys.stdin.readline().split()))
        
        cnt = 0
        for v in range(1, N+1):
            if isPrison[v] == 1:
                cnt += 1
            visited = [False] * (N+1)
            cnt += bfs(graph, visited, isPrison, v, K)
        ans.append(cnt)
    
    for ansnum in range(len(ans)):
        print(f'#{ansnum+1} {ans[ansnum]}')


if __name__ == '__main__':
    main()