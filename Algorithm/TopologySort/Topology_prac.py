from collections import deque

# v,e = 7,8
# graph = [[], [2,5], [3,6], [4], [7], [6], [4], []]
# indegree = [0 for _ in range(v+1)]

# for i in range(len(graph)):
#     for el in graph[i]:
#         indegree[el] += 1

def topology_sort(graph, indegree):
    q = deque()
    res = []

    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        popv = q.popleft()
        res.append(popv)

        for el in graph[popv]:
            indegree[el] -= 1
            if indegree[el] == 0:
                q.append(el)
    
    return res


def solution(graph):
    v = len(graph) - 1
    e = 0
    for el in graph:
        e += len(el)
    
    indegree = [0 for _ in range(v+1)]

    for i in range(len(graph)):
        for el in graph[i]:
            indegree[el] += 1
    
    res = topology_sort(graph, indegree, v, e)

    for el in range(1, len(res)):
        print(res[el], end=' ')


solution([[], [2,5], [3,6], [4], [7], [6], [4], []])