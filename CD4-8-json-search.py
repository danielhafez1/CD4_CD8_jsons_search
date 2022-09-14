import json
import requests  
import pickle
import datetime
import csv
import pandas as pd
import numpy as np
import re
from collections import Counter
import pandas as pd
import glob
import os
import argparse


#path = "/Users/daniel/Desktop/Master-Project/ireceptor_script-main/tests/CSARAGGNTGELFF2"
path = "/Users/daniel/Desktop/CSARRQGNTGELFF"
#path = "/Users/daniel/Desktop/Master-Project/ireceptor_script-main/tests/CSARRQGNTGELFF"

json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
print(json_files)

data_total = pd.DataFrame()
#print(json_files)


for i in json_files:

	file_name = path + "/{0}".format(i)
	print(file_name)
	
	f = open(file_name)
	data = json.load(f)
	data = data["Repertoire"]
	data1 = pd.json_normalize(data)
	data2 = pd.DataFrame(data1)
	
	data_total = data_total.append(data2)
	data_total = data_total.reset_index(drop = True)











#end = path + "/data_TRA_CSARRQGNTGELFF.csv"
end = path + "/JSON_ANALYSE.csv"
#end = path + "/data_TRA_CSARDGGNTGELFF.csv"


data_total.to_csv(end, index = False)




df = pd.read_csv(end)
all_phenotype = ["None"] * len(df['sample'])



for index,i in enumerate(df['sample']):

	
	try:

		if "cell_subset':" in i:
			

			phenotype_tmp = re.search("'cell_subset': (.+?)}", i)
			
			
			cell_subset = phenotype_tmp.group(1)
			

			if "CD4-positive" in cell_subset:
				all_phenotype[index] = "CD4-positive"

			elif "CD8-positive" in cell_subset:
				all_phenotype[index] = "CD8-positive"

			else:
				all_phenotype[index] = "None"



		else:
			continue

	except:
		all_phenotype[index] = "None"


print(f'"CD4-positive" appears {all_phenotype.count("CD4-positive")} time(s)')

print(f'"CD8-positive" appears {all_phenotype.count("CD8-positive")} time(s)')





