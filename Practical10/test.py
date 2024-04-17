import numpy as np
import matplotlib.pyplot as plt

N = 10000 
I= 1 
R = 0
beta = 0.3
gamma = 0.05 
vaccinated_rates = [0,0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9]

plt.figure(figsize=(10,6))

for vaccinated_rate in vaccinated_rates:
    V = int(vaccinated_rate * N)
    S = N-I-R-V

    Susceptible_population= [S]
    Infected_population= [I]

    beta = 0.3  # 传播率
    gamma = 0.05  # 恢复率

    for _ in range(1000):
        i = beta * Infected_population[-1] / N
        r = gamma

        infected_choose = np.random.choice(range(2),Susceptible_population[-1], p=[i,1-i])
        New_I=np.sum(infected_choose==0)

        recovered_choose = np.random.choice(range(2),Infected_population[-1], p=[r,1-r])
        New_R=np.sum(recovered_choose==0)

        Susceptible_population.append(Susceptible_population[-1] -New_I)
        Infected_population.append(Infected_population[-1]+New_I - New_R)

    plt.plot(Infected_population, label=f"vaccinated ({vaccinated_rate*100}%)")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()

