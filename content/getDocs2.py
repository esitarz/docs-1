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
	contents = ''
	text = ''
	#print(input)
	#print(type(input))
	if type(input) is list:
		for item in input:
			text += '\n## '+str(input).title()
			if type(item) is str:
				text = unwrap_str(item)
				contents += '\n'+text+'\n'
			if type(item) is list:
				text = unwrap_list(item)
				contents += '\n'+text+'\n'	
			if type(item) is dict:
				text = unwrap_dict(item)
				contents += text		


	return(contents)		

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
	#print(catList)
	page['tags'] = tagList
	page['category']= 'API Reference'
	page['slug']=str(item['ID'])
	page['comments'] = item['Comments']
	page['endpoints'] = item['Endpoints']

	header = ("---\ntitle: "+page['title']+"\ndate: "+page['date']+"\ncategory: "+page['category']+"\ntags: "+page['tags']+"\nslug: "+page['slug']+"\n---\n")

	return(header)


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
				#unwrap_str(v)
			page['contents'] += pypandoc.convert_text(section['Comments'], 'gfm', format='rst')

		elif type(section['Comments']) is int:
				#unwrap_str(v)
			page['contents'] += '`'+str(section['Comments'])+'`'
			page['contents'] += '\n---\n'


		elif type(section['Comments']) is list:
							#unwrap_list(v)
			for item in section['Comments']:
				text = pypandoc.convert_text(item, 'gfm', format='rst')
				text = format(text)
				print(text)
				page['contents'] += text
			page['contents'] += '\n---\n'
							

		endpoints = section['Endpoints']
		#section = resources[resources.index(p)]
		for item in endpoints:
			#print('\nSECTION: ')

			for key, value in endpoints[endpoints.index(item)].items():
				#print(key)

				#print(key, value)


				if key == 'HttpVerb':
					page['contents'] += '\n### `'+value+'`'.title()

				elif key == 'UriTemplate':
					page['contents'] += ' `'+value+'`'

				elif key == 'ID':
					continue

				elif key == 'Name':
					page['contents'] += '\n## '+value+''.title()

				elif key == 'RequestBody':
					page['contents'] += '\n **'+str(key).title()+'**: \n'+str(value)
				elif key == 'ResponseStatus':
					page['contents'] += '\n **'+str(key).title()+'**: `'+str(value)+'`\n'
				elif key == 'ResponseBody':
					page['contents'] += '\n **'+str(key).title()+'**: \n'+str(value)

				
				#print(type(value))
				#if type(value) is str:
						#unwrap_str(v)
				#	page['contents'] += pypandoc.convert_text(value, 'gfm', format='rst')

				#elif type(value) is int:
						#unwrap_str(v)
				#	page['contents'] += '`'+str(value)+'`'
				#	page['contents'] += '\n---\n'

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

