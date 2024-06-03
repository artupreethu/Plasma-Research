from boutdata import collect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


yind = 8
var = "Ne"

path1 = ["good-sims/linearf18-2", "$N_n$=0", "k", 'dotted',200]
path2 = ["good-sims/fixed15", "$N_n$~$10^{15}$", "r", 'solid',200]
path3 = ["good-sims/fixed16", "$N_n$~$10^{16}$", "b", 'solid',200]
path4 = ["good-sims/fixed17", "$N_n$~$10^{17}$", "m", 'solid',200]
path5 = ["good-sims/fixed18", "$N_n$~$10^{18}$", "k", 'solid',200]
path6 = ["good-sims/fixed19", "$N_n$~$10^{19}$", "tab:pink", 'solid',200]
path7 = ["good-sims/fixed20", "$N_n$~$10^{20}$", "c", 'solid',200]
path8 = ["good-sims/fixed21", "$N_n$~$10^{21}$", "tab:brown", 'solid',250]

paths = [path1, path2, path3, path4, path5, path6, path7, path8]

if var == "Nneuts":
	paths = paths[1:]
	nama = "neutral"
else:
	nama = "electron"

nav = []

for path,lbl,colr,ls,nom in paths:
	for tind in np.linspace(nom,500,301):
		#print(tind)
		n = collect(var, path = path, yind = yind, tind=int(tind)).squeeze()
		nnorm = collect("Nnorm", path = path)
		nav.append(n)
	density = np.mean(nav, axis=(0,2)) * nnorm #0 time, 2 azimuthal
	g_33 = collect("g_33", path = path, yind = yind).squeeze()
	radius = np.sqrt(g_33) * collect('rho_s0', path = path)
	#print(nneuts)
	#print(radius)
	plt.plot(radius, density, label = lbl, c=colr, linestyle=ls)
	#print(np.array(nav)[100][32])
	#print(np.array(nav)[100][0])
	#print(np.array(nav)[100][16])
	#print(np.array(nav)[100][48])
	#nn = collect("Nneuts", path=path, yind=yind, zind=zind).squeeze()
	#norm = collect("Nnorm", path=path)
	#nnav = np.mean(n, axis=(0))
	#ng_33 = collect("g_33", path=path, yind=yind).squeeze()
	#nradius = np.sqrt(ng_33) * collect('rho_s0', path=path)
	#print(nnav)

plt.xlabel('Radius [m]')
plt.ylabel(r'Average ' + nama + ' Density [m$^{-3}$]')
plt.title('Radial Profile')
plt.legend()
plt.savefig('final_thesis/allrad.png')
plt.close("all")
