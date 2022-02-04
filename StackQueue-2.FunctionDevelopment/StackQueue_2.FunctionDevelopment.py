'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
'''
def solution(progresses, speeds):
    day = []
    count = {}
    for i in range(len(progresses)):
        q = (100-progresses[i]) // speeds[i] #몫
        r = (100-progresses[i]) % speeds[i]  #나머지
        if r == 0:
            day.append(q)            
        else:
            day.append(q+1)
    for j in range(len(day)-1):
        if day[j] > day[j+1]:
            day[j+1] = day[j]
    for k in day:
        try: count[k] += 1
        except: count[k]=1
    answer = list(count.values())
    return answer
