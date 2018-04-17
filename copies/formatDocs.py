#!formatDocs.py : turn tpl.files into beautiful, beautiful markdown in the correct subfolders/etc in /content
from pathlib import *
from shutil import copy2
from bs4 import BeautifulSoup, SoupStrainer
import html5lib
from markdownify import markdownify as md
import stat
import os

def createLoc(item):
    #print(str(item.parents[0]))
    stem = item.stem
    stem = Path(stem).stem
    newLoc = Path('../formatted/').joinpath(item.parents[0], stem)
    newLoc = newLoc.with_suffix('.md')
    #print(newLoc)

    if not newLoc.parents[0].exists() and not newLoc.parents[0].is_dir():
        newLoc.parents[0].mkdir(mode = 0o1230, parents = True)
        print(str(newLoc.parents[0])+" created!"+ str(newLoc.parents[0].stat().st_mode))

    else:
        newLoc.parents[0].chmod(0o1230)



    return(newLoc)

def format2MD(item, location):

    #print(item)
    #print(location)

    html = item.read_text('unicode_escape')

    html = "\n".join(line.lstrip() for line in html.split("\n"))

    soup = BeautifulSoup(html, 'html5lib')

    title = (str(location).replace('-', ' ')).title()
    date = '2018-04-16'

    header = '---\ntitle: '+title+'\ndate: '+date+'\n---\n'
    print(header)

    text = []

    text.append(header)



    for tag in soup.find_all(['html', 'head', 'body', 'div', 'section']):
        if 'class' in tag.attrs:
            if 'alert' in tag.attrs['class']:
                #print(tag.attrs['class'])
                continue
            else:
                tag.unwrap()
        else:
            tag.unwrap()

    for tag in soup.find_all(['em', 'i', 'strong', 'b']):
        if 'class' in tag.attrs:
            if tag.attrs['class'] == 'fa fa-link':
                tag.clear()
        else:
            continue

    for tag in soup.find_all('a'):
        #print(tag.attrs)
        if 'href' in tag.attrs: 
            tag.string = '['+str(tag.string).strip()+']('+tag['href']+')'

        tag.unwrap()

    for tag in soup.find_all('table'):
        for item in soup.find_all('thead'):
            item.unwrap()
        #tag.unwrap()

    for tag in soup.find_all('code'):
        tag.string = '`'+str(tag.string).strip()+'`'
        tag.unwrap()

    for tag in soup.find_all('pre'):
        tag.insert_before('\n```\n')
        tag.insert_after('\n```\n')
        source = []
        if 'source' in tag.attrs:
            source.append(tag.attrs['source'])

        if len(source) > 0:
            stringSource =  ''.join(line.lstrip() for line in source)
            if tag.string is not None:
                tag.string = (str(tag.string).strip()).join(stringSource)
            else:
                tag.string = stringSource

            
        for item in  tag.children:
            if item.name == 'span':
                item.string = str(item.string).strip()
                item.unwrap()
                #print(item)
        ss = []
        for item in tag.stripped_strings:
            ss.append(item)
        tag.string = "\n".join(line.lstrip() for line in ss)
        tag.unwrap()

    for tag in soup.find_all('span'):
        tag.string = str(tag.string).strip()
        #tag.unwrap()


    for tag in soup.find_all(['li']):
        tag.insert_before(soup.new_tag('br'))
        tag.string = '\n- '+str(tag.string).strip()+''
        

        if 'ul' in tag.parent.name:
            tag.parent.insert_before(soup.new_tag('br'))
            #tag.parent.insert_after(soup.new_tag('br'))

            tag.parent.unwrap()

        tag.unwrap()

    for tag in soup.find_all('h2'):
        container = []
        if len(tag.contents) > 0:
            for item in tag.children:
                print(item.name)
                if item.string is not None:
                    container.append(item)
            if len(container) > 0:
                if tag.string is not None:
                    tag.string = ' '.join(line.lstrip() for line in container)
                else:
                    tag.string = str(tag.string).strip()
                tag.string = '\n##'+str(tag.string).strip()+'\n'
            tag.unwrap()

        else:
            tag.string = '## '+str(tag.string).strip()+'\n'
            tag.unwrap()

    for tag in soup.find_all('h3'):
        tag.string = '### '+str(tag.string).strip()+'\n'
        tag.unwrap()

    for tag in soup.find_all('p'):

        if tag.string is not None:
            tag.string = '\n'+str(tag.string).strip()+'\n'
            tag.insert_after(soup.new_tag('br'))
            tag.unwrap()
        else:
            tag.unwrap()


        #tag.string = '*'+str(tag.string).strip()+'*'
       #print(tag)
       


    for tag in soup.find_all('br'):
        tag.replace_with('\n')



    text.append(str(soup.prettify()))
        


    #print(text)
#        text += '# '+soup.h1.get_text()
#    if soup.h2 is not None:
#        text+= '## '+soup.h2.get_text()
#    if soup.p is not None:
#        text+= soup.p.get_text()
#    if soup.table is not None:
#        text+= soup.table.get_text()
#    if soup.code is not None:
#        text+= '`\n'+soup.code.get_text()+'\n`'

    #for string in soup.stripped_strings:
        #print(repr(string))


    return(text)

def main():

    p = Path('.')

    tpl = list(p.glob('frameworks-and-sdks/**/*.tpl.html'))

    print("Total Files To Process: "+str(len(tpl)))
    #del tpl[5:]
    print("New Total Files To Process: "+str(len(tpl)))

    pages = dict()

    for item in tpl:
        
        location = createLoc(item)
        print(location.stem)
        page = format2MD(item, location.stem)
        pages[location] = page

    for key, value in pages.items():
        print(key.parents[0])
        os.chmod(key.parents[0], 0o1230)
        with open(key, 'w', encoding='unicode_escape') as mark:
            print(key)
            for item in value:
                
                mark.writelines(item)


main()
