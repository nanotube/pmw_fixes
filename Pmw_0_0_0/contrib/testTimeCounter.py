""" Demonstration of the Pmw FullTimeCounter megawidget.
"""

# Import Pmw from the sibling directory.
#import sys
#sys.path[:0] = ['../../..']

import string
import Tkinter
import Pmw
import PmwFullTimeCounter

class Demo:
    def __init__(self, parent):
	self._time = PmwFullTimeCounter.FullTimeCounter(parent,
		labelpos = 'n',
		label_text = 'YYYY:MM:DD:HH:mm')
	self._time.pack(fill = 'both', expand = 1, padx=10, pady=5)

	button = Tkinter.Button(parent, text = 'Show', command = self.show)
	button.pack()

    def show(self):
	stringVal = self._time.getstring()
	print stringVal

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme = 'pmw1')
    root.title('FullTimeCounter')

    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()
