'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (1.02ms, 10.3MB)
테스트 8 〉	통과 (0.32ms, 10.3MB)
테스트 9 〉	통과 (1.76ms, 10.3MB)
테스트 10 〉	통과 (0.82ms, 10.3MB)
테스트 11 〉	통과 (2.03ms, 10.3MB)
테스트 12 〉	통과 (1.74ms, 10.3MB)
테스트 13 〉	통과 (0.10ms, 10.3MB)
테스트 14 〉	통과 (1.86ms, 10.3MB)
'''
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

'''
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    person = []
    i, oneN, twoN, threeN = 0, 0, 0, 0
    for answer in answers:
        if answer == one[(i % 5)]:
            oneN+=1
        if answer == two[(i % 8)]:
            twoN+=1
        if answer == three[(i % 10)]:
            threeN+=1
        i+=1
    num = [oneN, twoN, threeN]
    for idx, score in enumerate(num):
        if score == max(num):
            person.append(idx+1)
    return person

## enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 함수 
순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포함하는 enumerate 객체 리턴 
보통 enumerate 함수는 for문과 함께 자주 사용
'''