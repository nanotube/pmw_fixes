######################################################################
# This module provides a fontified Python Text class.
# 
# Copyright 1996  Mitchell S. Chapman
# $Id: FontText.py,v 1.1 2001/01/23 12:00:41 gregm Exp $
# -- Mitch Chapman
#---------------------------------------------------------------------
# $Log: FontText.py,v $
# Revision 1.1  2001/01/23 12:00:41  gregm
# Initial revision
#
# Revision 1.2  2000/12/30 15:53:47  gregm
# Release Pmw.0.8.4.
#
# Revision 1.1  1998/01/08 00:52:55  gregm
# First release of Pmw.0.6.
#
# Revision 1.1  1997/11/10 06:56:30  gregm
# See docsrc/text/changes_text.py 10 November 1997.
#
# Revision 1.2  1997/01/27 16:25:28  zack
# Fixed nasty non-keyword pattern bug.
#
# Revision 1.1  1997/01/20 15:51:04  zack
# Initial revision
#
# Revision 1.3  1996/12/04 04:52:12  zack
# Changed the code so that update isn't called in insert
#
# Revision 1.2  1996/12/03 19:02:05  zack
# Initial version from Mitch
#
# Revision 1.1  1996/11/26 05:15:12  zack
# Initial revision
#
# Revision 1.7  1996/10/25 00:14:29  mchapman
# Trying to learn how to insert.
#
# Revision 1.6  1996/10/22 01:26:20  mchapman
# Added a cheesy progress bar.
#
# Revision 1.5  1996/10/21 22:55:12  mchapman
#   Now needs about 8-9 seconds (w. no user feedback) to
#   fontify Tkinter.py
#
#   Still need to override insert(), delete().  refontLine() still needs
#   to back up to start of previous tagged region, extend to end of line
#   or end of tagged region.
#
#   Still too slow!  fontify() takes about 28 seconds to process
#   Tkinter.py.
#
# Revision 1.1  1996/10/18 02:12:31  mchapman
# Initial revision
#
######################################################################

__version__ = "$Revision: 1.1 $"

import Tkinter; Tk=Tkinter
import string, regex

######################################################################
# This class provides the progress box displayed during fontification.
######################################################################
class StatusBox(Tk.Frame):
    ##################################################################
    # Init. a new instance.
    ##################################################################
    def __init__(self, master, total=None):
	self.total = total or 100
	width = self.width = master.winfo_reqwidth() / 4
	height = self.height = master.winfo_reqheight() / 4
	Tk.Frame.__init__(self, master, relief='raised', bd=2,
			  highlightthickness=1, highlightbackground='black',
			  width=width, height=height)
        c = self.canvas = Tk.Canvas(self, highlightthickness=0,
				    width=width, height=height)
	c.pack()

	self.wOutline=3
	self.bar = c.create_rectangle(0, 0, 0, height, fill='#99f', outline='',
				      width=self.wOutline)
	self.text = c.create_text(width / 2, height / 2, anchor='center',
				  text='Highlighting 0%')


	# Re-adjust overall height to fit the text.
	bbox = c.bbox(self.text)
	height = self.height = 3 * (bbox[3] - bbox[1]) / 2

	self.config(width=width, height=height)
	c.config(width=width, height=height)
	c.coords(self.text, width/2, height/2)
	
	self.visible = 0
	
    ##################################################################
    # Make self visible or invisible.
    ##################################################################
    def show(self, makeVisible=1, event=None):
	if makeVisible:
	    self.place(relx=0.5, rely=0.5, x=-self.width/2, y=-self.height/2)
	else:
	    Tk.Place.forget(self)
	self.visible = makeVisible

    ##################################################################
    # Update self, to indicate the work is (done/total) complete.
    ##################################################################
    def update(self, done):
	c = self.canvas
	barWidth = (self.width * done) / self.total
        c.coords(self.bar, -self.wOutline, -self.wOutline,
		 barWidth + self.wOutline, self.height + self.wOutline)
	c.itemconfig(self.text,
		     text="Highlighting %d%%" % ((done * 100) / self.total))
	c.update()


######################################################################
# This class provides fontification for its contents, assuming they
# constitute a Python script.
######################################################################
class Text(Tk.Text):
    # This list of keywords is taken from ref/node13.html of the
    # Python 1.3 HTML documentation.  ("access" is intentionally omitted.)
    keywordsList = [
    "del", "from", "lambda", "return",
    "and", "elif", "global", "not", "try",
    "break", "else", "if", "or", "while",
    "class", "except", "import", "pass",
    "continue", "finally", "in", "print",
    "def", "for", "is", "raise"
    ]

    ##################################################################
    # Initialize a new instance.
    ##################################################################
    def __init__(self, master=None, **kw):
        apply(Tk.Text.__init__, (self, master), kw)
	self.stringTag = "string"
	self.commentTag = "comment"
	self.keywordTag = "keyword"
	self.identDefTag = "identifier"

	# Customize appearances by overriding these tag configurations.
	self.tag_configure(self.stringTag,
			   font="*lucidatypewriter-medium-*-*-*-*-140*",
			   foreground="#0a0")
	self.tag_configure(self.commentTag, foreground='purple')
	self.tag_configure(self.keywordTag,
			   font="*lucidatypewriter-bold-r-*-*-*-140*")
	self.tag_configure(self.identDefTag, foreground="red")
	self.bind("<KeyRelease>", self.refontLine)

	# print "(class %s)" % self.winfo_class(),
	binding = self.bind_class(self.winfo_class(), "<ButtonRelease-2>")

	self.bind("<ButtonRelease-2>", self.insertEH)
	self.bind("<Insert>", self.insertEH)

	# Build up a regular expression which will match anything
	# interesting, including multi-line triple-quoted strings.
	commentPat = "#.*"
	tripleQuotePat = "'''\([^']\|\\\\.\)*'''\|" + '"""\([^"]\|\\\\.\)*"""'
	quotePat = "'\([^']\|\\.\)*'\|" + '"\([^"]\|\\.\)*"'
	# Build up a regular expression which matches all and only
	# Python keywords.  This will let us skip the uninteresting
	# identifier references.
	# nonKeyPat identifies characters which may legally precede
	# a keyword pattern.
	nonKeyPat = "\(^\|[^a-zA-Z0-9_.\"']\)"

	keyPat = nonKeyPat + "\("
	for k in self.keywordsList:
	    keyPat = "%s%s\|" % (keyPat, k)
	keyPat = keyPat[:-2] + "\)" + nonKeyPat
	
	matchPat = "%s\|%s\|%s\|%s" % (keyPat, commentPat,
				       tripleQuotePat, quotePat)
	self.matchRE = regex.compile(matchPat)

	idKeyPat = "[ \t]*[A-Za-z_][A-Za-z_0-9.]*"  # Ident w. leading whitespace.
	self.idRE = regex.compile(idKeyPat)

    ##################################################################
    # Fontify a region of text.
    # This routine is intended for fontifying large regions of
    # text.  It has too much overhead to keep up with typing.
    ##################################################################
    def fontify(self, iStart=None, iEndFonting=None):
	iStart = iStart or "1.0"
	iEndFonting = iEndFonting or "end"
	str = self.get(iStart, iEndFonting)
	
	# Cache a few attributes for quicker reference.
	search = self.matchRE.search
	group = self.matchRE.group
	idSearch = self.idRE.search
	idGroup = self.idRE.group
	call = self.tk.call
	_w = self._w

	bounds = {}
	for tag in [self.commentTag, self.stringTag, self.keywordTag,
		    self.identDefTag]:
	    bounds[tag] = []
	addComment = bounds[self.commentTag].append
	addString = bounds[self.stringTag].append
	addKeyword = bounds[self.keywordTag].append
	addIdent = bounds[self.identDefTag].append

	# Show a little feedback.
	start = self.start = 0
	total = len(str)
	progress = StatusBox(self, total=total)
	timerID = self.after(1500, progress.show)
	
	cnt = 0
	lastStart = 0
	end = 0
	while 1:
	    start = search(str, end)
	    if start < 0: break  # EXIT LOOP

	    if cnt < 100:
		cnt = cnt + 1
	    else:
		cnt = 0
		progress.update(start)

	    match = group(0)
	    end = start + len(match)
	    c = match[0]

	    if c not in ["#", "'", '"']:
		# Must have matched a keyword.
		addKeyword("%s + %d c" % (iStart, start - lastStart))
		# Advance only to the end of the keyword...
		end = start + len(group(1) + group(2))
		iEnd = "%s + %d c" % (iStart, end - lastStart)
		addKeyword(iEnd)

		# If this was a defining keyword, look ahead to the
		# following identifier.
		if match in ["def", "class"]:
		    start = idSearch(str, end)
		    if start == 0:
			match = idGroup(0)
			end = start + len(match)
			addIdent("%s + %d c" % (iStart, start - lastStart))
			iEnd = "%s + %d c" % (iStart, end - lastStart)
			addIdent(iEnd)
	    elif c == "#":
		addComment("%s + %d c" % (iStart, start - lastStart))
		iEnd = "%s + %d c" % (iStart, end - lastStart)
		addComment(iEnd)
	    else:
		addString("%s + %d c" % (iStart, start - lastStart))
		iEnd = "%s + %d c" % (iStart, end - lastStart)
		addString(iEnd)

	    # Tcl/Tk seems to slow way down if you use large distances
	    # in "line.col + <distance> chars".  So "catch up" the index
	    # to the current position.
	    iStart = call(_w, "index", iEnd)
	    lastStart = end
	    
	for tag, extents in bounds.items():
	    if extents:
		apply(call, (_w, "tag", "add", tag) + tuple(extents))
		
	progress.show(0)
	if timerID:
	    self.after_cancel(timerID)

	
    ##################################################################
    # Refontify the current line.
    ##################################################################
    def refontLine(self, event=None):
	if event and not event.char: return

	if self.stringTag in self.tag_names('insert'): return
	
	# This isn't right.  The region to be fontified should
	# be bounded by the tags which begin and end the current
	# line, to give reasonable highlighting updates.
	for tag in [self.commentTag, self.stringTag, self.keywordTag]:
	    self.tag_remove(tag, "insert linestart", "insert lineend")
        self.fontify("insert linestart", "insert lineend")

    ##################################################################
    # Override superclass insert method so we can refont the
    # affected region.
    ##################################################################
    def insert(self, index, chars, *args):
        startIndex = self.index("%s linestart - 1 lines" % index)
	apply(Tk.Text.insert, (self, index, chars, args))
	endIndex = self.index("%s lineend" %
			      self.index('%s + %dc' % (index, len(chars))))
	for tag in [self.commentTag, self.stringTag, self.keywordTag]:
	    self.tag_remove(tag, startIndex, endIndex)

	self.fontify(startIndex, endIndex)


    def insertEH(self, event):
	# EGAD!  I don't know what to do here.
	# I can't easily invoke the default Tk binding *before*
	# doing my thing.
	# In fact, I can't easily invoke it at all.
	# So I've re-implemented the Tk4.0 behavior...
	mouseMoved = string.atoi(apply(self.tk.call,
				       ("expr", "$tkPriv(mouseMoved)")))
	if not mouseMoved:
	    try:
		pastyText = self.selection_get()
		self.insert("@%d,%d" % (event.x, event.y), pastyText)
	    except Tk.TclError: pass
	return "break"
    
######################################################################
# Mainline for testing.
######################################################################
def main():
    import sys, time
    
    t = Text()
    t.pack()

    # Fill up the text.
    args = sys.argv[1:] or ["FontText.py"]
	#"/usr/local/lib/python/tkinter/Tkinter.py"]

    for arg in args:
	inf = open(arg, "r")
	t.insert('end', inf.read())
	inf.close()

    t.mainloop()
    
if __name__ == "__main__":
    main()
