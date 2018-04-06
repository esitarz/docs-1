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
        newLoc = target.joinpath(item.relative_to(p).parents[1])

        if newLoc.exists() and newLoc.is_dir():
            print(str(newLoc)+" exists!")
        else:
            newLoc.mkdir(parents = True)
            print(str(newLoc)+" created!")

        newLoc = newLoc.with_name(item.name)


        copy2(item, newLoc)

        #print(str(newLoc))
