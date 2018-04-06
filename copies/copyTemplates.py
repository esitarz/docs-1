#! to copy template files from devcenter  >> copies folder
#one time only script

from pathlib import *
from shutil import copy2
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')
repos = config['REPOS']

p = Path(repos['devcenter']+'src/app/documentation')

tpl = list(p.glob('**/**/templates/*.tpl.html'))

target = Path(repos['docs']+'copies')

if target.exists() and target.is_dir():
    for item in tpl:
        newLoc = target.joinpath(item.relative_to(p).parents[0])
        print("parent location: ".ljust(25)+str(newLoc).ljust(30))

        if not newLoc.exists() and not newLoc.is_dir():
            newLoc.mkdir(parents = True)
            print(str(newLoc)+" created!")

        newLoc = newLoc.with_name(item.name)
        print("final file location: ".ljust(25)+str(newLoc).ljust(30))


        copy2(item, newLoc)

        #print(str(newLoc))
