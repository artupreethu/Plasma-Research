from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os

var = "Ne"
ylabel = r"Electron density [m$^{-3}$]"
path1 = os.path.join("good-sims/linearf18-2", ".")
path2 = os.path.join("good-sims/fixed15", ".")
path3 = os.path.join("good-sims/fixed16", ".")
path4 = os.path.join("good-sims/fixed17", ".")
path5 = os.path.join("good-sims/fixed18", ".")
path6 = os.path.join("good-sims/fixed19", ".")
path7 = os.path.join("good-sims/fixed20", ".")
path8 = os.path.join("good-sims/fixed21", ".")

pathopt = []
pathopt.append([path1, 'k', 'dotted', '$N_n$=0']) 
pathopt.append([path2, 'r', 'solid', '$N_n$~$10^{15}$']) 
pathopt.append([path3, 'b', 'solid', '$N_n$~$10^{16}$']) 
pathopt.append([path4, 'm', 'solid', '$N_n$~$10^{17}$']) 
pathopt.append([path5, 'k', 'solid', '$N_n$~$10^{18}$']) 
pathopt.append([path6, 'tab:pink', 'solid', '$N_n$~$10^{19}$']) 
pathopt.append([path7, 'c', 'solid', '$N_n$~$10^{20}$']) 
pathopt.append([path8, 'tab:brown', 'solid', '$N_n$~$10^{21}$']) 

legendlabels = []
for item in pathopt:
	legendlabels.append(item[3])

xopt = [0, 16, 32, 48, 56]
yopt = [0, 4, 8, 12, 15]
zopt = [32]

for xind in xopt:
	for yind in yopt:
		for zind in zopt:
			fig, ax = plt.subplots()
			for [path,k,ls,lbl] in pathopt:
				norm = collect("Nnorm", path=path)
				data = norm * collect(var, path=path, xind = xind, yind = yind, zind = zind).squeeze()
				x_data = 1e3 * collect("t_array", path = path) / collect("Omega_ci", path = path)
				#if path == path1:
				#	data = np.full(501, data)
				plt.plot(x_data, data, axes = ax, c = k, linestyle = ls, label = lbl)
			plt.xlabel("Time [ms]")
			plt.ylabel(ylabel)
			plt.legend(labels = legendlabels, labelcolor = 'linecolor')
			plt.title("Electron Density Timeseries at (" + str(xind) +", " + str(yind) + ", " + str(zind) + ")") 
			plt.savefig("final_thesis/electron_timeseries_"+str(xind) + "_" + str(yind) + "_" + str(zind))
			plt.close("all")

