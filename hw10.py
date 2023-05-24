'''
file=open('example.txt','w')
file.close()
print('파일 열고 닫기 완료')
''
import os
filename='example.txt'
if os.path.exists(filename):
    file=open(filename,'r')
    file.close()
else:
    print(f'ERROR:{filename}이 존재하지 않습니다!')
print('끝')
''
import os
if not(os.path.isdir('data')):
    os.makedirs('data')
''
with open('data/example.txt','w') as file:
    pass
print('파일 열고 닫기 완료')
''
num=2
name='홍길동'
with open('example.txt','w') as file:
    file.write('1 이찬수\n')
    file.write(f'{num} {name}\n')
#print('끝')
''
num=2
name='홍길동'
with open('example.txt','w') as file:
    file.write('1 이찬수\n')
    file.write(f'{num} {name}\n')
''
with open('data/example.txt','r') as file:
    all_text=file.read()
print(all_text)
''
lines=[]
with open('example.txt','r') as file:
    #lines=file.readlines()
    for line in file:
        lines.append(line.strip('\n'))
print(lines)
''
import pickle
filepath='data/example.bin'
def save_data(num,name,height,scores):
    with open(filepath,'wb') as file:
        pickle.dump(num,file)
        pickle.dump(name,file)
        pickle.dump(height,file)
        pickle.dump(scores,file)
def load_data():
    with open(filepath,'rb') as file:
        num=pickle.load(file)
        name=pickle.load(file)
        height=pickle.load(file)
        scores=pickle.load(file)
    return num,name,height,scores
num,name,height=123,'홍길동',180.5
scores={'mid':90,'fin':95,'rep':10,'att':10}
save_data(num,name,height,scores)
r_num,r_name,r_height,r_scores=load_data()
print(r_num)
print(r_name)
print(r_height)
print(r_scores)
''
import pickle
filepath='circle.bin'
class Circle:
    __PI=3.14159265
    def getPI(self):
        return __PI
    def __init__(self,radius):
        self.__radius=radius
        def getCircumference(self):
            result=2*Circle.__PI*self.__radius
            return result
    def getArea(self):
        result=Circle.__PI*self.__radius**2
        return result
with open(filepath,'wb') as file:
    c1=Circle(10)
    pickle.dump(c1,file)
with open(filepath,'rb') as file:
    c2=pickle.load(file)
    print(f'원의 넓이는 {c2.getArea()}')
''
#12.1
import os
filename='readme.txt'
fname=input('파일명:')
if os.path.exists(filename):
    with open('readme.txt','w') as file:
        file.write('1:안녕하세요 반갑습니다.\n')
        file.write('2:이 파일은 테스트 파일 저작을 위해 작성된 텍스트 문서입니다.\n')
        file.write('3:조금 낮설더라도 포기하지 마세요.')
    with open('readme.txt','r') as file:
        all_text=file.read()
    print(all_text)
''
#12.3
import os
filename='shoppingbag.txt'
def buy(sh):
    print('[구입]')
    while True:
        item=input('상품명? ')
        if item=='':
            break
        shopping_bag.append(item)
        print(f'장바구니에 {item}이 담겼습니다.')
def show(sh):
    with open('shoppingbag.txt','r') as file:
        text=file.read()
    print(f'>>>장바구니 보기: {text}')
shopping_bag=[]
if os.path.exists(filename):
    show(shopping_bag)
    buy(shopping_bag)
    with open('shoppingbag.txt','a') as file:
        file.write(f'{shopping_bag}')
    show(shopping_bag)
else:
    buy(shopping_bag)
    with open('shoppingbag.txt','a') as file:
        file.write(f'{shopping_bag}')
    show(shopping_bag)
''
import os
import pickle
filepath='data/score.bin'
class Score:
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
def save_data(scores,avg):
    with open(filepath,'wb') as file:
        pickle.dump(scores,file)
        pickle.dump(avg,file)
def load_data():
    with open(filepath,'rb') as file:
        scores=pickle.load(file)
        avg=pickle.load(file)
    return scores,avg
if os.path.exists(filepath):
    r_scores,r_avg=load_data()
    print('[파일 읽기]')
    print()
    print('[점수 출력]')
    print(f'개인점수:{r_scores}')
    print(f'평균:{r_avg:.1f}')
print('[점수 입력]')
scores=Score.input_scores()
print('[점수 출력]')
print('개인점수: ',end='')
Score.show_scores(scores)
avg=Score.get_average(scores)
print(f'평균:{avg:.1f}')
save_data(scores,avg)
'''
import os
import pickle

filepath = 'data/score.bin'

class Score:
    @staticmethod
    def input_scores():
        scores = []
        i = 1
        while True:
            n = int(input(f'#{i}? '))
            if n < 0:
                break
            scores.append(n)
            i += 1
        return scores

    @staticmethod
    def get_average(scores):
        total = sum(scores)
        return total / len(scores)

    @staticmethod
    def show_scores(scores):
        print(' '.join(str(n) for n in scores))

def save_data(scores, avg):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(avg, file)

def load_data():
    try:
        with open(filepath, 'rb') as file:
            scores = pickle.load(file)
            avg = pickle.load(file)
        return scores, avg
    except (EOFError, pickle.UnpicklingError):
        return [], 0

if os.path.exists(filepath):
    r_scores, r_avg = load_data()
    print('[파일 읽기]')
    print(end='\n')
    print('[점수 출력]')
    print('개인점수: ', end='')
    Score.show_scores(r_scores)
    print(f'평균: {r_avg:.1f}')
else:
    print('[점수 입력]')
    scores = Score.input_scores()

    print('[점수 출력]')
    print('개인점수: ', end='')
    Score.show_scores(scores)

    avg = Score.get_average(scores)
    print(f'평균: {avg:.1f}')

    save_data(scores, avg)
