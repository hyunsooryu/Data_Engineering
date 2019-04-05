import pandas as pd
import numpy as np

df = pd.DataFrame(columns = ['survived','pclass','sex','age','sibsp','parch','fare','embarked','class','who'])
print(df)
df.loc[0] = [0.0,3,'male',22.0,1,0,7.2500,'S','Third','man']
df.loc[1] = [1.0,1,'female',38.0,1,0,71.2833,'C','First','woman']
df.loc[2] = [1.0,3,'female',26.0,0,0,7.9250,'S','Third','woman']
df.loc[3] = [0.0,1,'female',35.0,1,0,53.1000,'S','First','woman']
df.loc[4] = [0.0,3,'male',35.0,1,0,8.0500,'S','Third','man']
print(df)

#what is pivot_table??????
#인텍스값 행 인덱스 key값 열 인덱스 라벨링 값 value 분석할 데이터
#타이타닉 데이터에서, 성별과 좌석별로의 생존률을 구하고 싶다.

#원하는 새 데이터프레임을 가져오기

df_15 = df[['survived','sex','class']] #리스트의 형태로 원하는것만 가져올 수있다.
#만약 loc도 한정해야한다면.
print(df_15)
df_15 = df.loc[1 : 3, ['survived','sex','class']] #indexing
print(df_15)

print(type(df['survived'][0]))#int type cant do with aggfunc. only float!
table = df.pivot_table(index = "sex", columns= 'class', values= 'survived', aggfunc= np.mean)
print(table)

practice_table = pd.read_csv("./the_pied_piper_of_hamelin.csv")
print(practice_table)
practice_table = practice_table.query('구분 == "Child"')
#일자별로 남자 어린이와 여자 어린이를 출력해라.
#index = 일자 columns = '성별' values = 나이 
table = practice_table.pivot_table(index = '일차', columns = '성별', values= '나이')
print(table)
print(practice_table.groupby('일차')['나이'].mean()) #일차별로 묶어서 그 나이들의 평균을 구했다.

#한번이라도 참가한 아이들의 이름을 출력해보자.

print(practice_table['이름'])
#1일, 2일등 여러일에 참여했을수도있다. #참여한 사람의 이름을 한번만 뽑고싶다.
for name in practice_table['이름'].unique():
    print(name) #아이들의 이름을 중복없이 뽑아주었습니다..



