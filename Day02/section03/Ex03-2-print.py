'''
print() 함수 사용법
     sep : 출력할 volue의 구분 문자
     end : volue 출력 후 출력할 문자 (기본값 '/n')
     file : 출력 방향 지정
     flush : flush 유무 지정
'''

print('재미있는', '파이썬')
print('Python', 'Java', 'c', sep=',')

print("안녕", end='')
print("하세요")

fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)
fos.close()