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

"""df = pd.DataFrame({    'Специальность' : ['Ветеринар', 'Ветеринар',
                        'Психолог', 'Психолог'] * 6,
                        'Врач' : ['Андрей', 'Сергей', 'Ирина'] * 8,
                        'Диагноз' : ['Простуда', 'Простуда', 'Простуда',
                                    'Волнения', 'Волнения', 'Простуда'] * 4,    
                        'Доза' : sps.randint(low=1, high=6).rvs(size=24),    
                        'Продолжительность' : sps.randint(low=1, high=6).rvs(size=24) })
df
"""



gp = df.groupby('врач')

result_A = gp.get_group('Андрей')
print(result_A)
b = result_A.groupby('поставленный диагноз').sum()
print(b)

sum_A = gp[['поставленный диагноз']].get_group('Андрей')
print(sum_A)

