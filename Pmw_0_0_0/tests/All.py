#!/usr/bin/env python

import os
import re
import sys

import Test
Test.initialise()

# Uncomment these to modify period between tests and how much output
# to print:
#Test.setdelay(1000)
#Test.setverbose(1)

# Ignore Tkinter test since it does not test any Pmw functionality
# (only Tkinter) and it fails under MS-Windows 95.
ignoreTests = ('Tkinter_test.py',)

allTestData = ()
files = os.listdir(os.curdir)
files.sort()

for file in files:
    if file not in ignoreTests and re.search('^.+_test.py$', file) is not None:
	test = file[:-3]
	exec 'import ' + test
	exec 'allTestData = allTestData + ' + test + '.testData'

Test.runTests(allTestData)
