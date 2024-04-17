import numpy as np
import matplotlib . pyplot as plt

N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05

Susceptible_population=[S]
Infected_population=[I]
Recovered_population=[R]
time=[0]

plt.figure(figsize=(10,6))

days=1000
for day in range(days):
    time.append(day)
    Susceptible_population.append(S)
    Infected_population.append(I)
    Recovered_population.append(R)

    contact_probability=I/N
    i=contact_probability*beta
    r=gamma

    I_choose=np.random.choice(range(2),S,p=[i,1-i])
    New_I=np.sum(I_choose==0)
    R_choose=np.random.choice(range(2),I,p=[r,1-r])
    New_R=np.sum(R_choose==0)
    
    S-=New_I
    I=I+New_I-New_R
    R+=New_R

plt.plot(time, Susceptible_population, label='Susceptible')
plt.plot(time, Infected_population, label='Infected')
plt.plot(time, Recovered_population, label='Recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()

