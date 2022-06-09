# 더 맵게
import heapq

def solution(scoville, K):

    heapq.heapify(scoville)

    sco_num = -1
    cnt = 0
    while sco_num < K:
        if len(scoville) == 1:
            cnt = -1
            break
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        sco_num = f + s*2
        heapq.heappush(scoville, sco_num)
        cnt += 1
        
    answer = cnt
    return answer