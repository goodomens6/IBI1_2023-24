uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
uk_city_names=['Edinburgh','Glasgow','Stirling','London']
china_city_names=['Haining','hanghou','Shanghai','Beijing']
print(uk_cities)
print(china_cities)

import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.bar(uk_city_names,uk_cities)
plt.ylabel('Population(millions)')
plt.title('Population of cities in the UK')

plt.figure(2)
plt.bar(china_city_names,china_cities)
plt.ylabel('Population(millions)')
plt.title('Population of cities in China')

plt.show()
plt.clf()