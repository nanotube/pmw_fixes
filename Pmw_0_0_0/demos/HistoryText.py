title = 'Pmw.HistoryText demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):
	# Create and pack the PanedWidget to hold the query and result
        # windows.
        # !! panedwidget should automatically size to requested size
        panedWidget = Pmw.PanedWidget(parent,
                orient = 'vertical',
                hull_height = 400,
                hull_width = 450)
        panedWidget.add('query', min = 0.05, size = 0.2)
        panedWidget.add('buttons', min = 0.1, max = 0.1)
        panedWidget.add('results', min = 0.05)
        panedWidget.pack(fill = 'both', expand = 1)

	# Create and pack the HistoryText.
        self.historyText = Pmw.HistoryText(panedWidget.pane('query'),
                text_wrap = 'none',
                text_width = 60,
                text_height = 10,
                statechangecmd = self.statechange,
        )
        self.historyText.pack(fill = 'both', expand = 1)
        self.historyText.statechangecmd = self.statechange
        self.historyText.component('text').focus()

        buttonList = (
            ['Prev', self.historyText.prev],
            ['Next', self.historyText.next],
            ['Search', Pmw.busycallback(self.search)],
            ['Clear', self.clear],
            ['Undo', self.historyText.undo],
            ['Redo', self.historyText.redo],
        )
        self.buttonDict = {}

        for text, cmd in buttonList:
            button = Tkinter.Button(panedWidget.pane('buttons'),
                    text = text, command = cmd)
            button.pack(side = 'left')
            self.buttonDict[text] = button

        for text in ('Prev', 'Next'):
            self.buttonDict[text].configure(state = 'disabled')

        self.results = Pmw.ScrolledText(panedWidget.pane('results'), text_wrap = 'none')
        self.results.pack(fill = 'both', expand = 1)

    def statechange(self, prevstate, nextstate):
        self.buttonDict['Prev'].configure(state = prevstate)
        self.buttonDict['Next'].configure(state = nextstate)

    def clear(self):
        self.historyText.delete('1.0', 'end')

    def addnewlines(self, text):
        if len(text) == 1:
            text = text + '\n'
        if text[-1] != '\n':
            text = text + '\n'
        if text[-2] != '\n':
            text = text + '\n'
        return text

    def search(self):
        sql = self.historyText.get()
        self.results.insert('end', self.addnewlines(sql))
        self.results.see('end')
        self.results.update_idletasks()
        self.historyText.addhistory()
        deleteSemiColon = '[\n;]+$'
        results = 'foo'
        if len(results) > 0:
            self.results.insert('end', self.addnewlines(results))
        self.results.see('end')


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
