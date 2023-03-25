'''
def first():
    print('안녕')
    second()
def second():
    print('반가워')
first()

def first():
    msg='안녕'
    print(msg)
    second()
    print(msg)
def second():
    msg='반가워'
    print(msg)
first()

def get_circle_area(radius):
    result=3.14*radius**2
    return result
r=float(input('넓이를 구할 원의 반지름은? '))
result=get_circle_area(r)
print(result)

print('현재 모듈 이름:',__name__)
''
import calc_area as ca
area=ca.get_circle_area(10)
print(area)
area=ca.get_rect_area(10,20)
print(area)
''
from calc_area import get_circle_area
from calc_area import get_rect_area
area=get_circle_area(10)
print(area)
area=get_rect_area(10,20)
print(area)
''
def get_circle_area(r):
    print('반지름',r,'인 원의 넓이를 계산합니')
from calc_area import *
area=get_circle_area(10)
print(area)
area=get_rect_area(10,20)
print(area)
'
from calc_area import get_circle_area as ca
from calc_area import get_rect_area as ra
area=ca(10)
print(area)
area=ra(10,20)
print(area)
''
from random import randint
def roll_dice():
    return randint(1,6)
def main():
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
if __name__=='__main__':
    main()
''
exchange_rate=0
def set_rate(rate):
    global exchange_rate
    exchange_rate=rate
def get_rate():
    return exchange_rate
def to_dollar(won):
    return won/exchange_rate
def to_won(dollar):
    return dollar*exchange_rate
def main():
    print('### 환율 변환 모듈 테스트 ###')
    set_rate(1010)
    print('오늘의 환율',get_rate())
    print('2020원 =',to_dollar(2020))
    print('2달러 =',to_won(2))
if __name__=='__main__':
    main()
'
import exchange_currency as ex
def main():
    rate=int(input('$1에 대한 오늘의 환율은? '))
    dollar=int(input('원화로 변환할 달러화 액수는? '))
    print(dollar,'달러는',ex.to_won(dollar),'원 입니다.')
    won=int(input('달러화로 변환할 원화 액수는? '))
    print(won,'원은',ex.to_dollar(won),'입니다.')
if __name__=='__main__':
    main()
'''
import math
sale=int(input('할인률은? '))
def get_fixed_price():
    Acost=int(input('A 상품의 할인된 가격은? '))
    return Acost
A=get_fixed_price()
def get_fixed_price():
    Bcost=int(input('B 상품의 할인된 가격은? '))
    return Bcost
B=get_fixed_price()
print('A상품의 정가는',A/0.8,'원')
print('B상품의 정가는',B/0.8,'원')
