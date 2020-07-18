#! /usr/bin/env python

import os, sys

scr = "~/code/scripts/setbg.sh"

try:
    filename = os.path.join(os.getcwd(),sys.argv[1])
except:
    print("usage: wallpaper.py [filename]")
    exit()

shebang = "echo '#! /bin/sh\n' > {}".format(scr)
command = "echo 'exec feh --bg-center {} &' >> {}".format(filename, scr)

if os.path.isfile(filename):
    print("setting background: {}".format(filename))
    os.system(shebang)
    os.system(command)
    os.system("feh --bg-center {}".format(filename))
else:
    print("does not exists")

# i english talk good yes
