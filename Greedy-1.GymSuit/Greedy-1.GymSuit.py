def solution(n, lost, reserve):
    answer = 0
    student = n*[1]
    for lo in lost:
        student[lo-1]-=1
    for re in reserve:
        student[re-1]+=1
    for i in range(n-1):
        if student[i] * student[i+1] == 0:
            if student[i] + student[i+1] == 2:
                student[i], student[i+1] = 1, 1
    for j in range(n):
        if student[j] >= 1:
            answer+=1
    return answer
