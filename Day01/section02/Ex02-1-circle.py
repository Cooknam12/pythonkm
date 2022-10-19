'''
Ex02-1-circle.py

개요:반지름을 전달하면 원의 넓이를 반환하는 get_ares() 함수
'''

#math 모듈 포함
import math

#get_area() 함수 정의
def get_area(radius):
    """ 개요:반지름을 전달하면 원의 넓이를 반환하는 get_ares() 함수"""
    area = math.pi *math.pow(radius, 2)
    return area

radius = 1.5
# get_area() 함수 호출 경과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__) #Docstring 확인