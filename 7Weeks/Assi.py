
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
print(lst, lst1)
