import numpy as np
import matplotlib . pyplot as plt

N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05

contact_probability=I/N
I_list=np.random.choice(range(2),S,p=[contact_probability*beta,1-contact_probability*beta])
New_I=np.sum(I_list==0)
print(contact_probability*beta)
print

