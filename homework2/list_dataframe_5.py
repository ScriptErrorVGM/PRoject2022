# This Python file uses the following encoding: utf-8
import os, sys
from asyncio.windows_events import NULL
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd 
import math
import seaborn as sns



# number 1
dff = pd.read_csv('polit.csv')
polit = pd.DataFrame(dff)
polit = polit.dropna()
polit = polit.reset_index(drop = True)

assert polit.shape == (135, 13), "Проверьте, сохранились ли изменения в polit"

# number 2

not_free = pd.DataFrame(polit[polit['fh09'] > 5])


assert not_free.shape == (30, 13), "Неверное число строк или столбцов" 
assert not_free.iloc[3, 9] == 0, "Неверный датафрейм" 
assert not_free.iloc[19, 1] == 'Mauritania', "Неверный датафрейм"

# number 3

af_w = pd.DataFrame(polit.loc[(polit['fparl08'] > 30) & (polit['afri'] == 1)])

assert af_w.shape == (6, 13), "Неверное число строк или столбцов" 
assert af_w.iloc[3, 5] == 33.92, "Неверный датафрейм" 
assert af_w.iloc[5, 7] == 0, "Неверный датафрейм"

# number 4

la_dem = pd.DataFrame(polit.loc[((polit['afri'] == 1) & (polit['polity09'] >= 8)) | 
(polit['lati'] == 1) & (polit['polity09'] >= 8)])

#print(la_dem)
assert la_dem.shape == (18, 13), "Неверное число строк или столбцов" 
assert la_dem.iloc[3, 5] == 12.66, "Неверный датафрейм" 
assert la_dem.iloc[5, 7] == 1, "Неверный датафрейм"

# number 5

polit['corr_round'] =  polit['corr0509'].round(2)
# if two multiples are equally close, rounding is done toward the even choice 
# (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2)

assert round(polit["corr_round"].sum()) == -14.0, "Ошибка в столбце corr_round" 
assert polit["corr_round"].max() == 2.38, "Ошибка в столбце corr_round"

# number 6

for i in range(len(polit)) :
        if (polit['fh09'][i] >= 1.0) & (polit['fh09'][i] <= 2.5) :
                polit.loc[i,'fh_status'] = 'free'
        elif (polit['fh09'][i] >= 3.0) & (polit['fh09'][i] <= 5.0) :
                polit.loc[i,'fh_status'] = 'partly free'
        elif (polit['fh09'][i] >= 5.5) & (polit['fh09'][i] <= 7.0) :
                polit.loc[i,'fh_status'] = 'not free'


assert polit["fh_status"].value_counts().values[0] == 57, "Неверные значения в столбце" 
assert polit["fh_status"].value_counts().values[1] == 48, "Неверные значения в столбце" 
assert polit["fh_status"].value_counts().values[2] == 30, "Неверные значения в столбце" 
assert polit["fh_status"].values[3] == 'free', "Неверные значения в столбце" 
assert polit["fh_status"].values[4] == 'partly free', "Неверные значения в столбце" 
assert polit["fh_status"].values[134] == 'not free', "Неверные значения в столбце"

# number 7

temp = polit.groupby(by = ['fh_status'])
print(temp)
min_gini = polit.groupby(['fh_status']).min()
max_gini = polit.groupby(['fh_status']).max()
mid_gini = polit.groupby(['fh_status']).median()

print('Max index gini :', max_gini['gini'].max())
print('Min index gini :', min_gini['gini'].max())
print('Mid index gini :', mid_gini['gini'].median())
