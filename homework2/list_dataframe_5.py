from asyncio.windows_events import NULL
import numpy as np 
import pandas as pd 

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

df = pd.DataFrame(data)
#print(df[1])
#print(df)
#df.columns = ['ru_name','en_name','class','cheer']
# number 5

df1 = df[[2]][1:][:3]
print(df1)
#print(df1[1])
#assert df1.shape == (3, 3), "Неверное число строк и столбцов"
#assert df1[1].values[-2] == "Dale", "Выбраны не те строки или столбцы"