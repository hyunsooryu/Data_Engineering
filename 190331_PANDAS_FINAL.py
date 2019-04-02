'''
2019:03:31 작성자 : 류현수
PANDAS 내용 정리 : ELICE IO
'''
import pandas as pd
import numpy as np 

data = pd.Series([1,2,3,4]) #default로 index 에는 0, 1, 2, 3 이 들어감을 알 수 있다.
print(data)
#판다스의 시리즈는 numpy_array가 보강된 형태이다. Data와 index를 가지고 있다. 
#SERIES는 딕셔너리로도 만들 수 있다.
population_dic = {
    'korea' : 5180,
    'japan' : 12718,
    'china' : 141500,
    'usa' : 32676 
}

population_series = pd.Series(population_dic)
print(population_series)

#DATA FRAME 은 여러개의 SERIES가 모여서 행과 열을 이루는 데이터입니다. SERIEZ는 NUMPY_ARRAY로 되어있다.
gdp_dic = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000
}

gdp_series = pd.Series(gdp_dic)
#데이터 프레임을 DIC형태로 만들어준다.
country = pd.DataFrame({
    'population' : population_series,
    'gdp' : gdp_series
})

print(country)

country_another_way = pd.DataFrame(np.array([5180, 159320000, 12718, 516700000, 141500, 1409250000, 32676, 2041280000]).reshape(4, 2), columns = ['popuation', 'gdp'])
print(country_another_way)

print(country['gdp']) #SERIES형태의 값을 반환함을 알 수 있다.
print(country_another_way['gdp'])

#SERIES 도 넘파이 연산자를 사용할 수 있다.

country['gdp_per_capita'] = country['gdp'] / country['population'] #데이터프레임에 column을 추가하고 있다. 1인당 쥐디피 결과가 나오게 된다. 
country['FIFA_RANKING'] = pd.Series({
    'korea' : 25,
    'japan' : 42,
    'china' : 192,
    'usa' : 15
})

print(country)

#DATAFRAME의 indexing 과 slicing에 대해 알아보도록 하겠습니다.

#명시적 인덱스를 참조하는 방법 loc->로 읽어냅니다.
print(country.loc['korea','population']) #index를 기준으로한 시리즈 데이터를 리턴합니다.
print(country.loc['korea' : 'japan',:'FIFA_RANKING']) #= country.loc['korea' : 'japan'][:'FIFA_RANKING']

#파이썬 스타일의 정수인덱싱, 슬라이싱을 가능하게하는 iloc를 알아보겠습니다.
print(country.iloc[0,0]) 
print(country.iloc[0: 2, :])

#두개다 많이 사용하지만, 개인적으로 명시적인 LOC 스타일을 더 많이 사용하곤 합니다..

#####데이터 프레임에 새 데이터를 추가하고 수정하는 방법에 대해 알아보겠습니다.

dataframe = pd.DataFrame(columns = ['이름', '나이', '주소'])
dataframe.loc[0] = ['류현수', '27', '경기도 부천시 소사본3동 두산아파트 101동 1504호'] #리스트로 추가하는 방법입니다.
dataframe.loc[1] = {'이름' : '황인후', '나이' : '27', '주소' : '서울시 오류 교도소 101번 사형수반'} #딕셔너리로 추가하는 방법입니다.
dataframe.loc[0, '나이'] = '28'
print(dataframe)
dataframe['전화번호'] = np.nan
print(dataframe)
print(dataframe["이름"]) #하나이니까 SERIES 타입으로 리턴해줍니다.
print(dataframe[["이름", "주소"]]) #하나 초과이니까 DATEFRAME으로 리턴해줍니다. 리스트니까요.
print(dataframe.isnull()) #데이터프레임 내에서 비어있는 곳에 대해 TRUE
print(dataframe.notnull()) #데이터프레임 내에서 채워져있는 곳에 대해 TRUE

dataframe.dropna()
print(dataframe) 
dataframe['전화번호'] = dataframe['전화번호'].fillna('전화번호 없음') #fillna를 사용해줍니다.
print(dataframe)

#SERIES끼리의 연산에 대해 알아봅시다.

A_SERIES = pd.Series([2, 4, 6], index = [0,1,2]) #리스트형태로 선언
B_SERIES = pd.Series({ #딕셔너리 형태로도 가능합니다.
    1 : 1,
    2 : 3,
    3 : 5
})

print(A_SERIES + B_SERIES) #연산결과에 0과 3에 NAN이 생기게됩니다. 이럴 때 NAN을 없애주는 방법이있습니다.
print(A_SERIES.add(B_SERIES, fill_value = 0)) #fill_value를 이용해서, NAN인 값들을 모두 채워주게 됩니다.

#DataFrame은 SERIES데이터들로 이루어져있기 때문에, SERIES연산이 가능해집니다.

#DataFrame의 연산입니다. add sub mul div 가 모두 가능합니다.
A_dataFrame = pd.DataFrame(np.random.randint(10, size = (2, 2)), columns = ['A', 'B'])
B_dataFrame = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns = ['B','A','C']) #DataFrame의 인자값으로 리스트, np.array등이 모두 가능하다.
print(A_dataFrame)
print(B_dataFrame)

print(A_dataFrame.mul(B_dataFrame, fill_value = 1)) #Nan값들은 모두 1로 대체한다는 연산입니다. 

new_data = {
    'A': [i + 5 for i in range(3)], #리스트타입
    'B': [i ** 2 for i in range(3)] #리스트타입
}

print(type(new_data))
#데이터프레임에서도 기존에 사용했었던, 집계함수들을 이용할 수 있다. ㅌ
df = pd.DataFrame(new_data)
print(df)
print(type(df))
print(type(df['A'])) #SERIES타입으로 자동 변환되어서 들어간것을 볼수있다.

print(df['A'].sum())
print(df.sum())
print(df.mean())
#sorting에 대해서도 익혀봅시다.
print(country)
print(country.sort_values('FIFA_RANKING', ascending = False))
print(country.sort_values(['population', 'gdp', 'gdp_per_capita'], ascending = False))
print("********************************************************")
country.loc['korea', 'FIFA_RANKING'] = 76 #한국의 피파랭킹을 바꾸고 싶을 때는 이렇게 한다.
print("********************************************************")
#GDP가 2041280000 위인 나라의 FIFA_RANKING을 바꾸고싶을때는?
print(type(country.query('gdp == 2041280000')))
print(country)
