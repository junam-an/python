##"a1234", "23871" 같은 문자열을 입력 받아 숫자값일 경우 True, 문자가 섞여있을 경우 False 리턴 예제

def Solution(s):
    output_s= True
    input_s=list(s)
    encounter=list("1234567890")

    for x in input_s:
        count=0
        for y in encounter:
            if x == y:
                count=count+1

        if count == 1:
            output_s=True
        else:
            output_s=False
            break

    return output_s


print(Solution("1c23a4"))











