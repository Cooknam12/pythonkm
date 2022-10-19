
#step 1 pymysql 모듈 불러오기
import pymysql

# step 2 mysql connection 연결
con = pymysql.connect(
    host= '172.16.12.101',
    user='scott',
    password='tiger',
    db='hr',
    charset='UTF8')

# step3 connection 으로부터 cursor 생성
cur = con.cursor();

#step4 sql문 실행
sql = 'SELECT empno, ename, JOB FROM emp'
cur.execute(sql)

# 데이타 fetch
rows = cur.fetchall();
print(rows)

#step 5 db연결 종료
con.close()
