'''list1=[11,22,33,44,55]
list2=['단출하게','단아하게','당당하게']
list3=[]
print(list1)
print(list2)
print(list3)
''
list4=[11,'홍길동',19,180.5]
#list5=[11,'홍길동',[10,10,,92,100]]
print(list4)
#print(list5)
print(f'{list4[1]}님의 키는 {list4[-1]}cm 입니다.')
''
list1=[11,22,33,44,55]
sub_list=list1[1:3]
print(sub_list)
print(sub_list[0])
''
nums=[11,22,33,44,55]
nums[0]=-1
print(nums)
nums[1:3]=[100,200,300]
print(nums)
''
nums=[11,22,33,44,55]
nums[1:2]=[100,200,300]
print(nums)
''
nums1=[11,22,33]
#nums2=[]
nums2=nums1[:]
print(nums1==nums2)
nums2[1]=0
print(nums1==nums2)
print(nums1<nums2)
print(nums1>nums2)
''
nums1=[11,22,33]
nums2=[44,55]
nums3=nums1+nums2
#nums4=nums1*2
#print(nums3)
#print(nums4)
n=len(nums3)
print(n)
''
nums=[11,22,33]
nums.append(55)
print(nums)
nums1=[11,22,33]
nums.insert(3,44)
print(nums)
nums1=[11,22,33]
nums.insert(-1,50)
print(nums)
''
nums=[11,22,33,0,11,22,33]
del nums[1]
print(nums)
del nums[2:4]
print(nums)
nums.remove(33)
print(nums)
''
nums=[11,22,33,44,55]
nums[1:4]=[]
print(nums)
nums.clear()
print(nums)
''
nums=[11,22,33,44,33]
print(nums.index(33))
print(nums.count(33))
''
nums=[11,22,33,44,55]
print(22 in nums)
print(66 not in nums)
''
t1=(11,22,33,44,55)
print(t1[0])
print(t1[1:3])
t2=(66,77)
t3=t1+t2
print(t3)
t4=t2*3
print(t4)
t5=(11,)
t6=11,
''
d={'python':'파이썬','basic':'기초','programming':'프로그래밍'}
#print(d.get('python'))
#res=d.get(0)
#print(res)
''
key=0
if key in d:
    print(d[key])
else:
    print(f'오류: 유효하지 않은 키 {key}')
''
#d['python']='PYTHON'
#del d['basic']
d.clear()
print(d)
''
#9.1
score=[]
print('[점수 입력]')
for i in range(1,4):
    s=int(input(f'#{i}? '))
    score.append(s)
average=(score[0]+score[1]+score[2])/3
print('[점수 출력]')
print(f'입력 점수: {score[0]} {score[1]} {score[2]}')
print(f'평균: {average:.1f}')
''
#9.2
score=[]
print('[점수 입력]')
for i in range(1,4):
    s=int(input(f'#{i}? '))
    score.append(s)
average=(score[0]+score[1]+score[2])/3
print('[점수 출력]')
print(f'입력 점수: {score[0]} {score[1]} {score[2]}')
print(f'평균: {average:.1f}')
average=(score[0]+score[1]+score[2])/3
print('[검색]')
ss=int(input('찾고자 하는 점수는? '))
if ss in scores:
    print(f'{ss}점은 {score.index(ss)+1}번 학생의 점수입니다.')
else:
    print(f'{ss}점을 맞은 학생은 없습니다.')
''
#9.3
shopping_bag=[]
while True:
    item=input('상품명? ')
    if item=='':
        break
    shopping_bag.append(item)
    print(f'장바구니에 {item}이 담겼습니다.')
print(f'>>>장바구니 보기: {shopping_bag}')
'''
shopping_bag={}
print('[구입]')
while True:
    item=input('상품명? ')
    if item!='':
        count=int(input('수량은? '))
        print(f'장바구니에 {item} {count}개가 담겼습니다.')
    if item=='':
        break
    shopping_bag[f'{item}']=count
print(f'>>>장바구니 보기:{shopping_bag}')
print('[검색]')
key=input('장바구니에서 확인하고자 하는 상품은? ')
if key in shopping_bag:
    print(f'{key}은(는) {shopping_bag[key]}개 담겨있습니다.')
