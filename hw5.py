
'''
n1=int(input('첫 번째 정수는? '))
n2=int(input('두 번째 정수는? '))
print(f'{n1}은/는 {n2}보다 큽니까? {n1}>{n2}')
print(f'{n1}은/는 {n2}보다 크거나 혹은 같습니까? {n1}>={n2}')
print(f'{n1}은/는 {n2}보다 작습니까? {n1}<{n2}')
print(f'{n1}은/는 {n2}보다 작거나 혹은 같습니까? {n1}<={n2}')
print(f'{n1}은/는 {n2}보다 같습니까? {n1}=={n2}')
print(f'{n1}은/는 {n2}보다 다릅니까? {n1}!={n2}')
''
age=int(input('당신의 나이는? '))
res=age>=0 and age<=120
print(f'{age}은(는) 유효한 나이인가? {res}')
res=age<0 or age>120
print(f'{age}은(는) 유효한 나이가 아닌가? {res}')
print(f'{age}은(는) 유효한 나이인가? {not res}')
''
n1=int(input('첫 번째 정수는? '))
n2=int(input('두 번째 정수는? '))
if n1>n2: print(f'{n1}은(는) {n2}보다 크다')
else: print(f'{n1}은(는) {n2}보다 크지 않다')
print('끝')
''
def is_even_number(n):
    if n%2==0:
        return True
    else:
        return False
num=int(input('정수를 입력하세요: '))
print(f'{num}은(는) ',end='')
if is_even_number(num):print('짝수',end='')
else:print('홀수',end='')
print('입니다')
''
if is_odd_number(num)==False:
    print('짝수',end='')
if is_odd_number(num):
    print('짝수',end='')
if is_odd_number(num):
    print('홀수',end='')
''
num=int(input('정수를 입력하세요: '))
''
if num==0:
    print('0',end='')
else:
    if num>0:
        print('양수',end='')
    else:
        print('음수',end='')
print('입니다')
''
if num==0:
    print('0입니다')
else:
    if num>0:
        print('양수입니다')
    else:
        print('음수입니다')
''
if num==0:
    print('0입니다')
elif num>0:
    print('양수입니다')
else:
    print('음수입니다')
''
def get_grade(s):
    if s>=90:
        return 'A'
    elif s>=80:
        return 'B'
    elif s>=70:
        return 'C'
    elif s>=60:
        return 'D'
    else:
        return 'F'
score=int(input('점수는? '))
grade=get_grade(score)
print(f'{score}점이므로 {grade}학점입니다.')
''
#7.2
def is_leap_year(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return True
    else:
        return False
def month_days(m):
    if is_leap_year(year):
        if m%2==0 and m!=2:
            print(' 30일까지 있습니다.')
        elif m%2==1:
            print(' 31일까지 있습니다.')
        else:
            print(' 29일까지 있습니다.')
    else:
        if m%2==0 and m!=2:
            print(' 30일까지 있습니다.')
        elif m%2==1:
            print(' 31일까지 있습니다.')
        else:
            print(' 28일까지 있습니다.')
year=int(input('연도? '))
month=int(input('월? '))
print(f'{year}년 {month}월은',end='')
is_leap_year(year)
month_days(month)
''
if is_leap_year(year):
    print('윤년입니다.')
else:
    print('평년입니다.')
''
#7.4
def input_age(a):
    if a>=0 and a<=120:
        return a
    else:
        return '-1'
def is_adult(a):
    if input_age(a):
        if a>=19:
            return True
        else:
            return False
age=int(input('나이? '))
input_age(age)
if is_adult(age):
    print('당신은 성인입니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')
''
#7.5
def find_char_type(ch):
    if ch==' ':
        return '공백'
    elif 'a'<=ch<='z' or 'A'<=ch<='Z':
        return '알파벳'
    elif '0'<=ch<='9':
        return '숫자'
    else:
        return '기타'
c=input('한 문자 입력? ')
ctype=find_char_type(c)
print(f'{ctype}문자를 입력했습니다.')
'''
def read_single_digit(n):
    if n==1:
        return '일 '
    elif n==2:
        return '이 '
    elif n==3:
        return '삼 '
    elif n==4:
        return '사 '
    elif n==5:
        return '오 '
    elif n==6:
        return '육 '
    elif n==7:
        return '칠 '
    elif n==8:
        return '팔 '
    elif n==9:
        return '구 '
    else:
        return '영 '
def read_number(m):
    n1=m//100
    m1=read_single_digit(n1)
    n2=(m%100)//10
    m2=read_single_digit(n2)
    n3=m%100%10
    m3=read_single_digit(n3)
    return f'{m1}{m2}{m3}'
num=int(input('세 자리 정수 입력: '))
char=read_number(num)
print(f'{char}')
