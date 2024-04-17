#!/usr/bin/env python

import numpy as np
import subprocess
import os

def change_field_freq(file_in, file_out,id_field, new_freq):
    # Read the contents of the file
    with open(file_in, 'r') as file:
        lines = file.readlines()
    fname="Field%d_Freq" % id_field

    # Find the line containing "Field2_Freq"
    for i, line in enumerate(lines):
        if fname in line:
            # Split the line into parts separated by '|'
            parts = lines[i+1].split('|')

            # Modify the frequency values
            parts[0] = "{:10.6f}".format(new_freq)
            parts[1] = "{:10.6f}".format(new_freq)

            # Join the modified parts back into a single line
            lines[i+1] = '|'.join(parts)
            break

    # Write the modified contents back to the file
    with open(file_out, 'w') as file:
        file.writelines(lines)

yambo_input="yambo.in_sfg" # Initial input file
id_field   =2 # External field to modify

# Loop on frequencies of the field id_field
start=2.0
end  =8.0
nsteps=120

mpirun="/home/attacc/local_gfortran/bin/mpirun -np 10"
yambo ="/home/attacc/SOFTWARE/yambo-bugfixes/bin/yambo_nl" 

frange = np.linspace(start, end, nsteps, endpoint=False)
for ifreq,freq in enumerate(frange):
        print("Doing freq %d of %d ..." % (ifreq+1,nsteps))
        yambo_output="yambo.in_sfg_EF%d" % ifreq
        change_field_freq(yambo_input,yambo_output, 2, freq)
        yambo_command=yambo+" -F "+yambo_output+" -J EF%d " %ifreq
        os.system(mpirun+"  "+yambo_command) 
