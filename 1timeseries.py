
from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt

paths = ["good-sims/evolve21"]

var = "Nneuts"
norm = collect("Nnorm", path=paths[0])
label = r"Electron density [m$^{-3}$]"
inds = (32,8,32)

datasets = [collect(var, path=path, xind=inds[0], yind=inds[1], zind=inds[2]).squeeze() for path in paths]
times = [collect("t_array", path=path) for path in paths]

data = np.concatenate(datasets) * norm
time = 1e3 * np.concatenate(times) / collect("Omega_ci", path=paths[0]) # ms


plt.plot(time, data)
plt.xlabel("Time [ms]")
plt.ylabel(label)
plt.savefig("4_14_plots/neutral_" + "_{}_{}_{}_timeseries.png".format(*inds))
#plt.savefig("3_4_plots/fixed_"+var + "_{}_{}_{}_timeseries.pdf".format(*inds))
#plt.show()

