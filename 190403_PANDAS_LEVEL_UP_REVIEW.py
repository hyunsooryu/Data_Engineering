import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randint(1, 7, (5, 2)), columns = ['A', 'B'])
print(df)
#SERIES TYPE OF A
print(df['A'])
print(type(df['A']))
#SERIRS TYPE OF B
print(df['B'])
print(type(df['B']))

#Masking is possible in DataFrame like numpy.

print(df[df['A'] > 3]) 

#what about there are lots of conditions?

print(df[(df['A'] > 3) & (df['B'] > 1)])

#above it, it is not easy if there are more than 2 conditions.
#so we can use q Query system at here to get Masking Results.

print(df.query('A > 3 and B > 2'))

strFrame1 = pd.DataFrame(np.array(["Dog","Happy","Cat","Sam","Cat","Toby","Pig","Mini", "Cat","Rokcy"]).reshape(5,2), columns = ["Animal","Name"], index = ['A','B','C','D','E'])

print(strFrame1)
#find which name = toby

#get index ======== index[0]!!!!!!!!!!!!!!
print(strFrame1.query('Name == "Mini"'))
print(strFrame1.query('Name == "Mini"').index[0])
loc_key = strFrame1.query('Name == "Mini"').index[0]
print(loc_key)
strFrame1.loc[loc_key, "Name"] = "Dasol"
print(strFrame1)
#Finding the Name and catch the index_num with index[0] and change it

print(strFrame1['Animal'])
print(strFrame1[strFrame1.Animal.str.contains('C..?')]['Name']) #str.contains can use a R Type
print(strFrame1[strFrame1.Animal.str.contains('D.g')])

df = pd.DataFrame(np.arange(5), columns = ["NUM"])
print(df)

print(df.apply(lambda x : x**2)) #Each of values in NUM is applied by lambda function

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
phoneFrame.loc[4] = '010에 7499에 8045입니다.'
phoneFrame.loc[5] = "010-칠4구구-팔공사5"
phoneFrame.loc[6] = "010-3236-7오칠팔"
print(phoneFrame)
phoneFrame['phone'] = phoneFrame['phone'].apply(preprocess_phone)
print("**********************************************************")
print(phoneFrame)
#apply can Use with a Function but, If we just want to replace it with another values?

#the answer is replace.

sexDataFrame = pd.DataFrame({
    'sex' : ['M','M','F','M'] #if push it with a dic, columns key values values
})
#use dic for replace
sexDataFrame['sex'].replace({'M' : 'MAN', 'F' : 'FEMALE'}, inplace = True)
print(sexDataFrame)

sexDataFrame.loc[0, 'age'] = '17'
print(sexDataFrame) 
print(sexDataFrame.fillna("no information")) 

groupDataFrame = pd.DataFrame({'key' : ['A','B','C','A','B','C'], 'data1' : [1,2,3,1,2,3], 'data2' : np.random.randint(0, 6, size = 6)})
print(groupDataFrame)
#group_by -> getGroup
print(groupDataFrame.groupby('key').get_group('A'))
print(groupDataFrame.groupby('key').get_group('B'))
print(groupDataFrame.groupby('key').get_group('C'))
#query - > masking
print(groupDataFrame.query('key == "A"'))
print(groupDataFrame.query('key == "B"'))
print(groupDataFrame.query('key == "C"'))

print(groupDataFrame.groupby('key')['data1'].sum()['A']) #그룹바이입니다.index
#그룹으로 묶어서 한번에 여러연산을 하고싶을때에는 aggregate을 사용해주면 좋습니다.

print(groupDataFrame.groupby('key').aggregate([np.max, np.min, np.mean, np.std, np.median]))
print(groupDataFrame.groupby('key').apply(lambda x : x.max() - x.min()))
print(groupDataFrame.groupby('key').filter(lambda x : x['data2'].mean() > 3 and x['data1'].mean() > 0.2))

class student():
    def __init__(self, grade, group, num, avg, s_num):
        self.grade = grade
        self.group = group
        self.num = num
        self.avg = avg
        self.s_num = s_num
    
    def getInfo(self):
        return [self.grade, self.group, self.num, self.avg, self.s_num]
class_num = [0] * 11
classDataFrame = pd.DataFrame(columns = ['학년','반','번호','평균성적', '학년번호'])
for i in range(0, 400):
    tmp = np.random.randint(1, 11)
    class_num[tmp] += 1
    tmpStudent = student(6, tmp, class_num[tmp], np.random.randint(40, 101), i)
    classDataFrame.loc[i] = tmpStudent.getInfo()


classDataFrame['전교석차'] = np.nan

sorted_data = classDataFrame.sort_values(['평균성적', '학년번호'], ascending = [False, True]).loc[:, '평균성적' : '학년번호'] #series
#전교등수 구현
print(sorted_data)

student_rank = 1
change_rank = 1
now_score = sorted_data.iloc[0, 0]
print("현재 최고점 점수 :", now_score)
n = 0
while n < 400:
    score = sorted_data.iloc[n, 0]    
    no = sorted_data.iloc[n, 1]
    if score == now_score:
        target_index = classDataFrame[classDataFrame['학년번호'] == no].index[0]
        #print(target_index)
        classDataFrame.loc[target_index, "전교석차"] = student_rank
    else:
        target_index = classDataFrame[classDataFrame['학년번호'] == no].index[0]
        classDataFrame.loc[target_index, "전교석차"] = change_rank
        student_rank = change_rank
        now_score = score
    n += 1
    change_rank += 1
classDataFrame['전교석차'] = classDataFrame['전교석차'].astype(int)
print(classDataFrame.sort_values('전교석차'))

