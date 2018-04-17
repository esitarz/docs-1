#!formatDocs.py : turn tpl.files into beautiful, beautiful markdown in the correct subfolders/etc in /content
from pathlib import *
from shutil import copy2
from bs4 import BeautifulSoup, SoupStrainer
import html5lib
import html2text
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
    print(location.parts)

    category = str(location.parts[3])
    category = (category.replace('-', ' ')).title()



    title = category+': '+location.stem
    title = (str(title).replace('-', ' ')).title()

    html = item.read_text('unicode_escape')

    html = "\n".join(line.lstrip() for line in html.split("\n"))

    soup = BeautifulSoup(html, 'html5lib')

    
    date = '2018-04-16'

    header = '---\ntitle: '+title+'\ndate: '+date+'\ncategory:'+category+'\n---\n'
    print(header)

    text = header

    for tag in soup.find_all(['html', 'head', 'body', 'div', 'section']):
        if 'class' in tag.attrs:
            if 'alert' in tag.attrs['class']:
                #print(tag.attrs['class'])
                continue
            else:
                tag.unwrap()
        else:
            tag.unwrap()



    for tag in soup.find_all('code'):
        tag.string = '`'+str(tag.string).lstrip()+'`'
        tag.unwrap()

    for tag in soup.find_all('pre'):
        tag.insert_before('```')
        tag.insert_after('```')
        source = []
        if 'class' in tag.attrs and tag.string is not None:
            tag.string.join(tag.attrs['class'])
        if 'source' in tag.attrs:
            source.append(tag.attrs['source'])

        if len(source) > 0:
            stringSource =  ''.join(line.lstrip() for line in source)
            if tag.string is not None:
                tag.string = (str(tag.string).lstrip()).join(stringSource)
                tag.string += '\n'
            else:
                tag.string = stringSource
                tag.string += '\n'

 

    format_html = html2text.HTML2Text()
    format_html.MARK_CODE = False
    format_html.bypass_tables = True
    format_html.WRAP_LINKS = False
    format_html.DEFAULT_IMAGE_ALT = "Image Here"
    format_html.IMAGES_TO_ALT = False
    format_html.SINGLE_LINE_BREAK = True


    for line in soup:
        markdown = format_html.handle(str(line).strip())
        #print(markdown)
        text+=(markdown)
    



    return(text)

def main():

    p = Path('.')

    tpl = list(p.glob('**/**/*.tpl.html'))

    print("Total Files To Process: "+str(len(tpl)))
    #del tpl[5:]
    print("New Total Files To Process: "+str(len(tpl)))

    pages = dict()

    for item in tpl:
        
        location = createLoc(item)
        print(location.stem)
        page = format2MD(item, location)
        pages[location] = page

    for key, value in pages.items():
        print(key.parents[0])
        os.chmod(key.parents[0], 0o1230)
        with open(key, 'w', encoding='utf-8') as mark:
            print(key)
            for item in value:
                
                mark.write(item)


main()
