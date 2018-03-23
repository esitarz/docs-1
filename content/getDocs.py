from pathlib import Path
from bs4 import BeautifulSoup
import markdown
import requests
import json
import os
from datetime import *
from string import *
import re
import pypandoc


def make_subdirectories(rootLoc):

	if not os.path.exists(rootLoc):
		print("MAKING DIR "+str(rootLoc))
		os.makedirs(rootLoc)

def write_docs(rootLoc, itemPath, page):
	contents = ''
	header = ("---\ntitle: "+page['title']+"\ndate: "+page['date']+"\ncategory: "+page['category']+"\ntags: "+page['tags']+"\nslug: "+page['slug']+"\n---\n")

	for item in list(page['contents'].keys()):
		print(item)
		for value in list(page['contents'].values()):
			print(''.join(str(e) for e in value))

		content = ''
	#content += item.values()
		#content += ''.join(item)
		#print(content)
	#print(content)
		contents += ''.join(str(e) for e in content)

	with open(str(rootLoc)+'/'+itemPath, 'w') as mark:
		mark.write(''.join(header))



	with open(str(rootLoc)+'/'+itemPath, 'a') as mark:
		mark.write(contents)
		


def scrape_docs(resources):
	
	resourceKeys= list(resources[0].keys())
	pages =[]


	for item in resources:
		#print(item)
		
		page = dict([('title', ''),('date', ''),('category', ''),('tags', ''),('slug', '')])
		
		page['title'] = str(item['Name'])
		page['date'] = str(date.today())
		tags = re.findall('[A-Z][^A-Z]*', str(item['Section']))
		tagList = ' '.join(str(e) for e in tags)
		#print(catList)
		page['tags'] = tagList
		page['category']= 'API Reference'
		page['slug']=str(item['ID'])

		#print(item['Endpoints'])
		pageContents = dict.fromkeys(item['Endpoints'].values())
		print(pageContents)
		pages.append(page)
		#for key in resourceKeys:
		#print(page.items())
		

	return(pages)
	

def format_content(pages, rootLoc):


	
	for page in pages:
		header =[]
		contents = []

		for item in page['contents']:
			content = dict.fromkeys(item.keys())

			for key in item.keys():

				value = (item[key])
				content[key]=(value)

			#print(content)
			for k, v in content.items():
				formatted = []
				formatted.append("## {0}\n {1}\n---\n".format(k,v))
				#print(formatted)
				content[k]=(str(formatted))

			page['contents'] = content

		#print(page)

			itemPath = page['slug']+'.md'

			write_docs(rootLoc, itemPath, page)

		



def main():

	d = requests.get('https://api.ordercloud.io/env')

	r = requests.get('https://api.ordercloud.io/v1/docs')

	apiBuilt = d.json()['BuildDate']
	updatedOn = datetime.strptime(apiBuilt, "%Y-%m-%dT%H:%M:%S+00:00")


	p = Path('**/api-reference/*.md')
	rootLoc = Path('content/api-reference')
	#print(str(rootLoc))

	parents = str(rootLoc).replace('-', ' ') 
	parents = parents.title()
	parents = parents.split('\\')

	sections = r.json()['Sections']
	resources = r.json()['Resources']
	roles = r.json()['Roles']

	pages = []

	make_subdirectories(rootLoc)
	
	format_content(scrape_docs(resources), rootLoc)






main()



# TODO: better formatting for contents
# TODO: run in build if updated last < build date