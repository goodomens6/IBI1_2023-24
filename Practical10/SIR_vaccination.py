import numpy as np
import matplotlib . pyplot as plt

N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05

Susceptible_population=[]
Infected_population=[]
Recovered_population=[]
time=[]

days=1000
for day in range(days):
    time.append(day)
    Susceptible_population.append(S)
    Infected_population.append(I)
    Recovered_population.append(R)

    contact_probability=I/N
    infection_probability=contact_probability*beta
    I_list=np.random.choice(range(2),S,p=[infection_probability,1-infection_probability])
    New_I=np.sum(I_list==0)
    R_list=np.random.choice(range(2),I,p=[gamma,1-gamma])
    New_R=np.sum(R_list==0)
    
    S-=New_I
    R+=New_R
    I=I+New_I-New_R

plt.plot(time, Infected_population, label='Infected')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()


import numpy as np
import matplotlib . pyplot as plt

N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05

Susceptible_population=[]
Infected_population=[]
Recovered_population=[]
time=[]

vaccined_levels=10
for vaccined_level in range(vaccined_levels):
    vaccined_percent=vaccined_level/10
    V=vaccined_percent*N
    days=1000
    for day in range(days):
        time.append(day)
        Susceptible_population.append(S)
        Infected_population.append(I)
        Recovered_population.append(R)

        contact_probability=I/N
        infection_probability=contact_probability*beta
        I_list=np.random.choice(range(2),S-V,p=[infection_probability,1-infection_probability])
        New_I=np.sum(I_list==0)
        R_list=np.random.choice(range(2),I,p=[gamma,1-gamma])
        New_R=np.sum(R_list==0)
    
        S-=New_I
        R+=New_R
        I=I+New_I-New_R

plt.plot(time, Infected_population, label='Infected')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()