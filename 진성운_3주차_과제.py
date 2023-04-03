# 1번
def grade(score):
    #your code
    if score<=100 and score>=90:
        return "A"
    elif score<=89 and score>=80:
        return "B"
    elif score<=79 and score>=70:
        return "c"
    elif score<=69 and score>=60:
        return "D"
    else:
        return "F"
    
# 2번
def quadrant(x, y):
    #your code
    if x>0 and y>0:
        return "제 1사분면"
    elif x<0 and y>0:
        return "제 2사분면"
    elif x<0 and y<0:
        return "제 3사분면"
    else:
        return "제 4사분면"
    
given_x = int(input(prompt="x좌표를 입력하세요 : "))
given_y = int(input(prompt="y좌표를 입력하세요 : "))
    
quadrant(given_x,given_y)
    
# 3번
def leapYear(year):
    # your code
    if year % 400 == 0:
        return "윤년입니다."
    elif year % 4 == 0 and year % 100 != 0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."

givenyear = int(input(prompt="연도를 입력하세요 : "))

leapYear(givenyear)

# 4번
def dice(a, b, c):
    # your code
    if a != b and b != c and a != c:           #다 다를 경우
        return 100 * max(a,b,c)
    elif a==b and b==c:                        #다 같을 경우
        return 10000 + 1000 * a
    else:                                       #두개만 같을 경우
        return 1000 + 100 * extract(a,b,c)
    
def extract(a,b,c):
    if a==b or a==c:
        return a
    else:
        return b

    
# 5번
def alarm(time):
    # your code
    if len(str(time)) >= 3:
        time_hour = int(str(time)[:-2])
        time_exchange = time_hour * 60 + int(str(time)[-2:])
        result_time = time_exchange - 45
        result_time_hour = result_time // 60
        result_time_minute = result_time % 60
        return str(result_time_hour) + "시 " + str(result_time_minute) + "분"
    elif len(str(time)) == 2:
        if time < 45:
            return "23시" +str(60 - (45 - time))
        else:
            return "00시" + str(time - 45)
    else:
        return "23시" + str(60 - (45 - time))
        