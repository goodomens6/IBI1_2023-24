import numpy as np
import matplotlib.pyplot as plt

# set the initial state
N=10000 
I=1 
R=0

# set the infection rate and the recovery rate
beta=0.3
gamma=0.05

# set the vaccinated rate
vaccinated_rates=[0,0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9]

plt.figure(figsize=(10,6))

# loop through all vaccinated rate
for vaccinated_rate in vaccinated_rates:
    # caculate the vaccined population and susceptible population
    V=int(vaccinated_rate*N)
    S=N-I-R-V

    # create 2 list for the two population to track how they evolve over time
    Susceptible_population=[S]
    Infected_population=[I]

    # loop over 1000 time points
    for _ in range(1000):

        # caculate the infection probability
        i=beta*Infected_population[-1]/N
        # caculate the recovery probability
        r=gamma

        # pick susceptible individuals at random to become infected with the infection probability
        infected_choose = np.random.choice(range(2),Susceptible_population[-1],p=[i,1-i])
        # caculate the total number of people who are newly infected
        New_I=np.sum(infected_choose==0)

        # pick infected individuals at random to become recovered with the recovery probability
        recovered_choose = np.random.choice(range(2),Infected_population[-1],p=[r,1-r])
        # caculate the total number of people who are newly recovered
        New_R=np.sum(recovered_choose==0)

        # keep track of the numbers of people in the two categories
        Susceptible_population.append(Susceptible_population[-1]-New_I)
        Infected_population.append(Infected_population[-1]+New_I-New_R)

    # plot the numbers of infected people as a function of time at current vaccinated rate
    plt.plot(Infected_population,label=f"{vaccinated_rate*100}%")

# when the vaccinated rate is 100%, the code before can not run
# set the initial state of 100% vaccinated rate
vaccinated_rate=1
S=0
I=0

# loop over 1000 time points
for _ in range(1000):

    # caculate the infection probability
    i=0
    # caculate the recovery probability
    r=gamma

    # pick susceptible individuals at random to become infected with the infection probability
    infected_choose = np.random.choice(range(2),S,p=[i,1-i])
    # caculate the total number of people who are newly infected
    New_I=np.sum(infected_choose==0)

    # pick infected individuals at random to become recovered with the recovery probability
    recovered_choose = np.random.choice(range(2),I,p=[r,1-r])
    # caculate the total number of people who are newly recovered
    New_R=np.sum(recovered_choose==0)

    # keep track of the numbers of people in the two categories
    Susceptible_population.append(Susceptible_population[-1]-New_I)
    Infected_population.append(Infected_population[-1]+New_I-New_R)

# plot the numbers of infected people as a function of time at 100% vaccinated rate
plt.plot(Infected_population,label=f"{vaccinated_rate*100}%")

# plot the xlable, ylable, title, and legend
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()

# show the plot
plt.show()
plt.clf()