import pandas as pd
import numpy as np

#MultiIndex 
df = pd.DataFrame(
    np.random.randn(4, 2),
    index = [['A','A','B','B'], ['1','2','1','2']],
    columns = ['data1', 'data2']
)

print(df)
#MultiColumn도 가능합니다.

df = pd.DataFrame(
    np.random.randn(4,4),
    columns = [['A','A','B','B'],['1','2','1','2']]
)

print(df)
print(df['A'])
print(type(df['A']))
print(df['A']['1'])
print(type(df['A']['1']))
print(df[''])