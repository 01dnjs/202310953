'''pw=''
while pw!='#1234*':
    pw=input('비밀번호: ')
print('어서오세요! 문이 열렸습니다!')
''
cnt=1
print(cnt)
cnt+=1
print(cnt)
''
cnt=0
print(cnt)
while cnt<5:
    cnt+=1
    print(cnt)
''
msg='hello'
for ch in msg:
    print(f'{ch}/',end='')
''
for i in range(0,10,1):
    print(i,end=' ')
print()
for i in range(0,10):
    print(i,end=' ')
print()
for i in range(10):
    print(i,end=' ')
''
for i in range(0,10,2):
    print(i,end=' ')
print()
for i in range(10,0,-1):
    print(i,end=' ')
''
def do_one_set(n):
    pass
for s in range(3):
    n=15
    for cnt in range(1,n+1):
        print(cnt,end=' ')
    print()
'''
#n=int(input('출력할 구구단을 양의 정수로 입력하세요: '))
for i in range(1,10):
    for n in range(2,6):
        print(f'{n} x {i} = {n*i:2d}',end='  ')
        n+=1
    print(end='\n')
    i+=1
print(end='\n')
for i in range(1,10):
    for n in range(6,10):
        print(f'{n} x {i} = {n*i:2d}',end='  ')
        n+=1
    print(end='\n')
    i+=1
'''
def input_positive_number(prompt):
    n=0
    while n<=0:
        n=int(input(prompt))
    return n
def display_multiplication_table(n):
    i=1
    while i<=9:
        print(f'{n} x {i} = {n*i:2d}')
        i+=1
n=input_positive_number('출력할 구구단을 양의 정수로 입력하세요: ')
display_multiplication_table(n)

def input_age(a):
    if a>=19 and a<=120:
        return a
age=int(input('나이? '))
while input_age(age):
    print('당신은 성인입니다.')
age=int(input('나이? '))
''
#8.1
def input_age(a):
    while a<0 or a>120:
        num=int(input('나이? '))
    return a
def is_adult(a):
    if a>=19:
        return True
    else:
        return False
num=int(input('나이? '))
age=input_age(num)
if is_adult(age):
    print('당신은 성인입니다.')
else:
    print('당신은 성인이 아닙니다.')
''
def is_leap_year(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return '윤년'
    else:
        return '평년'
yn=''
if yn=='Y'or'y':
    year=int(input('연도? '))
    yy=is_leap_year(year)
    print(f'{year}년은 ',end='')
    print(f'{yy}입니다.')
    yn=input('다른 년도도 확인하시겠습니까? ')
''
h=int(input('높이? '))
n=1
for i in range(1,n):
    while n<=h:
        print(n,'\n')
        n+=1
'''
