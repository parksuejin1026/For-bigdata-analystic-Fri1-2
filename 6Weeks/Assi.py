
# 이름 : 박수진
# 학과 : 인공지능소프트웨어학과

# 1. 원의 면적을 구해주는 함수
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

c_area = calculate_area(5.0)
print(c_area)

# 2. 정렬 프로그램
def sort_num(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1

print(sort_num(110, 210))
print(sort_num(2100, 80))

# 3. 사칙연산 계산기
def calc(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

n1, n2 = 200, 100
t1, t2, t3, t4 = calc(n1, n2)
print(n1, '+', n2 , '=', t1)
print(n1, '-', n2 , '=', t2)
print(n1, '*', n2 , '=', t3)
print(n1, '/', n2 , '=', t4) 