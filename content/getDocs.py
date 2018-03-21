from pathlib import Path
from bs4 import BeautifulSoup
import markdown
import requests
import json
import os
from datetime import *


d = requests.get('https://api.ordercloud.io/env')

r = requests.get('https://api.ordercloud.io/v1/docs')

apiBuilt = d.json()['BuildDate']
#print(apiBuilt)

updatedOn = datetime.strptime(apiBuilt, "%Y-%m-%dT%H:%M:%S+00:00")


p = Path('**/api-reference/*.md')
rootLoc = Path('content/api-reference')
print(str(rootLoc))


resources = r.json()['Resources']

if not os.path.exists(rootLoc):
	print("MAKING DIR "+str(rootLoc))
	os.makedirs(rootLoc)


for item in resources:
	#print(item)
	itemPath = item['ID']+'.md'

	header = "---\ntitle: "+item['Name']+"\ndate: "+str(updatedOn)+"\ncategory: "+str(rootLoc)+"\ntags: "+item['Section']+"\nslug: "+item['ID']+"\n---\n"

	with open(str(rootLoc)+'/'+itemPath, 'w') as mark:
            #print(newLoc)

            mark.write(header)
            mark.write(str(item['Endpoints']))



