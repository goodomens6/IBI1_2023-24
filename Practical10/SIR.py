import numpy as np
import matplotlib . pyplot as plt

# set the initial state
N=10000
S=9999
I=1
R=0

# set the infection rate and the recovery rate
beta=0.3
gamma=0.05

# create 3 list for each of the three population to track how they evolve over time
Susceptible_population=[S]
Infected_population=[I]
Recovered_population=[R]
# create a list to store the time change
time=[0]

plt.figure(figsize=(10,6))

# loop over 1000 time points
days=1000
for day in range(days):

    # caculate the infection probability
    contact_probability=I/N
    i=contact_probability*beta
    # caculate the recovery probability
    r=gamma

    # pick susceptible individuals at random to become infected with the infection probability
    I_choose=np.random.choice(range(2),S,p=[i,1-i])
    # caculate the total number of people who are newly infected
    New_I=np.sum(I_choose==0)

    # pick infected individuals at random to become recovered with the recovery probability
    R_choose=np.random.choice(range(2),I,p=[r,1-r])
    # caculate the total number of people who are newly recovered
    New_R=np.sum(R_choose==0)
    
    # caculate the three population
    S-=New_I
    I=I+New_I-New_R
    R+=New_R

    # keep track of the numbers of people in all three categories and the time
    time.append(day)
    Susceptible_population.append(S)
    Infected_population.append(I)
    Recovered_population.append(R)

#  plot the numbers of susceptible, infected, and recovered people as a function of time.
plt.plot(time, Susceptible_population, label='Susceptible')
plt.plot(time, Infected_population, label='Infected')
plt.plot(time, Recovered_population, label='Recovered')

# plot the xlable, ylable, title, and legend
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

# show the plot
plt.show()
plt.clf()

