from numpy import *

def mc_simulation_eu_call(S0,K,T,r,sigma,no_trial):
    random.seed(1000)
    z=random.standard_normal(no_trial)
    
    ST=S0*exp((r-0.5*sigma**2)*T+sigma*sqrt(T)*z)
    
    payOff=maximum(ST-K,0)
    
    eu_call_price=exp(-r*T)*sum(payOff)/no_trial
    
    return eu_call_price
    
S0=89.0
K=102.0
T=0.5
r=0.03
sigma=0.3
no_trial=1000000

eu_call_price=mc_simulation_eu_call(S0,K,T,r,sigma,no_trial)
print("\n The European Call Price is ${:12.8f}\n".format(eu_call_price))
