import pandas as pd
import os
import numpy as np

#Import the data
os.chdir('data')
paths = [d for d in os.listdir('.') if os.path.isdir(d)]
paths = np.array(paths)
dic = {}
for i in paths.astype(str):
	print(i)
	os.chdir(i)
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	data1 = pd.read_csv(files[0], delimiter='\t')
	data2 = pd.read_csv(files[1], delimiter='\t')
	frames = [data1, data2]
	dic[str(int(i))]=frames
	os.chdir('..')

	
	
		

