complete = 1
reviewdate = "22 May 1998"

name = """
    base class for megawidgets within a toplevel
"""

description = """
    This class creates a megawidget contained within a toplevel
    window.  It may be used directly to create a toplevel megawidget
    or it may be used as a base class for more specialised toplevel
    megawidgets, such as ~Dialog~.  It creates a Tkinter.Toplevel
    component, named *hull*, to act as the container of the megawidget. 
    The window class name for the *hull* widget is set to the
    most-specific class name for the megawidget.  Derived classes
    specialise this widget by creating other widget components as
    children of the *hull* widget.
    
    The megawidget may be used as either a normal toplevel window or
    as a modal dialog.  Use /show()/ and /withdraw()/ for normal use
    and /activate()/ and /deactivate()/ for modal dialog use.  If the
    window is deleted by the window manager while being shown
    normally, the default behaviour is to destroy the window.  If the
    window is deleted by the window manager while the window is active
    (ie:  when used as a modal dialog), the window is deactivated. 
    Use the /userdeletefunc()/ and /usermodaldeletefunc()/ methods to
    override these behaviours.  Do not call /protocol()/ to set the
    *WM_DELETE_WINDOW* window manager protocol directly if you want to
    use this window as a modal dialog.

    The currently active windows form a stack with the most recently
    activated window at the top of the stack.  All mouse and
    keyboard events are sent to this top window.  When it
    deactivates, the next window in the stack will start to receive
    events.

"""

text = {}
text['options'] = {}

text['options']['activatecommand'] = """
    If this is callable, it will be called whenever the megawidget is
    activated by a call to /activate()/.

"""

text['options']['deactivatecommand'] = """
    If this is callable, it will be called whenever the megawidget is
    deactivated by a call to /deactivate()/.

"""

text['options']['master'] = """
    This is used by the /activate()/ method to control whether the
    window is made 'transient' during modal dialogs.  See the
    /activate()/ method.

"""

text['options']['title'] = """
    This is the title that the window manager displays in the title
    bar of the window.

"""

text['components'] = {}

text['components']['hull'] = """
    This acts as the body for the entire megawidget.  Other components
    are created as children of the hull to further specialise the
    widget.

"""

text['methods'] = {}

text['methods']['activate'] = """
    Display the window as a modal dialog.  This means that all mouse
    and keyboard events go to this window and no other windows can
    receive any events.  If you do not want to restrict mouse and
    keyboard events to this window, use the /show()/ method instead.

    If the BLT extension to Tk is present, a busy cursor will be
    displayed on other toplevel windows, using /Pmw.showbusycursor()/.
    
    The /activate()/ method does not return until the /deactivate()/
    method is called, when the window is withdrawn, the grab released
    and the result returned.
    
    If 'globalMode' is false, the window will grab control of the
    pointer and keyboard, preventing any events from being delivered
    to any other toplevel windows within the application.  If
    'globalMode' is true, the grab will prevent events from being
    delivered to any other toplevel windows regardless of application. 
    Global grabs should be used sparingly, if at all.

    If 'globalMode' is *'nograb'*, then no grab is performed.  If BLT
    is present, this will allow mouse and keyboard events to be
    received by other windows whose *exclude* busycursor attribute has
    been set to true by a call to /Pmw.setbusycursorattributes()/. 
    Note that if *'nograb'* is used and BLT is not present, then 'all'
    other windows will receive mouse and keyboard events.  This is
    because, in plain Tk, there is no way to specify that two windows
    (only) receive events.  If your application may be used without
    BLT, then do not use *'nograb'*.

    When the window is displayed, it is positioned on the screen
    according to 'geometry' which may be one of:
    
    *centerscreenfirst* -- 
	The window will be centered the first time it is activated. 
	On subsequent activations it will be positioned in the same
	position as the last time it was displayed, even if it has
	been moved by the user.
    
    *centerscreenalways* --
	The window will be be centered on the screen (halfway across
	and one third down).
    
    *first* + 'spec' --
	It is assumed that the rest of the argument (after *'first'*)
	is a standard geometry specification.  The window will be
	positioned using this specification the first time it is
	activated.  On subsequent activations it will be positioned in
	the same position as the last time it was displayed, even if
	it has been moved by the user.  For example,
	/geometry = first+100+100/ will initially display the window
	at position (100,100).  Other calls to /activate()/ will not
	change the previous position of the window.

    'spec' --
	This is a standard geometry specification.  The window will be
	be positioned using this specification.

    If the *BLT* Tcl extension library is present, a *clock* cursor
    will be displayed until the window is deactivated.

    If the *activatecommand* option is callable, it is called just
    before the window begins to wait for the result.

    If the *master* option is not *None*, the window will become a
    transient window of *master*, which should be a toplevel window. 
    If *master* has the special value of *'parent'*, the master is the
    toplevel window of the window's parent.
    
"""

text['methods']['active'] = """
    Return true if the megawidget is currently active (that is,
    /activate()/ is currently waiting for a result to be passed to it
    by a call to /deactivate()/).
    
"""

text['methods']['deactivate'] = """
    This should be called while a call to /activate()/ is waiting.  It
    will withdraw the window, release the grab and cause the
    /activate()/ call to return with the value of 'result'.

    If the *deactivatecommand* option is callable, it is called just
    before the /deactivate()/ method returns.

"""

text['methods']['destroy'] = """
    Destroy the *hull* component widget, including all of its
    children.  If the megawidget is currently active, deactivate it.
    
"""

text['methods']['show'] = """
    Make the window visible.  This raises or deiconifies the toplevel
    window.  If the window has previously been shown it will remain in
    the same position.  This means that calling /withdraw()/ then
    /show()/ will not move the window, whereas calling /withdraw()/
    then /deiconify()/ may change the window's position.  (This may
    depend on the behaviour of the window manager.)
    
"""

text['methods']['userdeletefunc'] = """
    If 'func' is *None*, return the function that will be called
    when the window is deleted by the window manager while being
    displayed normally.  If 'func' is not *None*, set this function to
    'func'.  By default, the function is /self.destroy/.
    
"""

text['methods']['usermodaldeletefunc'] = """
    If 'func' is *None*, return the function that will be called
    when the window is deleted by the window manager while it is
    active (ie:  when being used as a modal dialog).  If 'func' is not
    *None*, set this function to 'func'.  By default, the function is
    /self.deactivate/.
    
"""
