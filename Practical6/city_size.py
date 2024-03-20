uk_cities=[0.56,0.62,0.04,9.7]#you can enter numbers that you want to be sorted in order
china_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()#make values be sorted in order
china_cities.sort()
print(uk_cities)#print sorted values
print(china_cities)
uk_city_names=['Edinburgh','Glasgow','Stirling','London']
china_city_names=['Haining','hanghou','Shanghai','Beijing']

import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.bar(uk_city_names,uk_cities)#make bar plot of city sizes in the UK
plt.ylabel('Population(millions)')
plt.title('City sizes in the UK')

plt.figure(2)
plt.bar(china_city_names,china_cities)#make bar plot of city sizes in China
plt.ylabel('Population(millions)')
plt.title('City sizes in China')

plt.show()#show the two bar plots
plt.clf()