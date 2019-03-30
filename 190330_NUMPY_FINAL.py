'''
2019 03 30 작성자 류현수
ELICE IO + ITGO 강좌 정리 노트
'''
#NOW DAYS DATA SCIENCE USE PYTHON A LOT.
#NUMPY -> 다차원 배열 처리를 위해 필요하다. 배열의 차원은 RANK라고합니다.

import numpy as np

#numpy배열을 만들어 내는 방법.
#1. python LIST를 이용하는 방법
#2. numpy 함수를 이용하는 방법

#1.
arr = np.array([1,2,3,4,5], dtype = "float")
print(arr)
#2.
# 2 - 1 모든값을 0으로 채워주는 함수 zeros
arr = np.zeros((10,10), dtype = "f") #shape, dtype을 념겨준다.
print(arr)
arr = np.zeros(10, dtype = "int") #1차원
print(arr)
# 2 - 2 모든값을 1로 채워주는 함수 ones
arr = np.ones((10, 1), dtype = "int")
print(arr)
arr = np.ones(10, dtype = "float")
print(arr)
# 2 - 3 arange 함수
arr = np.arange(10, dtype = "int")
print(arr)
arr = np.arange(0, 10, 2, dtype = "int")
print(arr)
# 2 - 4 linspace 함수
arr = np.linspace(0, 1, 5)
print(arr)
# 2 - 5 random.random -> shape을 이용함
arr = np.random.random((5,5))
print(arr)
# 2 - 6 random.normal -> 평균, 표준편차를 이용한 행렬만들어줌.
arr = np.random.normal(10, 1,(5,5))
print(arr)
# 2 - 7 random.randint -> 정수랜덤 값
arr = np.random.randint(0, 5, (2,2), dtype = "int")
print(arr)
arr = np.random.randint(5, size = (2,2), dtype = "int")
print(arr)
# 2 - 8 사용자가 지정한 값을 넣어주는 full
arr = np.full((10, 10), 4, dtype = "int")
print(arr)
# 2 - 9 eye -> 대각선을 1로 채워주는 함수
arr = np.eye(4, dtype= "int")
print(arr)

#numpy배열을 slicing 하는 방법
arr = np.arange(1, 17).reshape((4,4))
print(arr)
print(arr[1 : 4]) #1행부터 4행까지 보여주세요.
print(arr[1:, 1:]) #1행부터 3행까지 1열부터 3열까지
print(arr[2:3, 1:]) #2행의 1열부터 
print("**************************************************")
#numpy배열을 indexing 하는 방법
print(arr[[0, 2], [1, 3]]) #(0, 1)과 (2, 3)을 출력해줍니다.
#numpy배열의 boolean indexing하는 방법
bool_arr = (arr % 2 == 0) #target 배열에 조건 연산을 한 결과를 저장해주면 됩니다.
print(bool_arr)
print(arr[bool_arr]) #해당하는 값만 출력해줍니다.
print("****************************************************")

#numpy_array의 속성들
print(arr.dtype) #데이터타입 int32
print(arr.ndim)  #차원 2차원
print(arr.shape) #행렬 모양 (4,4)
print(arr.size)  #사이즈 16
print(arr[2,3])  #2행3열 값 12

#numpy배열의 서로 합치기 concatenate을 구현 하는 방법.
x = np.arange(16).reshape((4, 4))
y = np.arange(16).reshape((4, 4))

z1 = np.concatenate([x, y], axis = 0)
z2 = np.concatenate([x, y], axis = 1)
print(z1)
print(z2)

#numpy배열의 쪼개기 split을 구현하는 방법
a, b = np.split(z1, [4], axis = 0)
print(a)
print("*********************************************")
print(b)
print("*********************************************")
a, b = np.split(z2, [4], axis = 1)
print("*********************************************")
print(a)
print("*********************************************")
print(b)

#numpy의 연산방법
#add(), subtract(), multiply(), divide() 가있다.

#특별히 행렬의 곱셈, 벡터의 연산은 dot()을 이용한다.

#아래와 같은 연산에는 option으로 axis를 사용할 수 있다.
target = np.arange(1, 19).reshape((6, 3))
#sum() 총합을 구해준다.
target = np.int64(target) #64비트로 변환해준다.
print(np.sum(target))
print(np.sum(target, axis = 0))
print(np.sum(target, axis = 1))
#prod() 총곱을 구해준다.
print(np.prod(target))
print(np.prod(target, axis = 0))
print(np.prod(target, axis = 1))
#min() 최솟값을 구해준다.
print(np.min(target))
print(np.min(target,axis = 0))
print(np.min(target, axis = 1))
#max() 최댓값을 구해준다.
print(np.max(target))
print(np.max(target,axis = 0))
print(np.max(target, axis = 1))
#mean() 평균값을 구해준다.
print(np.mean(target))
print(np.mean(target, axis = 0))
print(np.mean(target, axis = 1))
#std() 표준편차값을 구해준다.
print(np.std(target))
print(np.std(target, axis = 0))
print(np.std(target, axis = 1))

#마스킹 연산에 대해 알아보자.

print(target % 2 == 0)
print(target[target % 2 == 0]) #짝수인 개수만을 출력해준다.