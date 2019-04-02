import pandas as pd
import numpy as np
'''
df = pd.DataFrame(np.random.rand(5,2), columns = ['A','B'])  #random.rand(5,2) 5행 2열의 랜덤넘버를 출력해줌.
print(df['A']) #SERIES 형태의 A
print(df['B']) #SERIES 형태의 B
print(df['A'] < 0.5) #마스킹 연산으로, 0.5보다 작은 col 'A' 의 값들이 true 그 외에는 false 로 처리됩니다.
print(df[df['A'] < 0.5]) #col 'A'의 값이 0.5보자 작은 행들을 모두 출력해줍니다.
print("***********************************************************")
print(df[(df.A < 0.5) & (df.B < 0.5)]) #col 'A'의 값이 0.5보다 작으며, col 'B'의 값또한 0.5보다 작은 행에 대하여 출력해줍니다.
        #df["A"] == df.A

#위와 같이 마스킹 연산을 통해 조건에 맞는 DATA FRAME 의 ROW값을 출력할 수 있습니다. 

#하지만 더 편한 방법이 있는데요? 바로 query를 사용해 주는 방법입니다.
print("***********************************************************")
print(df.query("A < 0.5 and B < 0.5"))

strFrame1 = pd.DataFrame(np.array(["Dog","Happy","Cat","Sam","Cat","Toby","Pig","Mini", "Cat","Rokcy"]).reshape(5,2), columns = ["Animal","Name"])
print(strFrame1)
print(strFrame1["Animal"].str.contains("C.t")) #str타입이며, Cat이라는 말을 갖고있다면. # 정규화 표현식을 사용할 수도 있다. 정규화 표현식!!
print(strFrame1.Animal.str.contains("(D|d).g")) #str타입을 요런식으로도 찾아낼 수 있다. str을 분석해내는 방법이다.

#사실 아래와같은 방법도 이용이가능합니다.
print(strFrame1["Animal"] == "Dog")
print(type(strFrame1["Animal"] == "Dog")) #SERIES 타입임을 알 수 있습니다.

print(strFrame1[strFrame1.Animal.str.contains("C.t")]) #데이터프레임형을 리턴해줍니다.

#함수로 데이터를 다루고싶을 때 어떻게 해야하는지를 알아봅시다.
#apply
#복잡한 데이터연산이 필요할 때, 사용하면 좋겠습니다.

df = pd.DataFrame(np.arange(5), columns = ["Num"])
print(df)
print(df.apply(lambda x: x**2)) #df의 모든 값들에 대해 람다식을 적용해줄수있습니다.  
print(strFrame1['Animal'].apply(lambda x: "귀여운 " + x)) #문자열도 당연히 가능하겠습니다.
strFrame1['Animal'] = strFrame1.Animal.apply(lambda x: "귀여운" + x)
print(strFrame1)

def preprocess_phone(target):
    char_dic = {
        '공' : 0,
        '영' : 0,
        '하나' : 1,
        '일' : 1,
        '둘' : 2,
        '이' : 2,
        '셋' : 3,
        '삼' : 3,
        '넷' : 4,
        '사' : 4,
        '다섯' : 5,
        '오' : 5,
        '여섯' : 6,
        '육' : 6,
        '일곱' : 7,
        '칠' : 7,
        '여덟' : 8,
        '팔' : 8,
        '아홉' : 9,
        '구' : 9,
    }
    size = len(target)
    ans = ""
    for index in range(0, size):
        if index < size - 1:
            #숫자인지 아닌지
            if target[index] in ['0','1','2','3','4','5','6','7','8','9']:
                ans += target[index]
                continue
            #숫자가 아니라면 2자리수인지
            if target[index : index + 2] in char_dic:
                ans += str(char_dic[target[index : index + 2]])
                index += 1
                continue
            #숫자가 아니라면 1자리 수인지
            if target[index] in char_dic:
                ans += str(char_dic[target[index]])
        else:
            #숫자인지 아닌지
            if target[index] in ['0','1','2','3','4','5','6','7','8','9']:
                ans += target[index]
                continue
            if target[index] in char_dic:
                ans += str(char_dic[target[index]])
    return ans

phoneFrame = pd.DataFrame(columns = ["phone"])
phoneFrame.loc[0] = '010-7499-8045'
phoneFrame.loc[1] = '공일공-일이삼사-1235'
phoneFrame.loc[2] = '010.1234.일이삼오'
phoneFrame.loc[3] = '공1공-1234....1이3오'
print(phoneFrame)
phoneFrame['phone'] = phoneFrame['phone'].apply(preprocess_phone)
print("**********************************************************")
print(phoneFrame)

#apply를 통해서도 데이터값을 바꿀 수 있지만, 만약 정말 replace 값을 대체만 하고싶을 때는 어떻게 해야하는지 알아보겠습니다.

sexDataFrame = pd.DataFrame(["Male", "Male", "Female", "Female", "Male"], columns = ["sex"])
print(sexDataFrame)

sexDataFrame['sex'].replace({"Male" : 0, "Female" : 1}, inplace = True) #사전형식으로 replace 형태를 보내줍니다.. "진짜 원래 값을 바꾸려면, inpluce = true"
print(sexDataFrame)

sexDataFrame['age'] = np.nan #column을 추가해줍니다. 값은 np.nan입니다.
print(sexDataFrame)


#그룹으로 묶어내는 경우에 대해 알아보겠습니다. #간단한 집계를 넘어서서 조건부로 집계를 하고싶은경우에 해당하며, 사용할 수 있습니다.
groupDataFrame = pd.DataFrame({'key' : ['A','B','C','A','B','C'], 'data1' : [1,2,3,1,2,3], 'data2' : np.random.randint(0, 6, size = 6)}) #사전으로 만들 수있죠.
print(groupDataFrame)

print(groupDataFrame.groupby('key')['data1'].sum()) #groupby로 key값으로 묶은 후에, sum을통해서 같은 키값인 경우에만 data들을 더해줍니다.
print(groupDataFrame.groupby(['key','data1']).sum()) #list타입으로 여러 col값을 사용할 수 도 있습니다.

#위처럼 sum, mean std와 같이 한번에 한연산만 groupby로 할 수도 있지만, aggregate를 사용하면 여러 연산을 한번에 할 수 있다는 장점이있습니다. 
print(groupDataFrame.groupby('key').aggregate(['sum','min',np.median, max])) #역시 인자값을 리스트로 보내줍니다.
print(groupDataFrame.groupby('key').aggregate({'data1' : 'min', 'data2' : max})) #dic방식으로 각각의 col 마다 원하는 연산을 시킬수도 있습니다.

#fillter에 대해서 알아보겠습니다 groupby로 묶은 후에, 그룹 속성을 기준으로 데이터를 필터링해줍니다.
#예를들어 key값으로 묶은 후에, 그 그룹에 대해서 평균값이 3보다 큰 값들만 추려내고 싶으면 어떻게 해야할까요?
print(groupDataFrame.groupby('key').filter(lambda x : x['data2'].mean() > 3)) #그 그룹내에 값들을 추려줍니다. #그룹 속성을 기준으로 필터링을 해줍니다.

#group_by로 묶인 데이터에 대해서 함수를 적용할 수 도있는데요. apply 입니다.
print(groupDataFrame.groupby('key').apply(lambda x : x.max() - x.min()))



groupDataFrame = pd.DataFrame({'key' : ['A','B','C','A','B','C'], 'data1' : [1,2,3,1,2,3], 'data2' : np.random.randint(0, 6, size = 6)}) #사전으로 만들 수있죠.
print(groupDataFrame)

#그룹바이 연산은 묶기만합니다. 묶고 가지고만 있습니다.
print("**********************************************************************")
print(groupDataFrame.groupby('key')['data1','data2'].sum())  #key값으로 묶은 그룹에 대해, data1과 , data2에 대해, sum을 적용하는 모습입니다.
print("**********************************************************************")
print(groupDataFrame.groupby(['key','data1']).sum()) #key값과 data1값을 기준으로 그룹을 묶고, 그 묶인 애들에 대해 연산을 해줍니다.

print(groupDataFrame[groupDataFrame['key'] == 'A'])
print(groupDataFrame.query("key == 'A'")) #찾는 대상 비교대상에 대해 ' '해줍니다. #마스킹연산이나 쿼리연산을 통해, 같은 값들을 묶은 DaTAFrame을 만들 수 있기 때문에, groupby로는 이 역할까지 안바래도 됩니다.index

#위처럼 연산을 한번이 아닌, 여러번 멀티로 하고싶을 때는 

print(groupDataFrame.groupby('key').aggregate([min, max, np.mean, np.std])) 
#원하는 연산을 딕셔너리로 보내서도 할 수 있습니다.

print(groupDataFrame.groupby('key')['data1'].aggregate([min, max, np.mean, np.std])['max']) #data1에 대해서만 수행을 해준모습입니다., max에 대해 series값을 가져올 수 있습니다.
print(groupDataFrame.groupby('key').filter(lambda x : x['data2'].mean() > 1)) #group으로 묶은것들에 대해서 적용 그룹의 평균이 1보다 크면 출력이됌. 그룹을 기준으로 필터링을 해줍니다.
print("*********************************************************************")
print(groupDataFrame)
print("*********************************************************************")
print(groupDataFrame.groupby('key')['data2'].apply(lambda group : group.max() - group.min())) #group은 series입니다.
print(type(groupDataFrame.groupby('key')['data2']))

print("*****************************************************************************************")

univ_list = ['경북대학교','부산대학교','충북대학교','충남대학교','서울대학교','숭실대학교','성균관대학교','가톨릭대학교','수원대학교','인하대학교']
univ_city = ['경북','부산','충북','충남', '서울','서울','서울','경기','경기','인천','제주도']
univDataFrame = pd.DataFrame(columns = ['시도', '학교명'])

for index in range(0, len(univ_list)):
    univDataFrame.loc[index] = [univ_city[index], univ_list[index]]
print(univDataFrame)

print(univDataFrame['시도'].values)

for city in univ_city:
    print("********************************************")
    if city in univDataFrame['시도'].values: #'values' = 키값이 아닌 밸류값입니다. series의 key값은 인덱스임으로, 시도명인 밸류를 봐줍니다.
        print(univDataFrame.groupby('시도').get_group(city))
    else:
        print(city + " 내에 학교에 대한 데이터가 없습니다.")
    print("********************************************")
print(univDataFrame.head()) #default로 5개를 가져오게됩니다.
cities = ['경북','부산','충북','충남','서울','경기','인천','제주도','전남','전북','경남','강원']
for city in cities:
    if city not in univDataFrame['시도'].values:
        print(city + " 내에 학교에 대한 데이터가 존재하지 않습니다.")
    else:
        print(city + " 내의 대학의 수 : " + str(len(univDataFrame.groupby('시도').get_group(city)))) #get_group을 통해 그 그룹안에 있는 도시들만 파악
'''
#groupby를 통해 그룹으로 묶어서 진행할 수 도 있습니다.
"""
class student():
    def __init__(self, grade, group, num, avg):
        self.grade = grade
        self.group = group
        self.num = num
        self.avg = avg
    def getInfo(self):
        return self.grade, self.group, self.num, self.avg
classDataFrame = pd.DataFrame(columns = ['학년', '반', '번호', '평균성적'])
print(classDataFrame)
num_checker = [list() for i in range(0, 8)]
for i in range(0, 100):
    tmp = np.random.randint(1, 7)
    num_checker[tmp].append(1)
    tmpStudent = student(6,tmp, len(num_checker[tmp]), np.random.randint(40, 101))
    classDataFrame.loc[i] = tmpStudent.getInfo()

print(classDataFrame)
print(classDataFrame.sort_values(['반','번호'])) #2가지의 기준으로 sort

#각 반 학생의 수와 평균 점수를 출력하시오.

for index in range(1, 7):
    tmp = classDataFrame.groupby('반').get_group(index)
    print(str(index) + "반의 학생 수 : ", len(tmp), "평균 점수 : ", tmp['평균성적'].mean())

#총 학생의 수와 평균 점수를 출력하시오.
print("***************************************************************************")
print("총 학생의 수 : ", len(classDataFrame), "총 학생 평균 점수 :", classDataFrame['평균성적'].mean())


"""# randn은 해당 모양의 랜덤값을반환합니다.
df = pd.DataFrame(np.random.randn(4, 2), index = [['A','A','B','B'],[1, 2, 1, 2]], columns = ['data1','data2'])

print(df)
