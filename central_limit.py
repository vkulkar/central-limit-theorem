# Demonstrates the central limit theorem.
# Flip a coin (Heads = 1, Tails = 0 or vice versa) n times and compute the sum. Repeat m times.
# Creates a normalized histogram of the sums and compares to the theoretical Gaussian distribution.
# Theoretically, the mean value of the sum should be n/2.0
# The variance should be n/4.0
# This script requires numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

def toss(n,m):
    '''
    toss n coins simultaneously. Compute the sum.
    Repeat m times
    '''
    s = np.random.random_integers(0,1,(n,m))
    return np.sum(s,axis=0)

def main():
    n = 400
    m = 5000
    sums = toss(n,m)

#   compute the histogram
    h = np.histogram(sums, bins=range(0,n+2))
    val =h[1][:-1] # removes the last point

#   theoretical results: Gaussian distribution
    miu = n*0.5 # theoretical mean
    sigma = np.sqrt(n*0.5*0.5) # theoretical standard deviation
    x = np.linspace(0,n,5000)
    y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-1.0*(x-miu)**2/(2.0*sigma**2))

#   plot the results
    bar1 = plt.bar(val,h[0]/(m*1.0))
    plt.xlim(miu-3*sigma,miu+3*sigma)
    xpos = [miu-3*sigma,miu-2*sigma,miu-sigma,miu,miu+sigma,miu+2*sigma,miu+3*sigma]
    plt.xticks(xpos,[r'$\mu-3\sigma$',r'$\mu-2\sigma$',r'$\mu-\sigma$',r'$\mu$',r'$\mu+\sigma$',r'$\mu+2\sigma$',r'$\mu+3\sigma$'])
    plt.title(r'Calculated average = %.2f, $\mu$ = %.2f, Calculated stdev = %.2f, $\sigma$ = %.2f' %(np.average(sums),miu,np.std(sums),sigma),{'fontsize':24})
    plt.xlabel('Sums',{'fontsize':24})
    plt.ylabel('Probability',{'fontsize':24})
    plt.tick_params(axis='both',labelsize=24)
    line1, = plt.plot(x,y,'r--',linewidth=6.0)
    plt.legend([line1,bar1],['Theory','Simulation'],fontsize=24)
    plt.show()

if(__name__ == '__main__'):
    main()
        
