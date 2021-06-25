import os
import shutil
import pandas as pd
import subprocess
import stat

mol2_list = []
working_dir = os.getcwd() + '/'
for r, d, f in os.walk(working_dir):
	for file in f:
		if '.sdf' in file:
			mol2_list.append(file)

df = pd.DataFrame(columns=['CAS','MW', 'logD', 'H_don', 'H_acc', 'PSA', 'n_rot', 'logS'])

for mol2_file in mol2_list:
	
	mol2_name = mol2_file
	mol2_base = mol2_file.split('.')
	mol2_base = mol2_base[0]

	runscript = open('runscript_marvin.sh','w')
	runscript.write('#!/bin/bash')
	runscript.write('\n')
	runscript.write('cxcalc mass logD -H 7.4 donorcount -H 7.4 acceptorcount -H 7.4 logS -H 7.4 psa rotatablebondcount ' + mol2_name + ' >> ' + mol2_base + '.out')
	runscript.close()
	
	# executable
	st = os.stat('runscript_marvin.sh')
	os.chmod('runscript_marvin.sh', st.st_mode | stat.S_IEXEC)

	# subprocess
	process = subprocess.Popen(['bash', 'runscript_marvin.sh'])
	print('calculating descriptors for ' + mol2_base)
	process.wait()

print('______cxcalc calculation done_______')

outfile_list = []
working_dir = os.getcwd() + '/'
for r, d, f in os.walk(working_dir):
	for file in f:
		if '.out' in file:
			outfile_list.append(file)

i=0
for outfile in outfile_list:
	outfile_o = open(outfile,'r')
	outfile_c = outfile_o.read()
	
	outfile_split = outfile_c.split()
	#print(outfile_split)	
	
	outfile_base = outfile.split('.')
	ZINC_ID = outfile_base[0]

	try:
		MW = outfile_split[14]
		logD = outfile_split[15]
		donorcount = outfile_split[16]
		acceptorcount = outfile_split[17]
		psa = outfile_split[18]
		nrot = outfile_split[19]
		logs = outfile_split[20]
	except:
		MW = logD = donorcount = acceptorcount = psa = nrot = logs = 'NaN'


	print(ZINC_ID + ' MW: ' + str(MW) + ' logD: ' + str(logD) + ' donorcount: ' + str(donorcount) + ' acceptorcount: ' + str(acceptorcount) + ' psa: ' + str(psa) + ' nrot: ' + str(nrot) + ' logs: ' + str(logs))

	df.loc[i,'ZINC_ID'] = ZINC_ID
	try:
		df.loc[i,'MW'] = float(MW)
	except: 
		df.loc[i,'MW'] = 'NaN'

	try:	
		df.loc[i,'logD'] = float(logD)
	except:
		df.loc[i,'logD'] = 'NaN'

	try:		
		df.loc[i,'H_don'] = int(donorcount)
	except:
		df.loc[i,'H_don'] = 'NaN'	

	try:
		df.loc[i,'H_acc'] = int(acceptorcount)
	except:
		df.loc[i,'H_acc'] = 'NaN'

	try:
		df.loc[i,'PSA'] = float(psa)
	except:
		df.loc[i,'PSA'] = 'NaN'
	
	try:
		df.loc[i,'n_rot'] = int(nrot)
	except:
		df.loc[i,'n_rot'] = 'NaN'
	
	try:
		df.loc[i,'logS'] = float(logs)
	except:
		df.loc[i,'logS'] = 'NaN'
	i=i+1

df.to_csv('PK_HIVHCV.csv')

	
