from math import log, sqrt,exp
from scipy import stats

def bs_callandput_value(S,K,T,r,sigma,option_type):
    if option_type=="call":
        d1=(log(S/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
        d2=d1-sigma*sqrt(T)
        N_d1=stats.norm.cdf(d1,0.0,1.0)
        N_d2=stats.norm.cdf(d2,0.0,1.0)
        price=(S*N_d1-K*exp(-r*T)*N_d2)
        
    if option_type=="put":
        d1=(log(S/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
        d2=d1-sigma*sqrt(T)
        N_d1=stats.norm.cdf(-d1,0.0,1.0)
        N_d2=stats.norm.cdf(-d2,0.0,1.0)
        price=(K*exp(-r*T)*(N_d2)-S*(N_d1))
        
    print("This option's price is {}".format(price))
    return(price)
    
bs_callandput_value( 
S=89,
K=100,
T=0.5,
r=0.02,
sigma=0.20,
option_type="call")

bs_callandput_value( 
S=102.5,
K=88.5,
T=0.25,
r=0.03,
sigma=0.3,
option_type="put")
