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


p = Path('.')

resources = r.json()['Resources']

for item in resources:
#	print(item)
	if not os.path.exists(item['Section']):
		os.makedirs(item['Section'])
		print("new directory: "+item['Section'])
	else:
		print(item['Section']+' directory exists')

	itemPath = item['Section']+'/'+item['ID']+'.md'

	header = "---\ntitle: "+item['Name']+"\ndate updated: "+str(updatedOn)+"\ncategory: "+item['Section']+"\n---\n"

	with open(Path(itemPath), 'w') as mark:
            #print(newLoc)

            mark.write(header)



