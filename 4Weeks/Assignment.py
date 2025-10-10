# 이름 : 박수진
# 학과 : 인공지능소프트웨어학과

# 1. if 문
x = 100 
if ( x > 1 ) :
    print("x는 1보다 큽니다.")

# 2. if - else 문
score = 60
if score >= 60 :
    print("합격입니다.")
    print("장학금도 수령하세요")
else :
    print("불합격입니다. ")

# 3. if - else 문 활용 1
num = int(input("양의 정수를 입력하시오 : "))
if ( num % 2 == 0) :
    print("짝수입니다.")
else :
    print("홀수입니다.")

# 4. if - else 문 활용 2
num = int(input("정수를 입력해주세요 : "))
if( num < 0) :
    print("음수입니다.")
else :
    print("양수입니다.")
    if( num % 2 == 0):
        print("짝수입니다.")
    else : 
        print("홀수입니다.")

# 5. if - else 문 활용 3
years = int(input("나이를 입력하시오 : "))
if (years >= 15) :
    print("본 영화를 보실 수 있습니다.")
else :
    print("본 영화를 보실 수 없습니다.")

# 6. random 활용
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")

# 7.  elif 문 
num = int(input("정수를 입력하시오 : "))
if num > 0 :
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else :
    print("음수입니다.")

# 8. if - else 문 안에 if - else 문 넣기
num = int(input("정수를 입력하시오 : "))
if num >= 0 :
    if num == 0 :
        print("0입니다.")
    else : 
        print("양수입니다.")
else :
    print("음수입니다.")

# 9. 
ID = input("아이디를 입력하시오 : ")
if (ID == "ilovepython") :
    PW = input("비밀번호를 입력해주세요")
    if (PW == "password") :
        print("환영합니다. ilovepython님")
    else :
        print("비밀번호가 틀립니다.")
else :
    print("아이디를 찾을 수 없습니다.")

# 10. 복붙
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")

# 11. for 문
for i in range(100): 
    print("파이썬 주식회사의 방문을 환영합니다!")
    
# 12. for - in 문
for i in [1, 2, 3, 4, 5] :
    print("i = ", i)
