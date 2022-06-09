from collections import deque

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    # print(v, end=' ')

    while queue:
        popv = queue.popleft()
        print(popv, end=' ')
        for el in graph[popv]:
            if not visited[el]:
                visited[el] = True
                queue.append(el)

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False] * len(graph)

bfs(graph, 1, visited)