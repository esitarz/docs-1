#!formatDocs.py : turn tpl.files into beautiful, beautiful markdown in the correct subfolders/etc in /content
from pathlib import *
from shutil import copy2
from bs4 import BeautifulSoup

def copyFile(listPaths, target):
    if target.exists() and target.is_dir():
        for item in listPaths:
            newLoc = target.joinpath(item.relative_to(p).parents[0])
            print("parent location: ".ljust(25)+str(newLoc).ljust(30))

            if not newLoc.exists() and not newLoc.is_dir():
                newLoc.mkdir(parents = True)
                print(str(newLoc)+" created!")

            newLoc = newLoc.with_name(item.name)
            print("final file location: ".ljust(25)+str(newLoc).ljust(30))


            copy2(item, newLoc)
    return(newLoc)

def main():

    p = Path('.')

    tpl = list(p.glob('**/**/*.tpl.html'))

    print("Total Files To Process: "+str(len(tpl)))
    del tpl[5:]
    print("New Total Files To Process: "+str(len(tpl)))

    for item in tpl:
        soup = BeautifulSoup(item.read_text('unicode_escape'), 'html.parser')
        print(item)
        if soup.h1 is not None: print('# '+soup.h1.get_text())
        if soup.h2 is not None: print('## '+soup.h2.get_text())
        if soup.p is not None: print(soup.p.get_text())

        print(soup.code)




    #print(str(tpl))





main()
