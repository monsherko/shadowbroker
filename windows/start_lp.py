#!/usr/bin/python

import os
import sys

# determine the absolute path to the disk
scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))
print "%s" % scriptDir

args = ""

for i in range(0, len(sys.argv)):
	if (len(args)):
		args = "%s %s" % (args, sys.argv[i])
	else:
		args = sys.argv[1]
	
sys.exit(os.system("python %s/configure_lp.py -load %s" % (scriptDir, args)))
