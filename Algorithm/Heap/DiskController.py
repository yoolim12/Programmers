# https://www.daleseo.com/python-heapq/
import heapq

def solution(jobs):
    answer = 0
    starttime = 0
    previousStart = 0
    cnt = 0
    heap = []
    while cnt < len(jobs):
        
        if cnt == 0:
            for s,h in jobs:
                if s == 0:
                    starttime += h
                    answer += h
        else:
            for s,h in jobs:
                if (s <= starttime) and s > previousStart:
                    heapq.heappush(heap, (h,s))
            if heap:
                how,st = heapq.heappop(heap)
                previousStart = st
                answer += (starttime - st) + how
                starttime += how
            else:
                starttime += 1
        cnt += 1
    return int(answer / len(jobs))