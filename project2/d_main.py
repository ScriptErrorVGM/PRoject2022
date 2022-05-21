from matplotlib.pyplot import polar
import numpy as np 
import pandas as pd 
import seaborn as sn
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis

dff = pd.read_csv('netflix_titles.csv')
#print(dff.shape)
#print(dff.columns)

# рейтинг по типу контента
rating = dff.groupby(['rating']).size().reset_index(name='counts')
pie_chart = px.pie(rating, values='counts', names='rating', 
                  title='Распределение рейтингов контента на Netflix',
                  color_discrete_sequence=px.colors.qualitative.Pastel)
#pie_chart.show()


#
# топ 10 режиссеров и актеров

dff['director'] = dff['director'].fillna('No Director Specified')
directors_filter = pd.DataFrame()
directors_filter = dff['director'].str.split(',', expand = True).stack() #  return DataFrame/MultiIndex expanding dimensionality.
directors_filter = directors_filter.to_frame() # конвертирует объект в датафрейм
directors_filter.columns = ['Director']

directors = directors_filter.groupby(['Director']).size().reset_index(name = 'Total Content')
directors = directors[directors.Director != 'No Director Specified']
directors = directors.sort_values(by = ['Total Content'], ascending = False)

directors_top_10 = directors.head(10)
directors_top_10 = directors_top_10.sort_values(by = ['Total Content'])
fig_1 = px.bar(directors_top_10, x = 'Total Content', y = 'Director', title = 'Топ 10 Режиссеров на Netflix')
#fig_1.show()

# топ 10 актеров 
dff['cast'] = dff['cast'].fillna('No Cast Specified')
cast_filter = pd.DataFrame()
cast_filter = dff['cast'].str.split(',', expand = True).stack()
cast_filter = cast_filter.to_frame()
cast_filter.columns = ['Actor']

actors = cast_filter.groupby(['Actor']).size().reset_index(name = 'Total Content')
actors = actors[actors.Actor != 'No Cast Specified']
actors = actors.sort_values(by = ['Total Content'], ascending =False)

actors_top_10 = actors.head(10)
actors_top_10 = actors_top_10.sort_values(by = 'Total Content')
fig_2 = px.bar(actors_top_10, x = 'Total Content', y = 'Actor' , title = 'Топ 10 Актеров на Netflix')
#fig_2.show()

#
# тенденция производства контента

df1 = dff[['type', 'release_year']]
df1 = df1.rename(columns = {'release_year' : 'Release Year'})
df2 = df1.groupby(['Release Year', 'type']).size().reset_index(name = 'Total Content')
df2 = df2[df2['Release Year'] >= 2000]
fig_3 = px.line(df2, x = 'Release Year', y = 'Total Content',color = 'type', title = 'Тенденция контента, созданного за эти годы на Netflix')
#fig_3.show()


#
# отношение к контенту

dfx=dff[['release_year','description']]
dfx=dfx.rename(columns={'release_year' : 'Release Year'})
for index,row in dfx.iterrows():
    z = row['description']
    testimonial=TextBlob(z)
    p = testimonial.sentiment.polarity
    if p == 0:
        sent ='Neutral'
    elif p > 0:
        sent = 'Positive'
    else:
        sent = 'Negative'
    dfx.loc[[index,2],'Sentiment']=sent


dfx = dfx.groupby(['Release Year','Sentiment']).size().reset_index(name = 'Total Content')

dfx = dfx[dfx['Release Year'] >= 2000]
fig4 = px.bar(dfx, x = "Release Year", y = "Total Content", color = "Sentiment", title = "Отношение к контенту на Netflix")
#fig4.show()


#
# корреляция

#print(df2)
n_col = ['Release Year','type','Total Content']

#corr_matrix = df2.loc[:,n_col].corr()
#print(corr_matrix)
#fig_corr = plt.figure(14,10)

sb_plot = sn.pairplot(df2[n_col])
#plt.show()

df2[n_col].corr()

fig_corr = plt,figure(figsize = (14,10))

sn.heatmap(df2[n_col].corr(), cmap='Reds')
#plt.show()


#
# animation 


Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

fig =plt.figure(figsize=(10,6))
plt.xlim(2000,2021)
plt.ylim(np.min(df2)[2],np.max(df2)[2])
plt.xlabel('LOL', fontsize=20)
plt.ylabel('KEK',fontsize=20)
plt.title('ALA',fontsize=20)

def animate(i):
    data = df2.iloc[:int(i+1)] #select data range
    p = sn.lineplot(x=df2.index, y=df2[title], data=data, color="r")
    p.tick_params(labelsize=17)
    plt.setp(p.lines,linewidth=7)

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=17, repeat=True)
print(df2)
plt.show()
#ani.save('HeroinOverdosesJumpy.mp4', writer=writer)


