#!/usr/bin/env python

import os
import re
import sys
import Tkinter

import Test
Test.initialise()

# Uncomment these to modify period between tests and how much output
# to print:
#Test.setdelay(1000)
#Test.setverbose(1)

# Ignore Tkinter test since it does not test any Pmw functionality
# (only Tkinter) and it fails under MS-Windows 95 (and it hasn't been
# kept up-to-date with changes to Tk.
if Tkinter.TkVersion >= 8.4:
    # Also ignore Blt test since it causes Blt 2.4z to core dump.
    ignoreTests = ('Tkinter_test.py', 'Blt_test.py')
else:
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
