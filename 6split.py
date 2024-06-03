from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os

var = "Ne"
ylabel = r"Electron density [m$^{-3}$]"
zind = 32
xind = 32
yind = 8
path1 = "good-sims/linear"
path2 = "good-sims/fixed17"
path3 = "good-sims/fixed18"
path4 = "good-sims/fixed19"
path5 = "good-sims/fixed20"
path6 = "good-sims/evolve20"
path7 = "good-sims/evolve21"
path8 = "good-sims/evolve22"
path9 = "good-sims/evolve23"
pathopts = []
pathopts.append([path1, 'k', "No Neutrals"])
pathopts.append([path2, 'r', path2[10:]])
pathopts.append([path3, 'b', path3[10:]])
pathopts.append([path4, 'm', path4[10:]])
pathopts.append([path5, 'c', path5[10:]])
pathopts.append([path6, 'tab:pink', path6[10:]])
pathopts.append([path7, 'tab:purple', path7[10:]])
pathopts.append([path8, 'tab:brown', path8[10:]])
pathopts.append([path9, 'tab:orange', path9[10:]])

for sp in np.arange(40,70,10):
	fig, ax = plt.subplots()
	spl = sp + 10
	for path,k,lbl in pathopts:
		norm = collect("Nnorm", path=path)
		data = norm * collect(var, path = path, xind=xind, yind=yind, zind=zind).squeeze()
		x_data = 1e3 * collect("t_array", path = path) / collect("Omega_ci", path = path)
		plt.plot(x_data[sp:spl], data[sp:spl], axes = ax, c = k, label = lbl)
	plt.xlabel("Time [ms]")
	plt.ylabel(ylabel)
	plt.legend()
	plt.title("T=" + str(sp) + ":" +str(spl)) 
	plt.savefig("3_29_plots/splits/"+str(sp)+"-"+str(spl)+".png")
	plt.close("all")
