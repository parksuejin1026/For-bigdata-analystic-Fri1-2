
#이름 : 박수진
#학과 : 인공지능소프트웨어학과

#1. 반복을 이용하여 팩토리얼 계산하기
n = int(input("정수를 입력하시오: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print(n, "!은", fact, "이다.")

#2. 사용자로부터 암호를 받아 로그인하기
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
    
print("** 로그인 성공 **")

#3. 1~10까지 더하는 코드
count = 1
s = 0
while count <= 10 :
    s = s + count
    count = count + 1
print("합계는 ", s)


#4. 구구단 
dan = int(input("원하는 단은 : "))
i = 1 

while i <= 9:
    print("%s * %s = %s" % (dan, i, dan * i))
    i = i + 1

#5. 암산 문제
import random

while True:
    x = random.randint(1,100) 
    y = random.randint(1,100)
    print(x, '+', y, '=', end = ' ')
    answer = int(input())
    if answer == x + y:
        print("잘했어요!")
    else:
         print("정답은", x+y, "입니다. 다음 번에는 잘할 수 있죠?")

#6. 무한 루프와 break로 빠져나가기
while True:
    light = input("신호등 색상을 입력하시오 : ")
    if light == 'green':
        break

print("녹색 신호입니다. 전진하세요!")

#7. continue 사용
st = 'I love Python Programing'
for ch in st:
    if ch in ['a','e','i','o','u', 'A','E','I','O','U']:
        continue
    print(ch, end= '')

#8. format() 메서드
for i in range(2, 11, 2):
    print('{0:3d} {1:4d} {2:5d}'.format(i, i *i , i*i*i))

#9. 쉼표 출력
print('{:,}'.format(1234567890))