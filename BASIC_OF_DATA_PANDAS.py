import pandas as pd
#pandas의 Series는 Numpy array가 보강된 형태의 DATA와 INDEX를 가지고 있는 데이터 형식입니다.
#pandas는 인덱스를 가지고 있게된다.
#아래와 같이 default는 0,1,2,3
data = pd.Series([1,2,3,4])
print(data)
data = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print(data)
#위와같이 index를 매겨줄 수 도 있다.
population_dic = {
    'korea' : 5180,
    'japan' : 12718,
    'china' : 141500,
    'usa' : 32676
}
#DIC도 넣어버릴수가있다.
population = pd.Series(population_dic)

#DataFrame Serisz들을 열로 삼는 강력한도구이다.
gdp_dict = {
    'korea' : 169320000,
    'japan' : 516700000,
    'china' : 1409250000,
    'usa' : 2041280000
}

gdp = pd.Series(gdp_dict)
country = pd.DataFrame({
    'population' : population,
    'gdp' : gdp
})
print(country.index) #행 주체들
print(country.columns) # 열 주제들
print(country)
print(country['gdp']['korea']) #값찾기
print(type(country['gdp'])) #seriez 객체임을 알 수 있다.

#series는 넘파이 array의 업그레이드 버전이라고 생각하면 쉽다.
#series는 numpy array 처럼 연산자를 쓸 수 있다.
gdp_per_capita = country['gdp'] / country['population']
country['gdp_per_capita'] = gdp_per_capita # 1인당 gdp라고합니다.
#series객체로 만들어지며 dtype = float이다. 
#요거를 그대로 country에다가 gdp_per_capita를 고대로 넣어준다.
print(country)
country.to_csv("./country.csv") #COMMA SEPARATE VALUE로 저장할 수 있습니다.
country.to_excel("country.xlsx") #EXCEL로도 저장이 가능합니다.
