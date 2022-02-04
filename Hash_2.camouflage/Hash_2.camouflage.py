def solution(clothes):
    dclothes = dict()
    answer = 1
    k = list(zip(*clothes))[1]
    for kinds in k:
        if kinds in dclothes:
            dclothes[kinds]+=1
        else:
            dclothes[kinds]=1
    for kinds in dclothes:
        dclothes[kinds]+=1
        answer *= dclothes[kinds]
    return answer-1
