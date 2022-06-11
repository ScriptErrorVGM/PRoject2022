from itertools import count
import numpy as np 
import pandas as pd 
import scipy.stats as sps

df = pd.DataFrame({     'время приема' : sps.randint(low=8, high=16).rvs(size=24),
                        'врач' : ['Андрей', 'Сергей', 'Ирина'] * 8,
                        'пациент' : ['Владимир','Степан','Алина','Георгий'] * 6,
                        'поставленный диагноз' : ['Простуда', 'Отравление', 'Простуда',
                                    'Волнения', 'Грипп', 'Простуда'] * 4,    
                        'назначение' : ['Медикаменты','Стационар','Медикаменты','Отдых'] * 6,    
                        'Продолжительность' : sps.randint(low=1, high=6).rvs(size=24) })
                        
print(df)


df2 = pd.crosstab(df['врач'], df['поставленный диагноз'], margins=True)

print(df2)
