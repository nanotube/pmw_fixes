title = 'Pmw.ScrolledFrame demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):
	# Create the ScrolledFrame.
	self.sf = Pmw.ScrolledFrame(parent,
		labelpos = 'n', label_text = 'ScrolledFrame',
		usehullsize = 1,
		hull_width = 400,
		hull_height = 220,
	)

	# Create a group widget to contain the flex options.
	w = Pmw.Group(parent, tag_text='Flex')
	w.pack(side = 'bottom', padx = 5, pady = 3)

	hflex = Pmw.OptionMenu(w.interior(),
		labelpos = 'w',
		label_text = 'Horizontal:',
		items = ['fixed', 'expand', 'shrink', 'elastic'],
		command = self.sethflex,
		menubutton_width = 8,
	)
	hflex.pack(side = 'left', padx = 5, pady = 3)
	hflex.invoke('fixed')

	vflex = Pmw.OptionMenu(w.interior(),
		labelpos = 'w',
		label_text = 'Vertical:',
		items = ['fixed', 'expand', 'shrink', 'elastic'],
		command = self.setvflex,
		menubutton_width = 8,
	)
	vflex.pack(side = 'left', padx = 5, pady = 3)
	vflex.invoke('fixed')

	# Create a group widget to contain the scrollmode options.
	w = Pmw.Group(parent, tag_text='Scroll mode')
	w.pack(side = 'bottom', padx = 5, pady = 0)

	hmode = Pmw.OptionMenu(w.interior(),
		labelpos = 'w',
		label_text = 'Horizontal:',
		items = ['none', 'static', 'dynamic'],
		command = self.sethscrollmode,
		menubutton_width = 8,
	)
	hmode.pack(side = 'left', padx = 5, pady = 3)
	hmode.invoke('dynamic')

	vmode = Pmw.OptionMenu(w.interior(),
		labelpos = 'w',
		label_text = 'Vertical:',
		items = ['none', 'static', 'dynamic'],
		command = self.setvscrollmode,
		menubutton_width = 8,
	)
	vmode.pack(side = 'left', padx = 5, pady = 3)
	vmode.invoke('dynamic')

        buttonBox = Pmw.ButtonBox(parent)
	buttonBox.pack(side = 'bottom')
	buttonBox.add('add', text = 'Add a\nbutton', command = self.addButton)
	buttonBox.add('yview', text = 'Show\nyview', command = self.showYView)
	buttonBox.add('scroll', text = 'Page\ndown', command = self.pageDown)
	buttonBox.add('center', text = 'Center', command = self.centerPage)

	# Pack this last so that the buttons do not get shrunk when
	# the window is resized.
	self.sf.pack(padx = 5, pady = 3, fill = 'both', expand = 1)

	self.frame = self.sf.interior()

	self.row = 0
	self.col = 0

	self.addButton()

    def sethscrollmode(self, tag):
	self.sf.configure(hscrollmode = tag)

    def setvscrollmode(self, tag):
	self.sf.configure(vscrollmode = tag)

    def sethflex(self, tag):
	self.sf.configure(horizflex = tag)

    def setvflex(self, tag):
	self.sf.configure(vertflex = tag)

    def addButton(self):
	button = Tkinter.Button(self.frame,
	    text = '(%d,%d)' % (self.col, self.row))
	button.grid(row = self.row, col = self.col, sticky = 'nsew')

	self.frame.grid_rowconfigure(self.row, weight = 1)
	self.frame.grid_columnconfigure(self.col, weight = 1)
	self.sf.reposition()

	if self.col == self.row:
	    self.col = 0
	    self.row = self.row + 1
	else:
	    self.col = self.col + 1

    def showYView(self):
        print self.sf.yview()

    def pageDown(self):
        self.sf.yview('scroll', 1, 'page')

    def centerPage(self):
        top, bottom = self.sf.yview()
        size = bottom - top
        middle = 0.5 - size / 2
        self.sf.yview('moveto', middle)

######################################################################
 
# Create demo in root window for testing.
if __name__ == '__main__': 
    import os
    if os.name == 'nt':
        size = 16
    else:
        size = 12
    root = Tkinter.Tk()
    Pmw.initialise(root, size = size, fontScheme = 'pmw2')
    root.title(title)
 
    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop() 
