# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분

import math

def calcCircleArea(r):
    area = math.pi * float(r**2)
    result = float(round(area,2))
    return result

def calcLog(a,b):
    result = round(float(math.log(b,a)),2)
    return result

def calcSin(x):
    result = round(float(math.sin(x)),2)
    return result

def calcFactorial(x):
    result = int(math.factorial(x))
    return result

def calcCombination(n, r):
    result = int(math.comb(n,r))
    return result

def calculator(order):
    if order[0] == "원":
        number = order[5:]
        answer = calcCircleArea(int(number))
        return answer
    
    elif order[0] == "로":
        order_list = order.split()
        if order_list[1] == 'e':
            order_list[1] = math.e
            answer = calcLog(int(order_list[1]),int(order_list[2]))
        else:
            answer = calcLog(int(order_list[1]),int(order_list[2]))
        if order_list[2] == 'e':
            order_list[2] = math.e
            answer = calcLog(int(order_list[1]),int(order_list[2]))
        else:
            answer = calcLog(int(order_list[1]),int(order_list[2]))
        return answer
    
    elif order[0] == "사":        
        order_list = order.split()
        answer = calcSin(int(order_list[1]))
        return answer
    
    elif order[0] == "팩":
        order_list = order.split()
        answer = calcFactorial(int(order_list[1]))
        return answer
    
    elif order[0] == "조":
        order_list = order.split()
        answer = calcCombination(int(order_list[1]),int(order_list[2]))
        return answer