'''
print('"때론 내 삶의 변화를 위해 \'내어 맡김\'이 필요하다."')
''
print('11\t홍길동\n123\t을지매')
''
print('동해물과 백두산이 마르고 닳도록 \
하느님이 보우하사 우리나라 만세')

print(''\
11\t홍길동
123\t일지매\
'')
msg1,msg2='안녕','하세요'
print('안녕''하세요')
print('안녕'+'하세요')
print(msg1+msg2)
print('안녕'+msg2)
print(msg1,'+',msg2)
'
res=2*2
print('2 x 2 = '+str(res))
''
print('*'*5)
print(5*"*")
''
def divide_name(name):
    LastName=name[0]
    firstName=name[1:]
    print('-'*12+'\n성:\t'+LastName+'\n이름:\t'+firstName+'\n'+'-'*12)
name=input('당신의 이름은? ')
divide_name(name)
'
n1=int(input('첫번째 정수는? '))
n2=int(input('두번째 정수는? '))
print(f'{n1}','와',f'{n2}','의 평균은',f'{(n1+n2)/2}')
''
num=int(input('정수는? '))
print(f'2진표현으로는 0b{num:b}입니다.')
print(f'10진표현으로는 {num:d}입니다.')
print(f'16진표현으로는 0x{num:x}입니다.')
''
n1=int(input('첫번째 정수는? '))
n2=int(input('두번째 정수는? '))
avg=n1/n2
print(f'{n1}/{n2}={avg}')
print(f'{n1}/{n2}={avg:f}')
print(f'{n1}/{n2}={avg:e}')
print(f'{n1}/{n2}={avg:g}')
''
num=15
print(f'[{num:d}]')
print(f'[{num:5d}]')
print(f'[{num:<5d}]')
print(f'[{num:^5d}]')
print(f'[{12345678:5d}]')
print(f'[{num:05d}]')
''
PI=3.14159265
print(f'[{PI:f}]')
print(f'[{PI:.2f}]')
print(f'[{PI:5.2f}]')
print(f'[{PI:.2f}]')
''
num=input('정수를 입력하세요: ')
lenght=len(num)
print(f'입력하신 {num}은(는) {lenght}자리 정수입니다')
''
week='월화수목금금금'
pos=week.find('금')
print(pos)
pos=week.find('금',5)
print(pos)
pos=week.rfind('금')
print(pos)
''
msg='Python은 배우기 쉽다. Python은 강력하다'
res=msg.replace('Python','파이썬')
print(res)
print(msg)
''
#6.2
def introduce(name,grade):
    name=input('이름? ')
    grade=int(input('학년? '))
    print(name[1:]+'은 내년에',f'{grade+1}','학년입니다.')
introduce()
''
#6.2
def introduce(name,grade):
    lastname=n[1:]
    return f'{lastname}은 내년에 {grade+1}학년입니다.'
n=input('이름? ')
g=int(input('학년? '))
msg=introduce(n,g)
print(msg)
'''
#6.4
def rep_char(c,n):
    print(c*n)
#6.5
def draw_line_string(msg):
    msg1=f' Hello {msg}, '
    msg2=' Welcome to Seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(msg1)
    print(msg2)
    rep_char('-',nstr)
msg=draw_line_string(input('Input his/her name: '))
