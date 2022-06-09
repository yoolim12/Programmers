# 딕셔너리 value 기준 정렬 https://blockdmask.tistory.com/566
# 풀이 참고 https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python
# sorted의 key값에 lambda 활용 https://ooyoung.tistory.com/59

def solution(genres, plays):
    answer = []
    dictcnt = {name:0 for name in set(genres)}
    dictlist = [(genres[i], plays[i], i) for i in range(len(plays))]
    dictlist2 = {name: [] for name in set(genres)}
    genrecnt = {name: genres.count(name) for name in set(genres)}
    for i in range(len(plays)):
        dictcnt[genres[i]] += plays[i]
    dictcntsort = sorted(dictcnt.items(), key=lambda x:x[1], reverse=True)
    dictlistsort = sorted(dictlist, key=lambda x:(x[0], -x[1], x[2]))
    
    for g,p,i in dictlistsort:
        dictlist2[g].append((p,i))
    
    for g, total in dictcntsort:
        if genrecnt[g] >= 2:
            for _ in range(2):
                p,i = dictlist2[g].pop(0)
                answer.append(i)
        else:
            p,i = dictlist2[g].pop(0)
            answer.append(i)
    
    return answer

# 다른 풀이 (람다 이해가 안됨...)
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer