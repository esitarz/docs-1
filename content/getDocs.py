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

last_updated = None

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

def unwrap_str(input):
	#print('UNWRAP THE STRINGS!')
	#print(input)
	contents = ''
	text = ''
	text = '\n '
	text += pypandoc.convert_text(input, 'gfm', format='rst')
	text = '\n'
	contents += text

	return(contents)

def unwrap_dict(input):
	contents = ''

	#print(input)
	#print(type(input))
	if type(input) is dict:
		for key, value in input.items():
			text = '\n### '+str(key)
			if type(value) is dict:
				
				text += unwrap_dict(value)

			elif type(value) is list:
				
				contents += unwrap_list(value)

			elif type(value) is str:
				
				contents += unwrap_str(value)
	else:
		contents += str(input) 
		#contents += pypandoc.convert_text(str(input), 'gfm', format='md')


	return(contents)

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
	text = str(json.dumps(body, sort_keys=True, indent=4, separators=(',', ': ')))
	#print(text)
	tabbed = text.replace('\n','\n\t')
	peskyCurlies = re.compile('^{')
	tabbed = re.sub(peskyCurlies, '\n\t{', tabbed)
	contents += tabbed
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


	p = Path('**/api-reference/*.md')
	rootLoc = Path('content/api-reference')

	for p in resources:
		itemPath = p['ID']+'.md'
		page = dict([('path', ''),('contents', '')])
		page['path'] = str(rootLoc)+'/'+itemPath
		title = str(p['Name'])
		meta = define_meta(p)
		print(page['path'])
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
					page['contents'] += '\n## '+returnSplit(str(key)).title()
				elif key == 'RequestBody' and value != None:
					page['contents'] += '\n## '+returnSplit(str(key)).title()
					if type(value) == dict:
						page['contents'] += parseSample(value)
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


				
				#print(type(value))
				#if type(value) is str:
						#unwrap_str(v)
				#	page['contents'] += pypandoc.convert_text(value, 'gfm', format='rst')

				#elif type(value) is int:
						#unwrap_str(v)
				#	page['contents'] += '`'+str(value)+'`'
				#	page['contents'] += '\n---\n'

				if key == 'Parameters' and len(value) == 0:
					continue

				if key == 'Parameters' and type(value) is list:
							#unwrap_list(v)
					page['contents'] += '\n\n| '+'Parameters'.ljust(15)+' | '+'Description'.ljust(30)+' |\n'
					page['contents'] += '|'.ljust(19, '-')+'|'.ljust(34, '-')+'|\n'
					for bullet in value:
						#print(type(bullet))
						if type(bullet) is str:
							page['contents'] += ' '+bullet
						if type(bullet) is dict:
												
							for k, v in bullet.items():
								if k == "Name":
									page['contents'] += '\n\n| '+'Parameters'.ljust(15)+' | '+'Description'.ljust(30)+' |\n'
									page['contents'] += '|'.ljust(19, '-')+'|'.ljust(34, '-')+'|\n'
								page['contents'] += '| '+k.ljust(15)+' | '+str(v).ljust(30)+' |\n'
							#page['contents'] += table


										

		pages.append(page)
			#print(pages)
								
	for page in pages:
		with open(page['path'], 'w') as mark:
			mark.write(page['contents'])


			#print(contents)


main()


#	def unwrap_list(input):

