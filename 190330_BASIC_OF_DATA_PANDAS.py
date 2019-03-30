import pandas as pd
import numpy as np
#Series를 만들어 내는 방법_1
data = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print(data)
print(type(data)) #pandas.core.series.Series임을 알 수있다.
#Series를 만들어 내는 방법_2 dictionary객체를 이용해서도 만들어 낼 수 있다.
dic = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
data = pd.Series(dic)
print(data)

population_dic = {
    'korea' : 5180,
    'japan' : 12718,
    'china' : 141500,
    'usa' : 32676
}

population = pd.Series(population_dic) #인구 자료 dic을 이용한 population Series 객체 생성
print(population)

#DataFrame에 대해 알아보자.
#DataFrame이란 여러개의 Series가 모여서 행과 열을 이룬 데이터입니다.

gdp_dic = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}

gdp = pd.Series(gdp_dic)
print(gdp) #gdp 자료 dic 을 이용한 gdp Series 객체 생성

country = pd.DataFrame({ #dictionary타입으로 시리즈들을 모아 하나의 데이터 프레임으로 만들어 낸다.
    'population' : population,
    'gdp' : gdp
})

#데이터프레임의 index값 알아보기
print(country.index) #한국 일본 중국 미국
#데이터프레임의 columns값 알아보기
print(country.columns) #인구 gdp

print(type(country['gdp'])) #pandas.Series객체임을 알수있다.


#데이터프레임의 시리즈도, numpy연산처럼 연산을 할 수 있다.
#1인당 gdp를 만들어보겠습니다.
gdp_per_capita = country['gdp'] / country['population'] #각각의 시리즈를 연산해줍니다.
country['gdp_per_capita'] = gdp_per_capita #연산결과를 다시 데이터 프레임의 시리즈 형태로 넣어줍니다.
print(country)

#만든 데이터 프레임은 엑셀 타입, 혹은 csv 파일로 저장할 수 있다.
#country.to_csv("./country_2019_03_30.csv")
#country.to_excel("country_2019_03_03.xlsx")

#엑셀파일이나, csv파일을 데이터 프레임의 형태로 불러올 수 있다.
#read_country_csv = pd.read_csv("./country_2019_03_30.csv")
#read_country_excel = pd.read_excel("country_2019_03_03.xlsx")

#명시적으로 인덱스를 참조하는 인덱싱 / 슬라이싱을 알아보자.
#인덱싱 입니다.
#1. loc
print(country.index)
print(country.columns)
print(country.loc['korea'])
print(country.loc['korea' : 'usa', :'population']) #loc에서는 numpy와는 다르게 뒤에 값을 모두 포함한 결과를 리턴해준다.

#2. iloc 파이썬 스타일의 정수 인덱스 인덱싱 / 슬라이싱 입니다. 파이썬 스타일이기 때문에 : 뒤에값을 배제한 결과를 리턴해줍니다.
print(country.iloc[0])
print(country.iloc[1:3, :2])
#3. ix[]는 지금은 지원이 중단되었습니다. 

#4. DataFrame 새 데이터 추가 및 수정하는 방법
#컬럼을 만들어주는 방법.
dataframe = pd.DataFrame(columns = ['이름','나이','주소'])
#print(dataframe)
#리스트를 활용해 넣어줍니다.
dataframe.loc[0] = ['류현수','28','서울']
#딕셔너리를 활용해 넣어줍니다.
dataframe.loc[1] = {'이름':'황인후','나이':'28','주소':'부천'}
dataframe.loc[1, '주소'] = '서울'
#print(dataframe)
#새로운 컬럼을 추가해주는 방법에 대해 알아봅시다.
dataframe['전화번호'] = np.nan
dataframe.loc[0,'전화번호'] = '01074998045'
dataframe.loc[1, '전화번호'] = '01032367578'
#컬럼을 선택하는 방법
print(dataframe["이름"]) #시리즈의 형태로 리턴해준다.
print(dataframe[['이름','전화번호']]) #새로운 데이터프레임의 형태로 리턴해준다.