def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(r):
    area=3.14*r*r
    return area

print('넓이를 구하고자 하는 원의 반지름은?')
r=get_radius('')
print('반지름',r,'인 원의 넓이=,','3.14x',r,'x',r,'=',get_circle_area(r))
