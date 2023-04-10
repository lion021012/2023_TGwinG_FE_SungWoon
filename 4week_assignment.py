# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                continue;
            elif lst[i] * 2 == lst[j]:
                result += 1
           
    return result
                
    
# 2번
def pascal(n):
    result_list_one = list()
    result_list_two = list()
    for i in range(1,n + 1):
        if i == 1 or i == 2:
            result_list_one.append(1)
        else:
            for j in range(1,len(result_list_one)):
                result_list_one[j] = result_list_two[j-1] + result_list_two[j]
            result_list_one.append(1) 
        result_list_two = list() + result_list_one    
    return result_list_one


# 3번
def beerRefrigerator(n):
    result_list = list()
    for i in range(1,n+1):
        for j in range(1,n+1):
            extra_number = n / (i*j)
            if extra_number != int(extra_number):
                continue;
            result_list.append(str(i) +  " x " + str(j) + " x " + str(int(extra_number)))
            result_list.append(2*(i*j + i*extra_number + j*extra_number))
    result_list_compare = result_list[1::2]
    result_list_min = min(result_list_compare)
    index_number = result_list.index(result_list_min) - 1
    return result_list[index_number]
    
# 4번
def matrixMul(mat1, mat2):
    # your code
    return