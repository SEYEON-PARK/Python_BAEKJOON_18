# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
# (2 ≤ A, B, C ≤ 10000)

print("지금부터 세 개의 수를 입력할 겁니다.")
A=int(input("2이상이고 10,000이하인 정수를 입력하세요. : "))
B=int(input("2이상이고 10,000이하인 정수를 입력하세요. : "))
C=int(input("2이상이고 10,000이하인 정수를 입력하세요. : ")) # 숫자 입력받기

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C) # 출력하기
