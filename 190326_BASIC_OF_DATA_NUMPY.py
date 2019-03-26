import numpy as np
'''
A = [[0 for x in range(10)] for x in range(10)]

파이썬 리스트와 다르게 넘파이 어레이는 단일 타입으로 구성됩니다.

print(A)

for i in range(10):
    for j in range(10):
        print(A[i][j], end = " ")
    print("\n")

arr = np.array([1,2,3,4,5], dtype = "float")
print(arr[2])

array = np.zeros(10, dtype = int)
print(array)
array = np.ones((3,5), dtype = int)
print(array)
array = np.arange(0,20,2)
print(array)
array = np.linspace(0, 1, 5)
print(array)
array = np.random.random((2, 2))  #shape 2 * 2로 배열을 만들때 씁니다.
print(array)
array = np.random.normal(0, 1, (2,2)) #평균이 0이고, 표준편차가 1인 데이터를 2 * 2행렬로 뽑아주세요.
print(array)
array = np.random.randint(0, 10, (2, 2)) #0부터 10까지의 정수를 2 * 2배열 형태로 뽑아줌.
print(array)
x2 = np.random.randint(5, size = (3, 4))
#CONPONENT FINDING
print(x2) #array
print(x2.ndim) #dimension
print(x2.shape) # row col
print(x2.size) # size
print(x2.dtype) # dtype

#INDEXING
x = np.arange(7)
print(x[3])
#print(x[7]) #index error
x[0] = 10 #data replace

#SLICING SAME AS PYTHON LIST
print(x[1 : 4])
print(x[1:])
print(x[:4])
print(x[::2])

print("2차원 array")
matrix = np.arange(1, 16).reshape(3, 5)
#1부터 15까지 들어있는 (3, 5)짜리 배열을 만듬.
print(matrix.dtype)
print(matrix.ndim)
print(matrix.shape)
print(matrix.size)
print(matrix.dtype)
print(matrix[2,3])
print(matrix[0:2, 1:4])

data = "hi brother"
#문자열에 대해 이렇게 받는것도 가능합니다.
string_1, string_2 = data.split(" ")
print(string_1)
print(string_2)
'''
'''
#reshape
x = np.arange(16).reshape(4,4)
y = np.arange(16).reshape(4,4)
print(y)
print(x)
#concatenate
z1 = np.concatenate([x, y], axis = 0) #row 를 기준으로 아래다가 붙여준다.  붙일 수 없는 사이즈. 즉 정확히 매칭되지않으면 붙여지지않는다.
z2 = np.concatenate([x, y], axis = 1) #col 를 기준으로 옆에다가 붙여준다.  붙일 수 없는 사이즈. 즉 정확히 매칭되지않으면 붙여지지 않는다.
print(z1)
print(z2)
#split
upper, lower = np.split(z1, [4], axis = 0)

print(upper)
print(lower)

lefter, righter = np.split(z2, [4], axis = 1)
print(lefter)
print(righter)
'''
#기존에 만약 값을 더하고 싶엇다면, 리스트에 경우 반복적으로 루프를 돌며 아래와 같이 더해줬어야한다. 
def addFiveToArray(values):
    output = np.empty(len(values), dtype = int) #int형으로 dtype을 선언해준다.
    #print(output)
    for i in range(len(values)):
        output[i] = values[i] + 5
    return output

values = np.random.randint(1, 10, size = 5)
print(values)
print(addFiveToArray(values))
#넘파이를 사용한다면 얘기가 다르다. 넘파이는 array +, - , *, / 에 대한 기본 연산을 지원해준다.
'''
print(values + 5)
print(values - 5)
print(values * 5)
print(values / 5)

A = np.array([[2,2],[2,2]])
B = np.array([[3,4],[5,6]])
print(A + B)
print(A - B)
print(A * B)
print(A)
print(B)
print(A / B)
'''
'''
#BROADCASTING shape이 다른 array끼리의 연산
print(np.arange(3).reshape(3, 1) + np.arange(3)) #reshape할때 값을 튜플로줘도되고 그냥ㄷ줘도되는군
'''
#집계함수
A = np.arange(8).reshape((2, 4))
print(np.sum(A))
axis_0_sum = np.sum(A, axis = 0)
axis_1_sum = np.sum(A, axis = 1)
print(axis_0_sum)
print(axis_1_sum)
A = np.arange(1, 20, 2)
#마스킹 연산
print(A < 3) 
print(A > 3)
print(A & 1)
print(A[A > 10]) #인덱스처럼 true 와 false 가 담긴 인덱스를 넣어준다면, true인 값만 출력하게됩니다.