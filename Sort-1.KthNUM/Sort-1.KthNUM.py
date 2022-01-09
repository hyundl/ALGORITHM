'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
'''
def solution(array, commands):
    answer = []
    for command in commands:
        #slice
        NewArray = array[command[0]-1:command[1]]
        #오름차순 정렬
        NewArray.sort()
        #list에 추가
        answer.append(NewArray[command[2]-1])        
    return answer