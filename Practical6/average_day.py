activity = {'Sleeping':8,"Classes":6,'Studing':3.5,'TV':2, 'Music':1,'Others':3.5}#make a dictionary to record the data
print(activity)#print the dictionary

import matplotlib.pyplot as plt
activity_labels=activity.keys()
time_day=activity.values()
plt.figure()
plt.pie(time_day,labels=activity_labels,startangle=90)#make pie chart
plt.show()#show the pie chart
plt.clf()

one_activity='Sleeping'#You can change this to check the hours spent on one specific activity
t=activity[one_activity]#print the hours spent on one specific activity
print(t)