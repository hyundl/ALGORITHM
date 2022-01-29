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
        NewArray = array[command[0]-1:command[1]]
        NewArray.sort()
        answer.append(NewArray[command[2]-1])        
    return answer

'''
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

## sort() / sorted()

리스트.sort() : 본체의 리스트를 정렬해서 변환하는 것
sorted(리스트) : 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것

ex.
students = [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]
sorted(students, key=lambda x: x[2])
-> [('최자영', 4.3, 2016301), ('김철수', 3.0, 2016302), ('홍길동', 3.9, 2016303)]
'''