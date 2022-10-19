'''
Set
   순서가 없다
   변경할 수 없다
   인덱싱 되지 않는 컬렉션
'''

thisset = {"피카츄", "라이츄", "파이리"}
#실행할 때 마다 순서가 변경
print(thisset)

# 항목 가져오기
thisset = {"피카츄", "라이츄", "파이리"}
for x in thisset:
    print(x)

# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬북이" in thisset)

# 항목 추가하기
thisset = {"피카츄", "라이츄", "파이리"}
thisset.add("꼬북이")
print(thisset)
print("꼬북이" in thisset)

# 다른 set의 항목 추가(중복값 허용 안함)
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬북이", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목 제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")
# print(thisset)

thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)

# 항목 제거(랜덤제거)
thisset.pop()

# 비우기
thisset.clear()
print(thisset)