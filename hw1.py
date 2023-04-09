def get_radius(prompt):
  r=int(input(prompt))
  return r
def get_circle_area():
  s=result*result*3.14
  return s
result=get_radius('넓이를 구하고자하는 원의 반지름은? ')
c=get_circle_area()
print('반지름',result,'인 원의 넓이 =','3.14 X', result, 'X', result,'=',c)
