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
    return answer
