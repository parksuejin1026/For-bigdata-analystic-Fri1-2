
## 이름 : 박수진
## 학과 : 인공지능소프트웨어학과

# 1. 과일 리스트 

fruits_list = []
count = 0
for i in range(3):
    name = input("좋아하는 과일 이름을 입력하시오 : ")
    fruits_list.append(name)

name = input("과일의 이름을 입력하세요 : ")
if name in fruits_list:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")

# 2. 도시 인구 자료

population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954] # 도시 인구 자료 리스트 생성

print('서울 인구 : ', population[1]) # 1번 인덱스
print('인천 인구 : ', population[-1]) # 마지막 인덱스인 5번 인덱스 출력

cities = population[0::2] # 0번 인덱스부터 2칸씩 띄어서 출력 도시만 출력
print('도시 리스트 : ',cities)
pops = population[1::2] # 1번 인덱스부터 2칸씩 띄어서 출력 인구만 출력
print('인구 총 합계', sum(pops)) 

# 3. pop() 메서드

lst = [0, 10, 20, 30, 40, 50]
lst5 = lst.pop()
print(lst5, lst)
lst1 = lst.pop(1)
print(lst1, lst)

bts = ['V', 'J-Hope', 'Suga', 'Jungkook'] # for 문 사용
for member in bts:
    print(member)

# 4. sort(), reverse
numbers = [9,6,7,1,8,4,5,3,2] 
numbers.sort() # 정렬
print(numbers)
numbers.sort(reverse=True) # 오름차순은 reverse=True 사용
print(numbers)

# 문자열일 경우 : 사전 순서대로 정렬
bts = ['V', 'J-Hope', 'Suga', 'Jungkook']
bts.sort()
print(bts)

# 5. sorted()
numbers = [ 9,6,7,1,8,4,5,3,2]
new_list = sorted(numbers) # 새로운 리스트에 내림차순으로 정리해서 저장 numbers는 바뀌지않음
print(new_list)
print(numbers)

# 6. list(), 인덱싱, 슬라이싱, split()
s = 'python'
str_list = list(s)
print(str_list)

print('s[0] =', s[0])
print('s[1] =', s[1])
print('s[-1] =', s[-1])
print('s[0:2] =', s[0:2])
print('s[-2:] =', s[-2:]) # -2번째 인덱스인 4번인덱스부터 5번인덱스까지 출력
print('s[-1:-3:-1] =', s[-1:-3:-1]) # 마지막 두 문자열 거꾸로 출력 -1(6)번 인덱스부터 -2(5)번 인덱스까지 출력

# split() 메서드
s = '23 35 67 88 1'
num_list = s.split() # 디폴트는 공백을 분리함 공백을 기준으로 문자열을 만들어 list 항목으로 분리하는 거임 ['23','35'] 이런 식으로
print(num_list)

s = '23,35,67,88,1'
num_list = s.split(',')
print(num_list)

# 7. 오늘의 명언
import random
quotes = []
quotes.append("꿈을 지녀라, 그러면 어려운 현실을 이길 수 있다.")
quotes.append("언제나 현재에 집중할 수 있다면 행복할 것이다.")
quotes.append("고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
quotes.append("사람은 사랑할 때 누구나 시인이 된다.")
quotes.append("시작이 반이다.")

print("####################")
print("#    오늘의 명언    #")
print("####################")
print("")

dailyQuote = random.choice(quotes)
print(dailyQuote)

# 8. sort()와 슬라이스를 써서 최댓값, 최솟값 구하기

heights = [178, 173, 166, 164, 176]
heights.sort()
print("이 중에서 가장 작은 값은 : ", heights[0])
print("이 중에서 가장 큰 값은 : ", heights[-1])


# 9. min(), max() 함수를 사용해서 최댓값, 최솟값 구하기

heights = [178, 173, 166, 164, 176]
print("이 중에서 가장 작은 값은 : ", min(heights))
print("이 중에서 가장 큰 값은 : ", max(heights))

