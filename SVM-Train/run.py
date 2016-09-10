import os
import sys
import string
import subprocess

settings = [(100000,1000),
			(500000,1000),
			(1000000,1000),
			(1500000,1000),
			(2000000,1000),
			(2500000,1000)]

# main
for setting in settings:
	subprocess.Popen(["python","worker.py",str(setting[0]),str(setting[1])])
