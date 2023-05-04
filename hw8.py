'''
def input_list(lst):
    name=input('이름? ')
    num=input('번호? ')
    lst.append(name)
    lst.append(num)
userinfor=[]
input_list(userinfor)
print(f'{userinfor[1]}번 {userinfor[0]}')
''
def input_list():
    name=input('이름? ')
    num=input('번호? ')
    lst=[]
    lst.append(name)
    lst.append(num)
    return lst
userinfor=input_list()
print(f'{userinfor[1]}번 {userinfor[0]}')
''
#10.1
def get_date():
    y=int(input('연도? '))
    m=int(input('월? '))
    d=int(input('일? '))
    return (y,m,d)
print('당신의 생일을 입력하세요:')
bday=get_date()
print(f'당신의 만 60번째 생일은 {bday[0]+60}년 {bday[1]}월 {bday[2]}일 입니다.')
''
msgs=['단출하게','단아하게','당당하게']
for e in msgs:
    print(f'{e}/',end='')
''
msgs=['단출하게','단아하게','당당하게']
for e in range(len(msgs)):
    print(f'{msgs[e]}/',end='')
''
msgs=['단출하게','단아하게','당당하게']
for e in range(len(msgs)-1,-1,-1):
    print(f'{msgs[e]}/',end='')
''
def input_num_of_population():
    nPeople=[]
    for i in range(4):
        n=int(input(f'{i+1}층의 거주인원수는? '))
        nPeople.append(n)
    return nPeople
def show_num_of_population(p):
    cnt=len(p)
    for i in range(cnt):
        print(f'{i+1}층의 거주인원수는 {p[i]}명 입니다.')
def get_total(lst):
    total=0
    for i in lst:
        total+=i
    return total
population=input_num_of_population()
show_num_of_population(population)
total=get_total(population)
print(f'총 거주인원수는 {total}명 입니다.')
''
scores=[
    ['이찬수',95,85],
    ['홍길동',90,80]
]
print(scores)
print(scores[0])
print(scores[0][0])
''
scores=[
    ['이찬수',95,85],
    ['홍길동',90,80]
]
for g in scores:
    for e in g:
        print(e,end='/')
    print()
''
scores=[
    ['이찬수',95,85],
    ['홍길동',90,80]
]
for gi in range(len(scores)):
    for ei in range(len(scores[gi])):
        print(scores[gi][ei],end='/')
    print()
''
d={
    'python':'파이썬',
    'basic':'기초',
    'programming':'프로그래밍'
}
for key in d.keys():
    print(key,d[key])
''
def dict_get(dic,key):
    if key in dic:
        return dic[key]
    else:
        return None
d={'python':'파이썬','basic':'기초','programming':'프로그래밍'}
res=dict_get(d,'python')
if res!=None:
    print(res)
else:
    print('오류: 잘못된 키')
res=dict_get(d,0)
if res!=None:
    print(res)
else:
    print('오류: 잘못된 키')
''
def dict_append(dic,key,value):
    if key in dic:
        return False
    dic[key]=value
    return True
d={'python':'파이썬','basic':'기초','programming':'프로그래밍'}
if dict_append(d,'PYTHON','파이썬'):
    print('추가 성공')
else:
    print('추가 실패')
if dict_append(d,'basic','베이직'):
    print('두번째 추가 성공')
else:
    print('두번째 추가 실패')
print(d)
''
def dict_delete(dic,key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False
d={'python':'파이썬','basic':'기초','programming':'프로그래밍'}
if dict_delete(d,'basic'):
    print('삭제 성공')
else:
    print('삭제 실패')
print(d)
''
#10.2
def find_max(lst):
    m=lst[0]
    for i in range(1,len(lst)):
        for j in range(len(lst)):
            if nums[i]>m:
                m=nums[i]
    return m
nums=[]
for i in range(5):
    n=int(input('정수 입력: '))
    nums.append(n)
print(f'가장 큰 정수는 {find_max(nums)}입니다.')
''
#10.3
def input_scores():
    s=[]
    i=1
    while(True):
        n=int(input(f'#{i}? '))
        if n<0:
            break
        s.append(n)
        i+=1
    return s
def get_average(s):
    total=0
    for i in s:
        total+=i
    return total/len(s)
def show_scores(s):
    for n in s:
        print(n,end=' ')
    print()
print('[점수 입력]')
scores=input_scores()
print('[점수 출력]')
print('개인점수: ',end='')
show_scores(scores)
avg=get_average(scores)
print(f'평균:{avg:.1f}')
''
#10.4
def input_scores():
    s=[]
    i=1
    while(True):
        n=int(input(f'#{i}? '))
        if n<0:
            break
        s.append(n)
        i+=1
    return s
def get_average(s):
    total=0
    for i in s:
        total+=i
    return total/len(s)
def show_scores(s):
    for n in s:
        print(n,end=' ')
    print()
def search(n,lst):
    if n not in scores:
        return None
    return lst.index(n)
print('[점수 입력]')
scores=input_scores()
print('[점수 출력]')
print('개인점수: ',end='')
show_scores(scores)
avg=get_average(scores)
print(f'평균:{avg:.1f}')
print('[검색]')
ss=int(input('찾고자 하는 점수는? '))
idx=search(ss,scores)
if idx!=None:
    print(f'{ss}점은 {scores.index(ss)+1}번 학생의 점수입니다.')
else:
    print(f'{ss}점을 맞은 학생은 없습니다.')
'''
def buy(sh):
    print('[구입]')
    while True:
        item=input('상품명? ')
        if item!='':
            count=int(input('수량은? '))
            print(f'장바구니에 {item} {count}개가 담겼습니다.')
        if item=='':
            return False
        sh[f'{item}']=count
def show(sh):
    print(f'>>>장바구니 보기:{sh}')
def find(sh):
    print('[검색]')
    key=input('장바구니에서 확인하고자 하는 상품은? ')
    if key in sh:
        print(f'{key}은(는) {sh[key]}개 담겨있습니다.')
    else:
        print(f'장바구니에 {key}은(는) 없습니다.')
shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)
