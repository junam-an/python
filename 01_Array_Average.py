def solution(arr):
    answer = 0
    for x in arr:
        answer = answer + x
    answer = answer / len(arr)
    return answer


print(solution([0,1,2,3,4]))