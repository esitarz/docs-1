from pathlib import Path
from bs4 import BeautifulSoup
import markdown
import requests
import json
import os
from datetime import *
from string import *
import re


d = requests.get('https://api.ordercloud.io/env')

r = requests.get('https://api.ordercloud.io/v1/docs')

apiBuilt = d.json()['BuildDate']
#print(apiBuilt)


updatedOn = datetime.strptime(apiBuilt, "%Y-%m-%dT%H:%M:%S+00:00")


p = Path('**/api-reference/*.md')
rootLoc = Path('content/api-reference')
#print(str(rootLoc))

parents = str(rootLoc).replace('-', ' ') 
parents = parents.title()
parents = parents.split('\\')

#print(parents)


resources = r.json()['Resources']


dump = json.loads(json.dumps(r.json()))
#print(contents)


sections = r.json()['Sections']
resources = r.json()['Resources']
roles = r.json()['Roles']


#print(sections)
#print(roles)

resourceKeys= list(resources[0].keys())
#print(resourceKeys)

pages =[]





if not os.path.exists(rootLoc):
	print("MAKING DIR "+str(rootLoc))
	os.makedirs(rootLoc)

for item in resources:
	#print(item)
	itemPath = item['ID']+'.md'

	page = dict([('title', ''),('date', ''),('category', ''),('tags', ''),('slug', ''),('contents', '')])
	page['title'] = str(item['Name'])
	page['date'] = str(date.today())
	tags = re.findall('[A-Z][^A-Z]*', str(item['Section']))
	tagList = ' '.join(str(e) for e in tags)
	#print(catList)
	page['tags'] = tagList
	page['category']= 'API Reference'
	page['slug']=str(item['ID'])
	page['contents']=str(item['Endpoints'])
	#for key in resourceKeys:
	print(page.items())
	
	header = "---\ntitle: "+page['title']+"\ndate: "+page['date']+"\ncategory: "+page['category']+"\ntags: "+page['tags']+"\nslug: "+page['slug']+"\n---\n"+page['contents']
	


	with open(str(rootLoc)+'/'+itemPath, 'w') as mark:
			#break
            #print(newLoc)

            mark.write(header)




# TODO: better formatting for contents
# TODO: run in build if updated last < build date