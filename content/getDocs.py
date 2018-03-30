#!python script to format api-reference into markdown files
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
from tabulate import tabulate



d = requests.get('https://api.ordercloud.io/env')

r = requests.get('https://api.ordercloud.io/v1/docs')

sections = r.json()['Sections']
resources = r.json()['Resources']
roles = r.json()['Roles']

def unwrap_list(input):

	contents = []
	for item in input:
		text = pypandoc.convert_text(item, 'gfm', format='rst')
		text = format(text)
		contents.append(text)


	return(contents) #LIST of strings

def define_meta(item):
	#print(item)

	page = dict([('title', ''),('date', ''),('category', ''),('tags', ''),('slug', ''), ('comments',''), ('endpoints','')])

	page['title'] = str(item['Name'])
	page['date'] = str(date.today())

	tags = re.findall('[A-Z][^A-Z]*', str(item['Section']))
	tagList = ' '.join(str(e) for e in tags)
	tagSlug = '-'.join(str(e) for e in tags)
	#print(catList)
	page['tags'] = tagList
	page['category']= 'API Reference'
	page['slug']=tagSlug+'-'+str(item['ID'])
	page['comments'] = item['Comments']
	page['endpoints'] = item['Endpoints']

	header = ("---\ntitle: "+page['title']+"\ndate: "+page['date']+"\ncategory: "+page['category']+"\ntags: "+page['tags']+"\nslug: "+page['slug']+"\n---\n")

	return(header)

def returnSplit(input):
	text = ' '.join(re.findall('[A-Z][^A-Z]*', input))
	return(text)

def parseSample(input):
	contents = ''
	body = json.loads(input['Sample'])
	text = str(json.dumps(body, sort_keys=True, indent=4))
	#print(text)
	tabbed = text.replace('\n','\n\t')
	#print(tabbed)
	peskyCurlies = re.compile('^{')
	tabbed = re.sub(peskyCurlies, '\n\t{', tabbed)
	#print(tabbed)
	contents += '\n\t:::json'+tabbed+'\n\n'
	return(contents)

def parseList(input):
	contents =''
	table = ''
	columns = []
	rows = []
	if len(input) > 0:
		for bullet in input:
			if type(bullet) is str:
				contents += ' '+bullet
			elif type(bullet) is dict:
				row = '|'
				for item in bullet.keys():
					row += ' '+str(bullet[item])+' |'
				column = ' | '.join(bullet.keys())
				columns.insert(0, column+' | ')
				rows.append(row)
				table = '\n'.join(rows)

				if columns:
					table = '\n| '+columns[0]+'\n|---|---|---|---|\n'+table+'\n'
				else:
					table = ''
		contents += '\n'+table


		#print(contents)

	return(contents)

def parseFields(input):
	contents =''
	table = ''
	columns = []
	rows = []
	for bullet in input['Fields']:
		#print(type(bullet))
		if type(bullet) is str:
			contents += ' '+bullet
		if type(bullet) is dict:
			first = True
			row = '|'

			for item in bullet.keys():
				row += ' '+str(bullet[item])+' |'
		column = ' | '.join(bullet.keys())
		columns.insert(0, column+' | ')
		rows.append(row)
		table = '\n'.join(rows)

	if columns:
		table = '\n| '+columns[0]+'\n|---|---|---|---|\n'+table+'\n'
	else:
		table = ''
	contents += table

	return(contents)


def main():

	pages = []

	print("Total Files To Process: "+str(len(resources)))
	#del resources[5:]
	#print("New Total Files To Process: "+str(len(resources)))

	p = Path('.')

	files = list(p.glob('**/api-reference/*.md'))
#	print(files)

	lastMod = datetime.utcfromtimestamp(p.stat().st_mtime)
	docsUpdated = datetime.strptime(d.json()['CommitDate'], "%Y-%m-%dT%H:%M:%S+00:00")  #2018-03-21T22:18:13+00:00
	print("Docs Content Last Modified: %s" % lastMod)

	print('Generated Docs Last Updated:'+str(docsUpdated))

	if lastMod >= docsUpdated:
		print('Docs are up to date!'.title())
	#TODO: for server, use ^ to distinguish if docs need updating

	rootLoc = Path('content/api-reference')


	for p in resources:
		itemPath = p['ID']+'.md'
		page = dict([('path', ''),('contents', '')])
		page['path'] = str(rootLoc)+'/'+itemPath
		title = str(p['Name'])
		meta = define_meta(p)
		print('updating... '+page['path'])
		page['contents'] += meta

		section = resources[resources.index(p)]
		#print('\nSECTION: ')
		#print(section['Comments'])

		#page['contents'] += '\n## Comments: \n'



		if type(section['Comments']) is list and len(section['Comments']) == 0:
			page['contents'] += '\n'

		elif type(section['Comments']) is str:

			page['contents'] += pypandoc.convert_text(section['Comments'], 'gfm', format='rst')

		elif type(section['Comments']) is int:
				#unwrap_str(v)
			page['contents'] += '`'+str(section['Comments'])+'`'
			page['contents'] += '\n---\n'


		elif type(section['Comments']) is list:
			text = unwrap_list(section['Comments'])
			page['contents'] += ' '.join(text)
			page['contents'] += '\n---\n'


		endpoints = section['Endpoints']
		#section = resources[resources.index(p)]
		for item in endpoints:
			#print('\nSECTION: ')

			for key, value in endpoints[endpoints.index(item)].items():
				#print(key)

				#print(key, value)


				if key == 'HttpVerb':
					page['contents'] += '\n## `'+value+'`'.title()

				elif key == 'UriTemplate':
					page['contents'] += ' `'+value+'`'
					page['contents'] += '\n'+endpoints[endpoints.index(item)]['Name']+''.title()

				elif key == 'ID':
					continue

				elif key == 'RequestBody' and value == None:
					continue
				elif key == 'RequestBody' and value != None:
					page['contents'] += '\n## '+returnSplit(str(key)).title()
					if type(value) == dict:
						page['contents'] += parseSample(value)
						#print(page['contents'])
						page['contents'] += parseFields(value)




				elif key == 'ResponseBody' and value == None:
					page['contents'] += '\n## '+returnSplit(str(key)).title()
				elif key == 'ResponseBody' and value != None:
					page['contents'] += '\n## '+returnSplit(str(key)).title()
					if type(value) == dict:
						page['contents'] += parseSample(value)
						page['contents'] += parseFields(value)

						#print(value.keys())

					elif key == 'ResponseStatus':
						page['contents'] += '\n**'+returnSplit(str(key)).title()+'**: `'+str(value)+'`\n'

				if key == 'Parameters' and len(value) == 0:
					continue

				if key == 'Parameters' and type(value) is list:
							#unwrap_list(v)
							page['contents']+=parseList(value)




		pages.append(page)
			#print(pages)

	for page in pages:
		with open(page['path'], 'w') as mark:
			mark.write(page['contents'])

	last_updated = str(date.today())

			#print(contents)


main()


#	def unwrap_list(input):
