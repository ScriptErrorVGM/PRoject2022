# This Python file uses the following encoding: utf-8
from multiprocessing.sharedctypes import Value
from optparse import Values
import os, sys
from asyncio.windows_events import NULL
from distutils.log import info
from re import L
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd 
import math
import seaborn as sns


data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

# nuber 1

df = pd.DataFrame(data)

df[3] = df[3].astype(float)


assert type(df) == pd.core.frame.DataFrame, "Объект df не является датафреймом"
assert df.shape == (5, 4), "Неверное число строк и столбцов"
assert df.dtypes.values[-1] == float, "Последний столбец не имеет тип float"

# number 2


N = len(df)

assert N == 5, "Неверный ответ"

# number 3

cn = df[3].notnull().sum()

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

# nubmer 7

df['logcheer'] = np.log(df['cheer'])

assert math.isclose(df["logcheer"].values[-2], -0.22314, abs_tol = 1e-5),"Неверно" 
assert math.isnan(df["logcheer"].values[-4]), "Неверно"

# number 8

tab = df['class'].value_counts()
x = tab.index
y = tab.values

#print(x,y)
sns.set()

sns.barplot(x=x,y=y)
plt.xlabel('class')
plt.ylabel('count')
plt.title('unique values with repeat count')

plt.show()

# number 9

L = [{'id': 53050,
  'text': 'В рамках проекта «Социальный лифт» Вышка предоставляет льготы при поступлении абитуриентам, оказавшимся в сложных жизненных обстоятельствах и социально-экономических условиях. В 2019 году льготу получил 71 человек, а в этом году университет готов оказать поддержку уже 165 абитуриентам.\n\nМы поговорили с ребятами, поступившими по программе, и делимся их историями в новом видео.\n\nПодробнее об условиях участия, сроках и количестве мест можно прочитать по ссылке: r.hse.ru/lift',
  'likes': {'count': 56, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 14370}},
 {'id': 53163,
  'text': 'Даже в самом загруженном расписании стоит оставить немного места для заботы о себе. «Вышка для своих» делится мартовской подборкой мероприятий [club6222726|Центра психологического консультирования ВШЭ]: от хатха-йоги до групповых кинопросмотров',
  'likes': {'count': 6, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 2460}},
 {'id': 53161,
  'text': 'Начался прием заявок на соискание премии HSE Alumni Awards. 19 марта стартует открытое онлайн-голосование, которое определит шорт-листы по каждой номинации. Лауреатами премии могут стать выпускники всех кампусов Вышки.\n\nЗаявки принимаются до 15 марта на сайте премии: bit.ly/2TzuxXn',
  'likes': {'count': 4, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 2144}},
 {'id': 53159,
  'text': 'Вышка заняла первое место среди российских вузов по десяти предметам в рейтинге QS World University Rankings by Faculty & Subject 2020. Всего университет представлен в 19 предметных рейтингах, а по пяти из них входит в топ-100 глобального списка.\n\nВ этом году ВШЭ также присутствует в 4 из 5 отраслей QS, в том числе впервые в «Естественных науках»',
  'likes': {'count': 90, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 7136}},
 {'id': 53136,
  'text': 'Почему изучать космос сложно, но интересно, для чего нужно наблюдать за геокороной Земли и как вернуть престиж профессии учёного? Рассказывает преподаватель факультета физики ВШЭ Игорь Балюкин, победитель конкурса ИКИ РАН в номинации «Лучшая работа, выполненная молодыми учеными»',
  'likes': {'count': 15, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 4255}},
 {'id': 53133,
  'text': 'В феврале и начале марта сотрудники Вышки провели заключительный этап олимпиады [club154631231|«Я — профессионал»] по восьми направлениям. В соревнованиях приняли участие более 1600 студентов из 65 регионов и 212 вузов',
  'likes': {'count': 4, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 3266}},
 {'id': 53132,
  'text': 'В первый день весны на краешке Москвы прошёл зимний спортивный фестиваль [club35314658|HSE SNOW FEST], в котором приняли участие 460 человек. Горячий чай с блинами, квесты, соревнования по горным лыжам и сноуборду ждали студентов, преподавателей и выпускников Вышки',
  'likes': {'count': 76, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 6847}},
 {'id': 53130,
  'text': 'Команда [club24893373|МИЭФ] и сборная Вышки заняли первое и второе места на российском этапе «инвестиционной олимпиады» CFA Institute Research Challenge. В апреле студенты отправятся на европейский финал в Иорданию, а в случае успеха — в Нью-Йорк на глобальный финал конкурса',
  'likes': {'count': 23, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
  'views': {'count': 4376}}]

info = pd.DataFrame(L)

assert info.shape == (8, 4), "Неверное число строк или столбцов"


# number 10
temp_likes = info['likes']
temp_views = info['views']
info['nlikes'] = 0
info['nviews'] = 0

for n in range(8) : 
        tab_1 = pd.DataFrame(temp_likes[n].items() )
        tab_2 = pd.DataFrame(temp_views [n].items())
        info.loc[n,'nviews'] = tab_2.loc[0][1]
        info.loc[n,'nlikes'] = tab_1.loc[0][1]



assert info.loc[3, "nlikes"] == 90, "Неверное решение"
assert info.loc[6, "nlikes"] == 76, "Неверное решение"
assert info.loc[5, "nviews"] == 3266, "Неверное решение"
assert info.loc[2, "nviews"] == 2144, "Неверное решение"

