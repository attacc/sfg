from yambopy import *
from yambopy.nl.sum_frequencies import SF_Harmonic_Analysis
from tqdm import tqdm

folder_name="EF"
n_steps=10
X_order=4

SFG_list     =[]
Freqs2_list  =[]

for ifolder in range(n_steps):
    print("Reading folders .... "+str(ifolder))
    try:
        fname=folder_name+str(ifolder)
        NLDB=YamboNLDB(calc=fname)
    except:
        print("Error reading folder "+str(ifolder))
        break
    Xhi=SF_Harmonic_Analysis(NLDB,X_order=X_order,prn_Peff=False,prn_Xhi=False)
    Freqs2_list.append(NLDB.Efield[1]["freq_range"][0])
    SFG_list.append(Xhi[1+X_order,1+X_order,:,:])



