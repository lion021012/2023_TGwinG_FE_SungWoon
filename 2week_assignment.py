# 1번
def sum(a, b):
    # your code
    return a+b

# 2번
def sub(a, b):
    # your code
    return a-b

# 3번
def mul(a, b):
    # your code
    return a*b

# 4번
def div(a, b):
    # your code
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    # your code
    return ((x1-x2)**2+(y1-y2)**2)**1/2

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    # your code
    a = lylics[21:31]
    return a

# 7번
def reverseStr(string):
    # your code
    reversed_str = string[::-1]
    return print(reversed_str)

# 8번
def introduce():
    # your code
    userbirthday_month = int(birthday[2:4])
    userbirthday_day = int(birthday[4:6])
    user_introduce = "제 이름은 " + str(username) + "입니다. 취미는 " + str(userhabit) + "입니다. 저는 " + str(useruniversity) + "를 다니고 있습니다. 제 생일은 " + str(userbirthday_month) + "월 " + str(userbirthday_day) + "일 입니다."
    return user_introduce
username = input(prompt="이름을 입력하세요 : ")
userhabit = input(prompt="취미를 입력하세요 : ")
useruniversity = input(prompt="재학 중인 학교를 입력하세요 : ")
birthday = input(prompt="생일을 입력하세요 : ")

resultRight = introduce()
print(resultRight)

# 9번
def calc():
    # your code
    first_number = int(input(prompt="첫 번째 수를 입력하세요 : "))
    second_number = int(input(prompt="두 번째 수를 입력하세요 : "))
    add = first_number + second_number
    sub = max(first_number,second_number) - min(first_number,second_number)
    mul = first_number * second_number
    div = max(first_number,second_number) // min(first_number,second_number)

    result = print("두 수의 합 : " + add , "두 수의 차 : " + sub , "두 수의 곱 : " + mul , "두 수의 몫 : " + div , sep="\n")
    return result

calc()