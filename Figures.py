import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

numSim = 100
resol100 = [] # Array of resolutions reached after 100
resolFin = [] # Array of maximum resolutions reached 
step95 = []   # Array of number of steps needed to reach 95% of the max resolution reached

for i in range(0,numSim):
    resultsFilename = 'results' + str(i) + '.txt'
    reader = np.loadtxt(resultsFilename)  # Reading file
    resolObs = reader[:,7]                # Only interested in resolution
    numObs = len(resolObs)
    resol100.append(resolObs[99])
    resolFin.append(resolObs[numObs-1])
    maxR = np.max(resolObs)
    step = next((j for j,res in enumerate(resolObs) if res > 0.95*maxR), None) # Step in which 95% max Res. is reached
    step95.append(step)

# Plotting ------
num_bins = 20
f, sub = plt.subplots(2, 2)

n, bins, patches = sub[0,0].hist(resol100, num_bins, normed=1, facecolor='blue', alpha=0.5) # Histogram
mu = np.mean(resol100)
sigma = np.std(resol100)
maxR = np.max(resol100)
minR = np.min(resol100)
y = mlab.normpdf(bins, mu, sigma) # Best fit
sub[0,0].plot(bins, y, 'r--')
sub[0,0].set(xlabel='Resolution', ylabel='Probability')
sub[0,0].set_title('100 steps Res: $\mu=%.0f$ $\sigma=%.0f$, max=%.0f, min=%.0f'%(mu,sigma,maxR,minR), size= 7)

n, bins, patches = sub[0,1].hist(resolFin, num_bins, normed=1, facecolor='blue', alpha=0.5) # Histogram
mu = np.mean(resolFin)
sigma = np.std(resolFin)
maxR = np.max(resolFin)
minR = np.min(resolFin)
y = mlab.normpdf(bins, mu, sigma) # Best fit
sub[0,1].plot(bins, y, 'r--')
sub[0,1].set(xlabel='Resolution', ylabel='Probability')
sub[0,1].set_title('Max steps Res: $\mu=%.0f$ $\sigma=%.0f$, max=%.0f, min=%.0f'%(mu,sigma,maxR,minR), size = 7)

n, bins, patches = sub[1,0].hist(step95, num_bins, normed=1, facecolor='brown', alpha=0.5) # Histogram
mu = np.mean(step95)
sigma = np.std(step95)
maxR = np.max(step95)
minR = np.min(step95)
y = mlab.normpdf(bins, mu, sigma) # Best fit
sub[1,0].plot(bins, y, 'r--')
sub[1,0].set(xlabel='# steps', ylabel='Probability')
sub[1,0].set_title('Steps 95perc max res: $\mu=%.0f$ $\sigma=%.0f$'%(mu,sigma), size = 7)

sub[1,1].scatter(step95, resolFin, alpha=0.8, c='red')
sub[1,1].set(xlabel='# steps', ylabel='Resolution')
sub[1,1].set_title('95per max resolution', size = 7)

# Tweak spacing to prevent clipping of ylabel
#f.subplots_adjust(left=0.15)
f.subplots_adjust( wspace = 0.6, hspace = 0.6, top = None, bottom = None )

plt.savefig('Simplex.pdf')
plt.show()

