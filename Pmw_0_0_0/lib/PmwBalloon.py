import os
import string
import Tkinter
import Pmw

class Balloon(Pmw.MegaToplevel):
    def __init__(self, parent = None, **kw):

	# Define the megawidget options.
	optiondefs = (
            ('initwait',                 500,            None), # milliseconds
            ('label_background',         'lightyellow',  None),
            ('label_justify',            'left',         None),
            ('master',                   'parent',       None),
            ('relmouse',                 'none',         self._relmouse),
            ('state',                    'both',         self._state),
            ('statuscommand',            None,           None),
            ('xoffset',                  20,             None), # pixels
            ('yoffset',                  1,              None), # pixels
	    ('hull_highlightthickness',  1,              None),
	    ('hull_highlightbackground', 'black',        None),
	)
	self.defineoptions(kw, optiondefs)

	# Initialise the base class (after defining the options).
	Pmw.MegaToplevel.__init__(self, parent)

	self.withdraw()
	self.overrideredirect(1)

	# Create the components.
	interior = self.interior()
	self._label = self.createcomponent('label',
		(), None,
		Tkinter.Label, (interior,))
	self._label.pack()

        # The default hull configuration options give a black border
        # around the balloon, but avoids a black 'flash' when the
        # balloon is deiconified, before the text appears.
        if not kw.has_key('hull_background'):
            self.configure(hull_background = self._label.cget('background'))

	# Initialise instance variables.
	self._timer = None
        # self._currentTrigger = None    ### TODO - see bugs list
	
	# Check keywords and initialise options.
	self.initialiseoptions(Balloon)

    def destroy(self):
	if self._timer is not None:
	    self.after_cancel(self._timer)
	    self._timer = None
	Pmw.MegaToplevel.destroy(self)

    def bind(self, widget, balloonHelp, statusHelp = None):

        # If a previous bind for this widget exists, remove it.
        self.unbind(widget)

	if balloonHelp is None and statusHelp is None:
	    return

	if statusHelp is None:
	    statusHelp = balloonHelp
	enterId = widget.bind('<Enter>', 
		lambda event = None, self = self, w = widget,
			sHelp = statusHelp, bHelp = balloonHelp:
				self._enter(w, sHelp, bHelp, 0))
	# Note: The Motion binding only works for basic widgets,
	# not megawidgets.
	motionId = widget.bind('<Motion>', 
		lambda event = None, self = self, statusHelp = statusHelp:
			self.showstatus(statusHelp))
	leaveId = widget.bind('<Leave>', self._leave)
	buttonId = widget.bind('<ButtonPress>', self._buttonpress)

        # Use the None item in the widget's private Pmw dictionary to
        # store the widget's bind callbacks, for later clean up.
        if not hasattr(widget, '_Pmw_BalloonBindIds'):
            widget._Pmw_BalloonBindIds = {}
        widget._Pmw_BalloonBindIds[None] = \
                (enterId, motionId, leaveId, buttonId)

    def unbind(self, widget):
        if hasattr(widget, '_Pmw_BalloonBindIds'):
            if widget._Pmw_BalloonBindIds.has_key(None):
                (enterId, motionId, leaveId, buttonId) = \
                        widget._Pmw_BalloonBindIds[None]
                # Need to pass in old bindings, so that Tkinter can
                # delete the commands.  Otherwise, memory is leaked.
                widget.unbind('<Enter>', enterId)
                widget.unbind('<Motion>', motionId)
                widget.unbind('<Leave>', leaveId)
                widget.unbind('<ButtonPress>', buttonId)
                del widget._Pmw_BalloonBindIds[None]

    def tagbind(self, widget, tagOrItem, balloonHelp, statusHelp = None):

        # If a previous bind for this widget's tagOrItem exists, remove it.
        self.tagunbind(widget, tagOrItem)

	if balloonHelp is None and statusHelp is None:
	    return

	if statusHelp is None:
	    statusHelp = balloonHelp
	enterId = widget.tag_bind(tagOrItem, '<Enter>', 
		lambda event = None, self = self, w = widget,
			sHelp = statusHelp, bHelp = balloonHelp:
				self._enter(w, sHelp, bHelp, 1))
	motionId = widget.tag_bind(tagOrItem, '<Motion>', 
		lambda event = None, self = self, statusHelp = statusHelp:
			self.showstatus(statusHelp))
	leaveId = widget.tag_bind(tagOrItem, '<Leave>', self._leave)
	buttonId = widget.tag_bind(tagOrItem, '<ButtonPress>', self._buttonpress)

        # Use the tagOrItem item in the widget's private Pmw dictionary to
        # store the tagOrItem's bind callbacks, for later clean up.
        if not hasattr(widget, '_Pmw_BalloonBindIds'):
            widget._Pmw_BalloonBindIds = {}
        widget._Pmw_BalloonBindIds[tagOrItem] = \
                (enterId, motionId, leaveId, buttonId)

    def tagunbind(self, widget, tagOrItem):
        if hasattr(widget, '_Pmw_BalloonBindIds'):
            if widget._Pmw_BalloonBindIds.has_key(tagOrItem):
                (enterId, motionId, leaveId, buttonId) = \
                        widget._Pmw_BalloonBindIds[tagOrItem]
                widget.tag_unbind(tagOrItem, '<Enter>', enterId)
                widget.tag_unbind(tagOrItem, '<Motion>', motionId)
                widget.tag_unbind(tagOrItem, '<Leave>', leaveId)
                widget.tag_unbind(tagOrItem, '<ButtonPress>', buttonId)
                del widget._Pmw_BalloonBindIds[tagOrItem]

    def showstatus(self, statusHelp):
	if self['state'] in ('status', 'both'):
	    cmd = self['statuscommand']
	    if callable(cmd):
		cmd(statusHelp)

    def clearstatus(self):
        self.showstatus(None)

    def _state(self):
	if self['state'] not in ('both', 'balloon', 'status', 'none'):
	    raise ValueError, 'bad state option ' + repr(self['state']) + \
		': should be one of \'both\', \'balloon\', ' + \
		'\'status\' or \'none\''

    def _relmouse(self):
	if self['relmouse'] not in ('both', 'x', 'y', 'none'):
	    raise ValueError, 'bad relmouse option ' + repr(self['relmouse'])+ \
		': should be one of \'both\', \'x\', ' + '\'y\' or \'none\''

    def _enter(self, widget, statusHelp, balloonHelp, isItem):
	if balloonHelp is not None and self['state'] in ('balloon', 'both'):
	    if self._timer is not None:
		self.after_cancel(self._timer)
		self._timer = None

	    self._timer = self.after(self['initwait'], 
		    lambda self = self, widget = widget, help = balloonHelp,
			    isItem = isItem:
			    self._showBalloon(widget, help, isItem))

	self.showstatus(statusHelp)

    def _leave(self, event):
	if self._timer is not None:
	    self.after_cancel(self._timer)
	    self._timer = None
	self.withdraw()
	self.clearstatus()
        # self._currentTrigger = None

    def _buttonpress(self, event):
	if self._timer is not None:
	    self.after_cancel(self._timer)
	    self._timer = None
	self.withdraw()
        # self._currentTrigger = None

    def _showBalloon(self, widget, balloonHelp, isItem):

	self._label.configure(text = balloonHelp)

        # First, display the balloon offscreen to get dimensions.
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry('+%d+0' % (screenWidth + 1))
        self.update_idletasks()

	if isItem:
            # Get the bounding box of the current item.
            bbox = widget.bbox('current')
            if bbox is None:
                # The item that triggered the balloon has disappeared,
                # perhaps by a user's timer event that occured between
                # the <Enter> event and the 'initwait' timer calling
                # this method.
                return

	    # The widget is either a text or canvas.  The meaning of
	    # the values returned by the bbox method is different for
	    # each, so use the existence of the 'canvasx' method to
	    # distinguish between them.
	    if hasattr(widget, 'canvasx'):
		# The widget is a canvas.  Place balloon under canvas
                # item.  The positions returned by bbox are relative
                # to the entire canvas, not just the visible part, so
                # need to convert to window coordinates.
                leftrel = bbox[0] - widget.canvasx(0)
                toprel = bbox[1] - widget.canvasy(0)
                bottomrel = bbox[3] - widget.canvasy(0)
	    else:
		# The widget is a text widget.  Place balloon under
                # the character closest to the mouse.  The positions
                # returned by bbox are relative to the text widget
                # window (ie the visible part of the text only).
		leftrel = bbox[0]
                toprel = bbox[1]
		bottomrel = bbox[1] + bbox[3]
	else:
	    leftrel = 0
            toprel = 0
	    bottomrel = widget.winfo_height()

        xpointer, ypointer = widget.winfo_pointerxy()   # -1 if off screen

        if xpointer >= 0 and self['relmouse'] in ('both', 'x'):
            x = xpointer
        else:
            x = leftrel + widget.winfo_rootx()
        x = x + self['xoffset']

        if ypointer >= 0 and self['relmouse'] in ('both', 'y'):
            y = ypointer
        else:
            y = bottomrel + widget.winfo_rooty()
        y = y + self['yoffset']

        edges = (string.atoi(self.cget('hull_highlightthickness')) +
            string.atoi(self.cget('hull_borderwidth'))) * 2
        if x + self._label.winfo_reqwidth() + edges > screenWidth:
            x = screenWidth - self._label.winfo_reqwidth() - edges

        if y + self._label.winfo_reqheight() + edges > screenHeight:
            if ypointer >= 0 and self['relmouse'] in ('both', 'y'):
                y = ypointer
            else:
                y = toprel + widget.winfo_rooty()
            y = y - self._label.winfo_reqheight() - self['yoffset'] - edges

        Pmw.setgeometryanddeiconify(self, '+%d+%d' % (x, y))

	# if isItem:
        #     item = widget.find_withtag('current')  # Only works for canvas
        #     self._currentTrigger = (widget, item)
        # else:
        #     self._currentTrigger = (widget,)
