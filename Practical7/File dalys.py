import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')
print(dalys_data.iloc[0:100:10,3:4])
print(dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs'])
china_data=dalys_data.loc[dalys_data['Entity']=='China',['Entity','Year','DALYs']]
print('mean:'+str(np.mean(china_data.iloc[ : ,2])))
print('2019:'+str(china_data.iloc[-1,-1]))# the DALYs in China in 2019 was less than the mean

plt.plot(china_data['Year'],china_data['DALYs'],'bo')
plt.ylabel('DALYs')
plt.xlabel('Year')
plt.title('DALYs in China over time')
plt.xticks(china_data.Year,rotation=-50)
plt.show()
plt.clf()

UK_data=dalys_data.loc[dalys_data['Entity']=='United Kingdom',['Entity','Year','DALYs']]
plt.plot(china_data['Year'],china_data['DALYs'], label = "China")
plt.plot(UK_data['Year'],UK_data['DALYs'], label = "UK")
plt.title('DALYs in China and UK over time')
plt.ylabel('DALYs')
plt.xlabel('Year')
plt.legend()
plt.show()
plt.clf()