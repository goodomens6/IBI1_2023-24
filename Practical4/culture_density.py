#Function: calculate the day for the culture density goes more than 90%
i=5
j=0
while i<=90:#if the culture density is less than 90%
    i=2*i#the culture density doubles
    j=j+1#the number of days increase 1
#On day 6, the culture density goes over 90%, the loop stops
print('On the',str(j),'day the cell density goes over 90%.')
print('He can have',str(j-1),'days for holiday from the lab.')