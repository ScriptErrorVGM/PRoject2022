from asyncio.windows_events import NULL
import numpy as np 
import pandas as pd 
import math

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

# nuber 1

df = pd.DataFrame(data)
#print(df[1])
#df.columns = ['ru_name','en_name','class','cheer']
df[3] = df[3].astype(float)
#print(df[1])

assert type(df) == pd.core.frame.DataFrame, "Объект df не является датафреймом"
assert df.shape == (5, 4), "Неверное число строк и столбцов"
assert df.dtypes.values[-1] == float, "Последний столбец не имеет тип float"

# number 2


N = len(df)

assert N == 5, "Неверный ответ"

# number 3

dff = df
dff[3] = dff[3].fillna('None')
cn = len(dff[dff[3] != 'None'])

assert cn == 4, "Неверный ответ"

# number 4


g = df[1][2]

assert g == 'Dale', "Неверный ответ"

# number 5


df1 = df.iloc[1:4,0:3]

assert df1.shape == (3, 3), "Неверное число строк и столбцов"
assert df1[1].values[-2] == "Dale", "Выбраны не те строки или столбцы"

# number 6



df.columns = ['ru_name','en_name','class','cheer']

assert df1.shape == (3,3)
assert df1[1].values[-2] == 'Dale', 'Выбраны не те строки или столбцы'

# nuber 7

df.insert('logcheer', np.log(df['cheer']))

print(df)

  
