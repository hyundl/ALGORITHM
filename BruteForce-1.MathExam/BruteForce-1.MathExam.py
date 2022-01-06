def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    num = []
    i, oneN, twoN, threeN = 0, 0, 0, 0
    for answer in answers:
        if answer == one[(i % 5)]:
            oneN+=1
        if answer == two[(i % 8)]:
            twoN+=1
        if answer == three[(i % 10)]:
            threeN+=1
        i+=1
    MaxScore = max(oneN, twoN, threeN)
    if MaxScore == oneN:
        num.append(1)
    if MaxScore == twoN:
        num.append(2)
    if MaxScore == threeN:
        num.append(3)
    return num