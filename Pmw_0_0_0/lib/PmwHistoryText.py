import Pmw

# The history is stored as a list of entries, represented by 3-tuples. 
# The first item in a history entry is the original text as added by
# addhistory().  The second item is the edited text (if the user has
# gone back in the history, edited it and then moved away from it). 
# The third item specifies whether the entry should currently display
# the original or modified text.

_ORIGINAL = 0
_MODIFIED = 1
_DISPLAY = 2

class HistoryText(Pmw.ScrolledText):

    def __init__(self, parent = None, **kw):

        # Define the megawidget options.
        optiondefs = (
            ('statechangecmd',    None,            None),
        )
        self.defineoptions(kw, optiondefs)

        # Initialise the base class (after defining the options).
        Pmw.ScrolledText.__init__(self, parent)

        # Initialise instance variables.
	self._list = []
	self._currIndex = 0
	self._pastIndex = None
	self._lastIndex = 0
        self._compressTail = 1
        self._compressAny = 1

        # Check keywords and initialise options.
        self.initialiseoptions(HistoryText)

    def addhistory(self):
	text = self.get()
	if text[-1] == '\n':
	    text = text[:-1]

	if len(self._list) == 0:
            # This is the first history entry.  Add it.
	    self._list.append([text, text, _MODIFIED])
            return

        currentEntry =  self._list[self._currIndex]
        if text == currentEntry[_ORIGINAL]:
            # The current history entry has not been modified. Check if
            # we need to add it again.

            if self._compressTail and self._currIndex == self._lastIndex:
                # The compresstail option was specified and the last
                # history entry is currently being displayed, so do
                # not add it again.
                return

            if self._compressAny:
                # The compressany option was specified, so do not add
                # it again.
                return

        # Undo any changes for the current history entry, since they
        # will now be available in the new entry.
        currentEntry[_MODIFIED] = currentEntry[_ORIGINAL]

        if self._currIndex == self._lastIndex:
            # The last history entry is currently being displayed,
            # so disable the special meaning of the 'Next' button.
            self._pastIndex = None
            self.statechangecmd('normal', 'disabled')
        else:
            # A previous history entry is currently being displayed,
            # so allow the 'Next' button to go to the entry after this one.
            self._pastIndex = self._currIndex
            self.statechangecmd('normal', 'normal')

        # Create the new history entry.
        self._list.append([text, text, _MODIFIED])

        # Move the pointer into the history entry list to the end.
        self._lastIndex = self._lastIndex + 1
        self._currIndex = self._lastIndex

    def next(self):
	if self._currIndex == self._lastIndex and self._pastIndex is None:
	    self.bell()
        else:
            self._modifyDisplay('next')

    def prev(self):
        self._pastIndex = None
	if self._currIndex == 0:
	    self.bell()
        else:
            self._modifyDisplay('prev')

    def undo(self):
	if len(self._list) != 0:
            self._modifyDisplay('undo')

    def redo(self):
	if len(self._list) != 0:
            self._modifyDisplay('redo')

    def gethistory(self):
        return self._list

    def _modifyDisplay(self, command):
        # Modify the display to show either the next or previous
        # history entry (next, prev) or the original or modified
        # version of the current history entry (undo, redo).

        # Save the currently displayed text.
        currentText = self.get()
        if currentText[-1] == '\n':
            currentText = currentText[:-1]

        currentEntry =  self._list[self._currIndex]
        if currentEntry[_DISPLAY] == _MODIFIED:
            currentEntry[_MODIFIED] = currentText
        elif currentEntry[_ORIGINAL] != currentText:
            currentEntry[_MODIFIED] = currentText
            if command in ('next', 'prev'):
                currentEntry[_DISPLAY] = _MODIFIED

        if command in ('next', 'prev'):
            prevstate = 'normal'
            nextstate = 'normal'
            if command == 'next':
                if self._pastIndex is not None:
                    self._currIndex = self._pastIndex
                    self._pastIndex = None
                self._currIndex = self._currIndex + 1
                if self._currIndex == self._lastIndex:
                    nextstate = 'disabled'
            elif command == 'prev':
                self._currIndex = self._currIndex - 1
                if self._currIndex == 0:
                    prevstate = 'disabled'
            self.statechangecmd(prevstate, nextstate)
            currentEntry =  self._list[self._currIndex]
        else:
            if command == 'undo':
                currentEntry[_DISPLAY] = _ORIGINAL
            elif command == 'redo':
                currentEntry[_DISPLAY] = _MODIFIED

        # Display the new text.
        self.delete('1.0', 'end')
        self.insert('end', currentEntry[currentEntry[_DISPLAY]])
