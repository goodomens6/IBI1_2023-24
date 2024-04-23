import numpy as np
import matplotlib . pyplot as plt

# make array of all susceptible population
population = np.zeros( (100 , 100) )
# choose one person to be infected
outbreak = np.random.choice (range(100) ,2)
# change the status from 0 (susceptible) to 1 (infected)
population [outbreak[0],outbreak[1]] = 1

# visualize the population state
plt.figure (figsize=(6 ,4) , dpi=150)
# apply different colors to distinguish the state
cmap=plt.colormaps['viridis']

# draw the map of initial state
plt.subplot(1,4,1)
plt.imshow (population, cmap=cmap, interpolation='nearest')
plt.title('time 0')

# set the infection rate and the recovery rate
beta=0.3
gamma=0.05

#create a function to simulate a loop in the SIR model
def SIR(beta,gamma,population):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x=infectedIndex[0][i]
        y=infectedIndex[1][i]
        
        # change the status from 1 (infectes) to 2 (recovered)
        population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
        

# run the function for 100 loops
times=100
for time in range(times):
    SIR(beta,gamma,population)

    # draw the map after 10 loop
    if time==9:
        plt.subplot(1,4,2)
        plt.imshow (population, cmap=cmap, interpolation='nearest')
        plt.title('time 10')

    # draw the map after 50 loop
    if time==49:
        plt.subplot(1,4,3)
        plt.imshow (population, cmap=cmap, interpolation='nearest')
        plt.title('time 50')

    # draw the map after 100 loop                
    if time==99:
        plt.subplot(1,4,4)
        plt.imshow (population, cmap=cmap, interpolation='nearest')
        plt.title('time 100')

plt.show() # show the map
plt.clf() # close the map