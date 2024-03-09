import numpy as np
from scipy import optimize

#Define parameters
alpha=1/3
beta=2/3
p2=1
N=75

#Initial endowment
w_A_1=0.8
w_A_2=0.3
w_B_1=1-w_A_1
w_b_2=1-w_A_2
w_1=w_A_1+w_B_1
w_2=w_A_2+w_B_2

#Seed
seed=1986
np.random.seed()



#Define utility and demand function
def u_A(x1, x2):
    return x1**alpha*x2**(1-alpha)

def u_B(x1, x2):
    return x1**beta*x2**(1-beta)

def A_demand_1(p1,p2,w_A_1,w_A_2):
    return alpha*(p1*w_A_1+p2*w_A_2)/p1


def A_demand_2(p1,p2,w_A_1,w_A_2):
    return (1-alpha)*(p1*w_A_1+p2*w_A_2)/p2


def B_demand_1(p1,p2,w_A_1,w_A_2):
    return alpha*(p1*w_A_1+p2*w_A_2)/p1

def B_demand_2(p1,p2,w_A_1,w_A_2):
    return (1-beta)*(p1*w_A_1+p2*w_A_2)/p2


#Demand function for good 1
def demand_good_1(alpha, beta, p1, p2, w_1, w_2):
    #Income based on endowments and price
    I=p1*w_1+p2*w_2

    #Demand for good 1 as a function of price, preference and income
    x_1=alpha*I/p1

    #Aggrated demand
    return np.sum(x_1)


    

#Excess demand function
def excess_demand_good_1()
    
    #Total demand for good 1
    demand_x_1=demand_good_1(alpha, beta, p1, p2, w_1, w_2)

    #Total supply of good 1
    supply_x_1=np.sum(w_1)
#Walras market clearing







#




