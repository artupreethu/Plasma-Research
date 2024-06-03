from boutdata import collect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


var = "Ne"

path1 = "good-sims/linear"
path2 = "good-sims/fixed15"
path3 = "good-sims/fixed16"
path4 = "good-sims/fixed17"
path5 = "good-sims/fixed18"
path6 = "good-sims/fixed19"
path7 = "good-sims/fixed20"
path8 = "good-sims/fixed21"

pathopts = []
pathopts.append([path1, 'k', "$N_n$=0",'dotted'])
pathopts.append([path2, 'r', "$N_n$~$10^{15}$", 'solid'])
pathopts.append([path3, 'b', "$N_n$~$10^{16}$", 'solid'])
pathopts.append([path4, 'm', "$N_n$~$10^{17}$", 'solid'])
pathopts.append([path5, 'k', "$N_n$~$10^{18}$", 'solid'])
pathopts.append([path6, 'tab:pink', "$N_n$~$10^{19}$", 'solid'])
pathopts.append([path7, 'c', "$N_n$~$10^{20}$", 'solid'])
pathopts.append([path8, 'tab:brown', "$N_n$~$10^{21}$", 'solid'])

if var == "Nneuts":
	pathopts = pathopts[1:]
	nama = "neutral"
else:
	nama = "electron"

legendlabels = []
for item in pathopts:
        legendlabels.append(item[2])

nav = []
#pathopts = [pathopts[8]]
for path,k,lbl,ls in pathopts:
	for tind in np.linspace(200,500,301):
		n = collect(var, path = path, tind=int(tind)).squeeze()
		nnorm = collect("Nnorm", path = path)
		nav.append(n)
	density = np.mean(nav, axis=(0,1,2)) * nnorm #0 time, 2 azimuthal
	z = collect("dz", path=path).squeeze()
#	print(density)
#	print(density.shape)
#	print(z)
#	print(z.shape)
	plt.plot(np.arange(z.shape[0])*(360/64), density, c = k, label = lbl, ls=ls)

plt.xlabel('Azimuthal Angle')
plt.ylabel(r'Average ' + nama + ' Density [m$^{-3}$]')
plt.title('Azimuthal Profile')
plt.legend(labels = legendlabels, labelcolor = 'linecolor')
plt.savefig('final_thesis/all_azi.png')
	#plt.close("all")
