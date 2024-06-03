from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
import scipy.fft as fft
from scipy import signal

var = "Ne"
path1 = os.path.join("good-sims/linear", ".")
path2 = os.path.join("good-sims/fixed17",".")
path3 = os.path.join("good-sims/fixed18",".")
path4 = os.path.join("good-sims/fixed19",".")
path5 = os.path.join("good-sims/fixed20",".")
path6 = os.path.join("good-sims/evolve20",".")
path7 = os.path.join("good-sims/evolve21",".")
path8 = os.path.join("good-sims/evolve22",".")
path9 = os.path.join("good-sims/evolve23",".")
pathopts = []
pathopts.append([path1, 'k', "No Neutrals", 210])
pathopts.append([path2, 'r', path2[10:-2], 210])
pathopts.append([path3, 'b', path3[10:-2], 190])
pathopts.append([path4, 'm', path4[10:-2], 70])
pathopts.append([path5, 'c', path5[10:-2], 70])
pathopts.append([path6, 'tab:pink', path6[10:-2], 210])
pathopts.append([path7, 'tab:purple', path7[10:-2], 220])
pathopts.append([path8, 'tab:brown', path8[10:-2], 110])
pathopts.append([path9, 'tab:orange', path9[10:-2], 100])

plt.figure()

xopt = [32]
yopt = [8]
zopt = [32]

for xind in xopt:
	for yind in yopt:
		for zind in zopt:
			for [path, k, label, nom] in pathopts:
				norm = collect("Nnorm", path=path)
				data = norm * collect(var, path = path, xind=xind, yind=yind, zind=zind).squeeze()
				x_data = 1e3 * collect("t_array", path = path) / collect("Omega_ci", path = path)
				sr = 1/(x_data[1] - x_data[0]) #sampling rate
				print(sr)
				f, Pxx_den = signal.welch(data[nom:], sr, nperseg=100, scaling = 'spectrum')
				plt.loglog(f, np.sqrt(Pxx_den), color = k, label = label)
			plt.xlabel("frequency [hz]")
			plt.ylabel("amplitude")
			plt.legend()
			plt.title("FFT")
			plt.savefig("3_29_plots/fft/all")
			plt.close("all")
			plt.figure()
