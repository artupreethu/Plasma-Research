from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
import math

#var = "Nneuts"
ylabel = r"Neutral density [m$^{-3}$]"
path1 = os.path.join("good-sims/linearf17-2", ".")
path2 = os.path.join("good-sims/fixed17", ".")
paths=[path1,path2]

#			data2 = norm2 * collect(var, path = path2, xind=xind, yind=yind, zind=zind).squeeze()
#			x_data2 = 1e3 * collect("t_array", path = path2) / collect("Omega_ci", path = path2)
			#fig, ax = plt.subplots()
			#plt.plot(x_data1, data1, axes = ax, c = 'k', label = "no neutrals")
			#plt.plot(x_data2, data2, axes = ax, c = 'b', label = "neutrals")
			#plt.xlabel("Time [ms]")
			#plt.ylabel(ylabel)
			#plt.legend()
			#plt.title("Neutral Density Over Time at (" + str(xind) +", " + str(yind) + ", " + str(zind) +")") 
			#plt.savefig("fixedneuts/neut")
from scipy.optimize import curve_fit

def func(r,a,b,c):
    return [a * (1-math.tanh((b*i-c))) for i in r]
nav=[]
var = "Ne"
inds = [32,8,32]
for path in paths:
	for tind in np.linspace(0,500,501):
		n = collect(var, path = path, yind = inds[1], tind=int(tind)).squeeze()
		nnorm = collect("Nnorm", path = path)
		nav.append(n)
		density = np.mean(nav, axis=(0,2)) * nnorm #0 time, 2 azimuthal
		g_33 = collect("g_33", path = path, yind = inds[1]).squeeze()
		radius = np.sqrt(g_33) * collect('rho_s0', path = path)
	if path == path1:
		ne1 = []
		um = [ne1.append(i) for i in density]
		rad1 = []
		um = [rad1.append(i) for i in radius]
	if path == path2:
		ne2 = []
		um = [ne2.append(i) for i in density]
		rad2 = []
		um = [rad2.append(i) for i in radius]
#	print("radius")
#	print(rad)
#	print("densities")
#	print(ne)
#	popt, pcov = curve_fit(func, rad, ne, p0=[1e18,1,5])
#	print(str(popt[0])+"*(1-tanh("+str(popt[1])+"r-"+str(popt[2])+"))")
#	print(popt)
error=[]
for i in np.arange(len(ne1)):
	error.append(ne1[i]-ne2[i])
print(error)
