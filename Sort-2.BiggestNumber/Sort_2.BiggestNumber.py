'''
테스트 1 〉	통과 (65.68ms, 27.9MB)
테스트 2 〉	통과 (29.75ms, 19.7MB)
테스트 3 〉	통과 (86.19ms, 33.5MB)
테스트 4 〉	통과 (1.42ms, 10.5MB)
테스트 5 〉	통과 (53.44ms, 25.8MB)
테스트 6 〉	통과 (43.57ms, 23.9MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
'''
def solution(numbers):
    answer = ''
    sNumbers = []
    str_numbers = [str(i) for i in numbers]
    tmp = [j*3 for j in str_numbers]
    tmp.sort(reverse=True)
    for k in tmp:
        sNumbers.append(k[0:len(k)//3])
    for n in sNumbers:
        answer += n
    if answer.count("0") == len(answer):
        answer = "0"
    return answer
'''
from itertools import permutations
def solution(numbers):
    answer = ''
    candidate = []   
    NumPerm = list(permutations(numbers))
    for num in NumPerm:
        tmp = ''
        for x in num:
            tmp += str(x)
        candidate.append(tmp)
    int_candidate = [int(i) for i in candidate]
    answer = str(max(int_candidate))
    return candidate
'''