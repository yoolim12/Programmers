from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        popv = queue.popleft()
        for i in range(len(graph[popv])):
            if graph[popv][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return visited

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    while False in visited:
        idx = visited.index(False)
        visited = bfs(computers, idx, visited)
        cnt += 1
        print(visited)

    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))