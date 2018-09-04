from os import walk
import csv
import numpy as np

all_files = []

mypath = './'

for (dirpath, dirnames, filenames) in walk(mypath):
    all_files = filenames 

wav_files = [ fi for fi in all_files if fi.endswith(".wav") ]

wav_files.sort()

with open('sayit.csv', 'w', newline='') as csvfile:
    sayitwriter = csv.writer(csvfile, delimiter=',')

    for g in wav_files:
        if(g.startswith('0_')):
            sayitwriter.writerow([g] + ['0.0'])
        elif(g.startswith('1_')):
            sayitwriter.writerow([g] + ['1.0'])
        else:
            raise ValueError('wav file without correct prefix: _0 or _1')
            
