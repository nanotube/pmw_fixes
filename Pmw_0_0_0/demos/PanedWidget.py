title = 'Pmw.PanedWidget demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):
	self.paneCount = 0

	# Create a main PanedWidget with top and bottom panes.
	pane = Pmw.PanedWidget(parent, hull_width=400, hull_height=300)
	pane.add('top', min=100)
	pane.add('bottom', min=100)

	# Create three panes in the top pane.
	topPane = Pmw.PanedWidget(pane.pane('top'), orient='horizontal',
            hull_width=0, hull_height=0)
	for num in range(4):
	    if num == 1:
		name = 'Fixed\nsize'
		topPane.add(name, min = .2, max = .2)
	    else:
		name = 'Pane\n' + str(num)
		topPane.add(name, min = .1, size = .25)
	    button = Tkinter.Button(topPane.pane(name), text = name)
	    button.pack(expand = 1)

	topPane.pack(expand = 1, fill='both')

	# Create a "pane factory" in the bottom pane.
	label = Tkinter.Label(pane.pane('bottom'),
		pady = 10,
		text = 'Below is a "pane factory".\n' +
			'Drag the handle on the left\nto create new panes.')
	label.pack()
	self.bottomPane = Pmw.PanedWidget(pane.pane('bottom'),
		orient='horizontal',
		command = self.resize,
		hull_borderwidth = 1,
		hull_relief = 'raised',
		hull_width=0, hull_height=0
                )
	self.bottomPane.add('starter', size = 0.0)
	self.bottomPane.add('main')
	button = Tkinter.Button(self.bottomPane.pane('main'),
		text = 'Pane\n0')
	button.pack(expand = 1)
	self.bottomPane.pack(expand = 1, fill = 'both')
	pane.pack(expand = 1, fill = 'both')

    def resize(self, list):
	pane = self.bottomPane
	# Remove any panes less than 2 pixel wide.
	for i in range(len(list) - 1, 0, -1):
	    if list[i] < 2:
		pane.delete(i)

	# If the user has dragged the left hand handle, create a new pane.
	if list[0] > 1:
	    self.paneCount = self.paneCount + 1

	    # Add a button to the new pane.
	    name = pane.panes()[0]
	    text = 'Pane\n' + str(self.paneCount)
	    button = Tkinter.Button(pane.pane(name), text = text)
	    button.pack(expand = 1)

	    # Create a new starter pane.
	    name = 'Pane ' + str(self.paneCount)
	    pane.insert(name, size=0.0)

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme = 'pmw1')
    root.title(title)

    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()
