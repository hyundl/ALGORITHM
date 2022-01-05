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