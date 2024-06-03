from boutdata import collect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


datasets = [("linear", "good-sims/linear", 'k--'), ("no neuts", "long-linear", 'b--')]

for xind in [0,16,48,63]:
	for tind in [50,100,200,300,400,450]:
		for label, path, style in datasets:
			n = collect("Ne", path = path, xind = xind, tind=tind).squeeze()
			nnorm = collect("Nnorm", path = path)
			nav = np.mean(n, axis=(1)) * nnorm
			y = collect("dy", path=path).squeeze()
			plt.plot(np.arange(y.shape[1]), nav, style, label=label)
		plt.xlabel("Axial")
		plt.ylabel(r"Electron Density [m$^{-3}$]")
		plt.legend()
		plt.title("Axial Profile at ("+str(xind)+",y,z_avg) & t=" + str(tind))
		plt.savefig("fixedneuts/axialprofiles/"+str(xind)+"-y-zavg-t"+str(tind))
		plt.close("all")
