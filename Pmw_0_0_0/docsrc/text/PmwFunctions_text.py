aboutcontact = """
    The value passed to this function is used to construct the text
    displayed by ~AboutDialog~ megawidgets created subsequently.

"""

aboutcopyright = """
    The value passed to this function is used to construct the text
    displayed by ~AboutDialog~ megawidgets created subsequently.

"""

aboutversion = """
    The value passed to this function is used to construct the text
    displayed by ~AboutDialog~ megawidgets created subsequently.

"""

aligngrouptags = """
    This function takes a sequence of ~Group~s and adjusts the
    vertical position of the tags in each group so that they all have
    the height of the tallest tag.  This can be used when groups are
    positioned side-by-side but the natural height of the tags are
    different because, for example, different fonts with different
    sizes are used.

"""

drawarrow = """
    Draw a triangle in the Tkinter.Canvas 'canvas' in the given
    'color'.  The value of 'direction' may be *'up'*, *'down'*,
    *'left'* or *'right'* and specifies which direction the arrow
    should point.  The values of 'baseOffset' and 'edgeOffset' specify
    how far from the edges of the canvas the points of the triangles
    are as a fraction of the size of the canvas.

"""

pushgrab = """
    The grab functions (/pushgrab()/, /popgrab()/, /releasegrabs()/
    and /grabstacktopwindow()/) are an interface to the Tk *grab*
    command which implements simple pointer and keyboard grabs.  When
    a grab is set for a particular window, Tk restricts all pointer
    events to the grab window and its descendants in Tk's window
    hierarchy.  The functions are used by the /activate()/ and
    /deactivate()/ methods to implement modal dialogs.

    Pmw maintains a stack of grabbed windows, where the window on the
    top of the stack is the window currently with the grab.  The grab
    stack allows nested modal dialogs, where one modal dialog can be
    activated while another modal dialog is activated.  When the
    second dialog is deactivated, the first dialog becomes active
    again.

    Use /pushgrab()/ to add 'grabWindow' to the grab stack.  This
    releases the grab by the window currently on top of the stack (if
    there is one) and gives the grab and focus to the 'grabWindow'. 
    If 'globalMode' is true, perform a global grab, otherwise perform
    a local grab.  The value of 'deactivateFunction' specifies a
    function to call (usually grabWindow.deactivate) if popgrab() is
    called (usually from a deactivate() method) on a window which is
    not at the top of the stack (that is, does not have the grab or
    focus).  For example, if a modal dialog is deleted by the window
    manager or deactivated by a timer.  In this case, all dialogs
    above and including this one are deactivated, starting at the top
    of the stack.

    For more information, see the Tk grab manual page.

"""

popgrab = """
    Remove 'window' from the grab stack.  If there are not more
    windows in the grab stack, release the grab.  Otherwise set the
    grab and the focus to the next window in the grab stack.  See also
    /pushgrab()/.

"""

releasegrabs = """
    Release grab and clear the grab stack.  This should normally not
    be used, use /popgrab()/ instead.  See also /pushgrab()/.

"""

grabstacktopwindow = """
    Return the window at the top of the grab stack (the window
    currently with the grab) or *None* if the grab stack is empty (no
    window has the grab).  See also /pushgrab()/.

"""

jdntoymd = """
    Return the year, month and day of the Julian Day Number 'jdn'.  If
    'julian' is *1*, then the date returned will be in the Julian
    calendar.  If 'julian' is *0*, then the date returned will be in
    the modern calendar.  If 'julian' is *-1*, then which calendar to
    use will be automatically determined by the value of 'jdn' and
    'papal'.  If 'papal' is true, then the date set by Pope Gregory
    XIII's decree (4 October 1582) will be used as the last day to use
    the Julian calendar.  If 'papal' is false, then the last day to
    use the Julian calendar will be according to British-American
    usage (2 September 1752).

"""

ymdtojdn = """
    Return the Julian Day Number corresponding to 'year', 'month' and
    'day'.  See /jdntoymd()/ for description of other arguments)

"""

busycallback = """
    Create a wrapper function which displays a busy cursor while
    executing 'command' and return the wrapper.  When the wrapper
    function is called, it first calls /Pmw.showbusycursor()/, then
    the 'command' (passing any arguments to it), then /Pmw.hidebusycursor()/.
    The return value of 'command' is returned from the wrapper.

    If 'updateFunction' is specified, it is called just before the
    call to /Pmw.hidebusycursor()/.  This is intended to be the
    Tkinter /update()/ method, in which case it will clear any events
    that may have occurred while 'command' was executing.  An example
    of this usage is in the /ShowBusy/ demonstration:  run the
    demonstration, click on the entry widget then click on the button
    and type some characters while the busy cursor is displayed.  No
    characters should appear in the entry widget.

    Note that the Tkinter /update()/ method should only be called when
    it is known that it can be safely called.  One case where a
    problem has been found is when a filehandler has been created (on
    a non-blocking Oracle database connection), but the filehandler
    does not read from the connection.  The connection is read (by a
    call to the Oracle fetch function 'ofen') in a loop which also
    contains a call to /_tkinter.dooneevent()/.  If /update()/ is
    called from /dooneevent()/ and there is data to be read on the
    connection, then the filehandler will be called continuously, thus
    hanging the application.

"""

setyearpivot = """
    Set the pivot year and century for the application's date
    processing.  These values are used in the /datestringtojdn()/
    method, which is used by ~Counter~ and ~EntryField~
    and derived classes.  The initial values of 'pivot' and 'century'
    are *50* and *2000* repectively.  Return a tuple containing the
    old values of 'pivot' and 'century'.

"""

datestringtojdn = """
    Return the Julian Day Number corresponding to the date in 'text'.
    A Julian Day Number is defined as the number of days since 1 Jan 4713
    BC.  The date must be specified as three integers separated by the
    'separator' character.  The integers must be in the order specified by
    'format', which must be a combination of *'d'*, *'m'* and *'y'* in
    any order.  These give the order of the day, month and year
    fields.  Examples of valid input are:

	# 'dmy':  31/01/99  31/1/1999  31/1/99
	# 'mdy':  01/31/99  1/31/1999  1/31/99
	# 'ymd':  99/01/31  1999/1/31  99/1/31

    If the application's 
    'pivot' year (default 50) is not *None* and the year specified
    in 'text' has only one or two digits, then the year is
    converted to a four digit year.  If it is less than or equal to
    the pivot year, then it is incremented by the application's
    'century' value (default 2000).  If it is more than the pivot year
    then it is incremented by the 'century' value less 100.

    The function /Pmw.setyearpivot()/ can be used to change the
    default values for the application's
    'pivot' and 'century'.

"""

stringtoreal = """
    Return the real number represented by 'text'.  This is similar to
    /string.atof()/ except that the character representing the decimal
    point in 'text' is given by 'separator'.

"""

showbusycursor = """
    Block events to and display a busy cursor over all windows in this
    application that are in the state *'normal'* or *'iconic'*, except
    those windows whose *exclude* busycursor attribute has been set to
    true by a call to /Pmw.setbusycursorattributes()/.
    
    If a window and its contents have just been created,
    /update_idletasks()/ may have to be called before
    /Pmw.showbusycursor()/ so that the window is mapped to the screen. 
    Windows created or deiconified after calling
    /Pmw.showbusycursor()/ will not be blocked.

    To unblock events and remove the busy cursor, use
    /Pmw.hidebusycursor()/.  Nested calls to /Pmw.showbusycursor()/
    may be made.  In this case, a matching number of calls to
    /Pmw.hidebusycursor()/ must be made before the event block and
    busy cursor are removed.
    
    If the BLT extension to Tk is not present, this function has no
    effect other than to save the value of the current focus window,
    to be later restored by /Pmw.hidebusycursor()/.

"""

displayerror = """
    This is a general purpose method for displaying background errors
    to the user.  The errors would normally be programming errors and
    may be caused by errors in Tk callbacks or functions called by other
    asynchronous events.  The error messages are shown in a text window.
    If further errors occur while the window is displayed, the window
    is raised and these new errors are queued.  The queued errors may
    be viewed by the user or ignored by dismissing the window.

"""

reporterrorstofile = """
    If 'file' is *None*, or if /Pmw.reporterrorstofile()/ has not been
    called, future Tk background errors will be displayed in an error
    window (by calling /Pmw.displayerror()/).  If 'file' is not
    *None*, future Tk background errors will be written to the file. 
    'file' may be any object with a /write()/ method, such as
    /sys.stderr/.

"""

initialise = """
    Initialise Pmw.  This performs several functions:

	- Set up a trap in the Tkinter Toplevel constructor so that a
	  list of Toplevels can be maintained.  A list of all Toplevel
	  windows needs to be kept so that /Pmw.showbusycursor()/ can
	  create busy cursors for them.

	- Set up a trap in the Tkinter Toplevel and Frame destructors
	  so that Pmw is notified when these widgets are destroyed. 
	  This allows Pmw to destroy megawidgets when their hull
	  widget is destroyed and to prune the list of Toplevels.

	- Modify Tkinter's CallWrapper class to improve the display of
	  errors which occur in callbacks.  If an error occurs, the
	  new CallWrapper class calls /Pmw.clearbusycursor()/ to
	  remove the any outstanding busy cursors and calls
	  /Pmw.displayerror()/ to display the error.  This behaviour
	  can be modified by calling /Pmw.reporterrorstofile()/.

	- Using the window given by 'root', set the *WM_DELETE_WINDOW*
	  root window protocol to destroy the root window.  This means
	  that the root window is destroyed if the window manager
	  deletes it.  This is only done if the protocol has not been
	  set before the call to /Pmw.initialise()/.  This protocol is
	  required if there is a modal dialog displayed and the window
	  manager deletes the root window.  Otherwise the application
	  will not exit, even though there are no windows.

	- Set the base font size for the application to 'size'.  This
          is used by /Pmw.logicalfont()/ as the default point size for
          fonts.  If this is not given, the default is *14*, except
          under NT where it is *16*.  These are reasonable default
          sizes for most screens, but for unusually high or low screen
          resolutions, an appropriate size should be supplied.  Note
          that Tk's definition of 'point size', is somewhat
          idiosyncratic.
	
	- Set the Tk option database for 'root' according to
	  'fontScheme'.  This changes the default fonts set by Tk. 
	  'fontScheme' may be one of

	    *None*  --
		Do not change the Tk defaults.

	    *'pmw1'*  --
                If running under posix (Unix), set the default font to
                be Helvetica with bold italic menus, italic scales and
                a special balloon font 6 points smaller than the base
                font size and with the *'pixel'* field set to *'12'*.
                For other operating systems (such as NT or Macintosh),
                simply set the default font to be Helvetica.  All
                fonts are as returned by calls to /Pmw.logicalfont()/.

	    *'pmw2'*  --
                This is the same as *'pmw1'* except that under posix
                the balloon font is 2 points smaller than the base
                font size and the *'pixel'* field is not set.

	    *'default'*  --
                This sets the default fonts using the Tk font naming
                convention, rather than that returned by
                /Pmw.logicalfont()/.  The default font is bold
                Helvetica.  The font for entry widgets is Helvetica. 
                The font for text widgets is Courier The size of all
                fonts is the application base font size as described
                above.

	- If 'root' is *None*, use the Tkinter default root window as the
	  root, if it has been created, or create a new Tk root window.
	  The /initialise()/ method returns this 'root'.

	- If 'useTkOptionDb' is true, then, when a megawidget is
	  created, the Tk option database will be queried to get the
	  initial values of the options which have not been set in
	  the call to the constructor.  The resource name used in the
	  query is the same as the option name and the resource class
	  is the option name with the first letter capitalised.  If
	  'useTkOptionDb' is false, then options for newly created
	  megawidgets will be initialised to default values.

	- If 'noBltBusy' is true, then /Pmw.showbusycursor()/ will not
          display a busy cursor, even if the BLT busy command is
          present.

	- If 'disableKeyboardWhileBusy' is false, then do not disable
          keyboard input while displaying the busy cursor.  Normally,
          Pmw ignores keyboard input while displaying the busy cursor
          by setting the focus for each toplevel window to the Blt
          busy window.  However, under NT, this may cause the toplevel
          windows to be raised.  If this is not acceptable, programs
          running on NT can request show/hidebusycursor to not ignore
          keyboard input by setting 'disableKeyboardWhileBusy' to true
          in /Pmw.initialise()/.

    It is not absolutely necessary to call this function to be able to use
    Pmw.  However, some functionality will be lost.  Most importantly,
    Pmw megawidgets will not be notified when their hull widget is
    destroyed.  This may prevent the megawidget from cleaning up
    timers which will try to access the widget, hence causing a
    background error to occur.

"""

alignlabels = """
    Adjust the size of the labels of all the 'widgets' to be equal, so
    that the body of each widget lines up vertically.  This assumes
    that each widget is a megawidget with a *label* component in
    column 0 (ie, the *labelpos* option was set to *'w'*, *'wn'* or
    *'ws'*).  If 'sticky' is set to a combination of *'n'*, *'s'*,
    *'e'* and *'w'*, the label will be positioned within its cell
    accordingly.  For example to make labels right justified, set
    'sticky' to *'e'*, *'ne'* or *'se'*.

"""

forwardmethods = """
    Forward methods from one class to another.

    This function adds methods to the class 'fromClass'.  The names of
    the methods added are the names of the methods of the class
    'toClass' (and its base classes) except those which are already
    defined by 'fromClass' or are found in the 'exclude' list. 
    Special methods with one or more leading or trailing underscores
    are also excluded.

    When one of the added methods is called, the method of the same
    name is called on an instance defined by 'toPart' and the return
    value passed back.  If 'toPart' is a string, then it specifies the
    name of an attribute ('not' a component) of the 'fromClass'
    object.  The class of this attribute should be 'toClass'.  If
    'toPart' is not a string, it must be a function taking a
    'fromClass' object and returning a 'toClass' object.
    
    This function must be called outside of and after the definition
    of 'fromClass'.

    For example:

    #class MyClass:
    #    def __init__(self):
    #        ...
    #        self.__target = TargetClass()
    #        ...
    #
    #    def foo(self):
    #        pass
    #
    #    def findtarget(self):
    #        return self.__target
    #
    #Pmw.forwardmethods(MyClass, TargetClass, '__target',
    #    ['dangerous1', 'dangerous2'])
    #
    ## ...or...
    #
    #Pmw.forwardmethods(MyClass, TargetClass,
    #    MyClass.findtarget, ['dangerous1', 'dangerous2'])

    In both cases, all /TargetClass/ methods will be forwarded from
    /MyClass/ except for /dangerous1/, /dangerous2/, special methods like
    /__str__/, and pre-existing methods like /foo/.

"""

installedversions = """
    If 'alpha' is false, return the list of base versions of Pmw
    that are currently installed and available for use.  If 'alpha' is
    true, return the list of alpha versions.

"""

setalphaversions = """
    Set the list of alpha versions of Pmw to use for this session to
    the arguments.  When searching for Pmw classes and functions,
    these alpha versions will be searched, in the order given, before
    the base version.  This must be called before any other Pmw class
    or function, except functions setting or querying versions.

"""

setversion = """
    Set the version of Pmw to use for this session to 'version'.  If
    /Pmw.setversion()/ is not called, the latest installed version of
    Pmw will be used.  This must be called before any other Pmw class
    or function, except functions setting or querying versions.

"""

version = """
    If 'alpha' is false, return the base version of Pmw being used
    for this session.  If /Pmw.setversion()/ has not been called, this
    will be the latest installed version of Pmw.  If 'alpha' is true,
    return the list of alpha versions of Pmw being used for this
    session, in search order.  If /Pmw.setalphaversions()/ has not
    been called, this will be the empty list.

"""

alphabeticvalidator = """
    Validator function for ~EntryField~ *alphabetic* standard validator.

"""

alphanumericvalidator = """
    Validator function for ~EntryField~ *alphanumeric* standard validator.

"""

datevalidator = """
    Validator function for ~EntryField~ *date* standard validator.

"""

hexadecimalvalidator = """
    Validator function for ~EntryField~ *hexadecimal* standard validator.

"""

integervalidator = """
    Validator function for ~EntryField~ *integer* standard validator.

"""

numericvalidator = """
    Validator function for ~EntryField~ *numeric* standard validator.

"""

realvalidator = """
    Validator function for ~EntryField~ *real* standard validator.

"""

timevalidator = """
    Validator function for ~EntryField~ *time* standard validator.

"""

hidebusycursor = """
    Undo one call to /Pmw.showbusycursor()/.  If there are no
    outstanding calls to /Pmw.showbusycursor()/, remove the event
    block and busy cursor.

    If the focus window has not been changed since the corresponding
    call to /Pmw.showbusycursor()/, or if 'forceFocusRestore' is true,
    then the focus is restored to that saved by /Pmw.showbusycursor()/.
    
"""

clearbusycursor = """
    Unconditionally remove the event block and busy cursor from all
    windows.  This undoes all outstanding calls to
    /Pmw.showbusycursor()/.

"""

setbusycursorattributes = """
    Use the keyword arguments to set attributes controlling the effect
    on 'window' (which must be a *Tkinter.Toplevel*) of future calls
    to /Pmw.showbusycursor()/.  The attributes are:

    *exclude* -- a boolean value which specifies whether the window
    will be affected by calls to /Pmw.showbusycursor()/.  If a window
    is excluded, then the cursor will not be changed to a busy cursor
    and events will still be delivered to the window.  By default,
    windows are affected by calls to /Pmw.showbusycursor()/.

    *cursorName* -- the name of the cursor to use when displaying the
    busy cursor.  If *None*, then the default cursor is used.

"""

tracetk = """
    Print debugging trace of calls to, and callbacks from, the Tk
    interpreter associated with the 'root' window .  If 'root' is
    *None*, use the Tkinter default root.  If 'on' is true, start
    tracing, otherwise stop tracing.  If 'withStackTrace' is true,
    print a python function call stacktrace after the trace for each
    call to Tk.  If 'file' is *None*, print to standard error,
    otherwise print to the file given by 'file'.

    For each call to Tk, the Tk command and its options are printed as
    a python tuple, followed by the return value of the command (if
    not the empty string).  For example:

    #python executed:
    #  button = Tkinter.Button()
    #  button.configure(text = 'Hi')
    #
    #tracetk output:
    #  CALL  TK> 1:  ('button', '.3662448') -> '.3662448'
    #  CALL  TK> 1:  ('.3662448', 'configure', '-text', 'Hi')

    Some calls from python to Tk (such as *update*, *tkwait*,
    *invoke*, etc) result in the execution of callbacks from Tk to
    python.  These python callbacks can then recursively call into Tk. 
    When displayed by *tracetk()*, these recursive calls are indented
    proportionally to the depth of recursion.  The depth is also
    printed as a leading number.  The return value of a call to Tk
    which generated recursive calls is printed on a separate line at
    the end of the recursion.  For example:

    #python executed:
    #  def callback():
    #      button.configure(text = 'Bye')
    #      return 'Got me!'
    #  button = Tkinter.Button()
    #  button.configure(command = callback)
    #  button.invoke()

    #tracetk output:
    #  CALL  TK> 1:  ('button', '.3587144') -> '.3587144'
    #  CALL  TK> 1:  ('.3587144', 'configure', '-command', '3638368callback')
    #  CALL  TK> 1:  ('.3587144', 'invoke')
    #  CALLBACK> 2:    callback()
    #  CALL  TK> 2:    ('.3587144', 'configure', '-text', 'Bye')
    #  CALL RTN> 1:  -> 'Got me!'

    *Pmw.initialise()* must be called before *tracetk()* so that hooks
    are put into the Tkinter CallWrapper class to trace callbacks from
    Tk to python and also to handle recursive calls correctly.

"""

logicalfont = """
    Return the full name of a Tk font, being a hyphen-separated list
    of font properties.  The \'logical\' name of the font is given by
    'name' and may be one of *'Helvetica'*, *'Times'*, *'Fixed'*,
    *'Courier'* or *'Typewriter'*.  Pmw uses this name to define the
    default values of many of the font properties.  The size of the
    font is the base font size for the application specified in the
    call to /Pmw.initialise()/ increased or decreased by the value of
    'sizeIncr'.  The other properties of the font may be specified by
    other named arguments.  These may be *'registry'*, *'foundry'*,
    *'family'*, *'weight'*, *'slant'*, *'width'*, *'style'*,
    *'pixel'*, *'size'*, *'xres'*, *'yres'*, *'spacing'*,
    *'avgwidth'*, *'charset'* and *'encoding'*.

"""

logicalfontnames = """
    Return the list of known logical font names that can be given
    to /Pmw.logicalfont()/.

"""

timestringtoseconds = """
    Return the number of seconds corresponding to the time in 'text'. 
    The time must be specified as three integers separated by the
    'separator' character and must be in the order hours, minutes and
    seconds.  The first number may be negative, indicating a negative
    time.

"""

setgeometryanddeiconify = """
    Deiconify and raise the toplevel 'window' and set its position and
    size according to 'geom'.  This overcomes some problems with the
    window flashing under X and correctly positions the window under
    NT (caused by Tk bugs).

"""
