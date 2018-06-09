#!/usr/bin/python

import os
import sys
import Image

size = 128, 128

for root, subFolders, files in os.walk("/home/peter/dev/machine-learning/workshop-2018-06/data"):
        for file in files:
            try:
                outfile = os.path.join(root, file)
                print("resizing " + outfile)
                im = Image.open(outfile)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile, "JPEG")
            except IOError:
                print "cannot create thumbnail for '%s'" % file
