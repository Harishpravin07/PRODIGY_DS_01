import pandas as pd

from matplotlib import pyplot as plt


df = pd.read_excel('D:\Project\Dataset.xlsx')  

Year = df['Year'].head(20)

age = df['Median Age'].head(20)
 


fig, ax = plt.subplots(figsize =(16, 9))
 
ax.barh(Year, age)
 

for s in ['top', 'bottom', 'left', 'right']:

    ax.spines[s].set_visible(True)


ax.xaxis.set_ticks_position('none')

ax.yaxis.set_ticks_position('none')
 

ax.xaxis.set_tick_params(pad = 5)

ax.yaxis.set_tick_params(pad = 10)
 

ax.grid(color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)
  
ax.invert_yaxis()
 

for i in ax.patches:

    plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
 

ax.set_title('Yearly Median Age', loc ='left', )

plt.show()