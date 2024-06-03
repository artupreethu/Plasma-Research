from boutdata import collect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


var = "Nneuts"
nama = "neutral"

#path1 = "good-sims/evolve20"
path2 = "good-sims/evolve21"
#path3 = "good-sims/evolve22"
#path4 = "good-sims/evolve23"

pathopts = []
#pathopts.append([path1, 'k', path1[10:]])
pathopts.append([path2, 'r', path2[10:]])
#pathopts.append([path3, 'b', path3[10:]])
#pathopts.append([path4, 'm', path4[10:]])

legendlabels = []
for item in pathopts:
        legendlabels.append(item[2])

#nav = []
#for path,k,lbl in pathopts:
#	for tind in np.linspace(0,500,6):
#		for xind in np.linspace(0,63,64):
#			n = collect(var, path = path, xind = xind, yind = 8, zind = 32, tind=int(tind)).squeeze()
#			nnorm = collect("Nnorm", path = path)
#			nav.append(n)
#	density = np.mean(nav, axis=(0,1,2)) * nnorm #0 time, 2 azimuthal
#	z = collect("dz", path=path).squeeze()
#	plt.plot(np.arange(z.shape[0]), density, c = k, label = lbl)
#
#plt.xlabel('Azimuthal Angle')
#plt.ylabel(r'Average ' + nama + ' Density [m$^{-3}$]')
#plt.title('Azimuthal Profile')
#plt.legend(labels = legendlabels, labelcolor = 'linecolor')
#plt.savefig('3_29_plots/' + nama + '_azimuthal_profiles/all')
	#plt.close("all")


nav = []
df = pd.DataFrame(columns = ['T', 'X', 'Nneuts'])
for path,k,lbl in pathopts:
	for xind in np.arange(0,64,16):
		for tind in np.linspace(0,500,6):
			n = collect(var, path=path, xind=int(xind), yind=8, zind=32, tind=int(tind)).squeeze()
			nnorm = collect("Nnorm", path=path)
			density = n * nnorm
			df.loc[len(df.index)] = [tind,xind,density]
100df = df.loc[6:11]
200df = df.loc[12:17]
300df = df.lov[18:23]
