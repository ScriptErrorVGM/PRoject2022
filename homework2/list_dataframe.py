from asyncio.windows_events import NULL
import numpy as np 
import pandas as pd 

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

# nuber 1

df = pd.DataFrame(data)
print(df[1])
df.columns = ['ru_name','en_name','class','cheer']
df['cheer'] = df['cheer'].astype(float)
#print(df[1])

assert type(df) == pd.core.frame.DataFrame, "Объект df не является датафреймом"
assert df.shape == (5, 4), "Неверное число строк и столбцов"
assert df.dtypes.values[-1] == float, "Последний столбец не имеет тип float"

# number 2


N = len(df)

assert N == 5, "Неверный ответ"

# number 3

dff = df
dff['cheer'] = dff['cheer'].fillna('None')
cn = len(dff[dff.cheer != 'None'])

assert cn == 4, "Неверный ответ"

# number 4

g = df['en_name'][2]

assert g == 'Dale', "Неверный ответ"


