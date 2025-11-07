
# 이름 : 박수진
# 학과 : 인공지능소프트웨어학과

# 1. 편의점 재고관리
stores = {'커피음료':7,"펜":3,"종이컵":2,"콜라":4, "책":5}

name = input("물건의 이름을 입력하시오 : ")
print(f'{name}은(는) 현재 {stores[name]}개가 있습니다.')

# 2. 집합 항목 찾기
numbers = {2, 1, 3}
if 1 in numbers:
    print("집합 안에 1이 있습니다.")
else:
    print("집합 안에 1이 없습니다.")

# 3. 집합 항목 출력
numbers = {2,1,3}
for i in numbers:
    print(i, end =" ")