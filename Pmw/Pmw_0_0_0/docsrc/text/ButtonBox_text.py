complete = 1
reviewdate = "24 May 1998"

name = """
    manager megawidget for buttons
"""

description = """
    A button box is a container megawidget which manages a number of
    buttons.  One of these buttons may be specified as the default and
    it will be displayed with the platform specific appearance for a
    default button.  The buttons may be laid out either horizontally
    or vertically.

"""

sections = (
    ('Dynamic components', 1, 'Components', 
	"""
	Button components are created dynamically by the /add()/ and
	/insert()/ methods.  By default, the buttons are of type
	Tkinter.Button and are created with a component group of
	*Button*.

	"""
    ),
)

text = {}

text['options'] = {}

text['options']['orient'] = """
    Specifies the orientation of the button box.  This may be
    *'horizontal'* or *'vertical'*.

"""

text['options']['padx'] = """
    Specifies a padding distance to leave between each button in the x
    direction and also between the buttons and the outer edge of the 
    button box.

"""

text['options']['pady'] = """
    Specifies a padding distance to leave between each button in the y
    direction and also between the buttons and the outer edge of the
    button box.

"""

text['components'] = {}

text['components']['frame'] = """
    If the *label* component has been created (that is, the *labelpos*
    option is not *None*), the *frame* component is created to act as
    the container of the buttons created by the /add()/ and
    /insert()/ methods.  If there is no *label* component, then no
    *frame* component is created and the *hull* component acts as the
    container.

"""

text['methods'] = {}

text['methods']['add'] = """
    Add a button to the end of the button box as a component named
    'componentName'.  Any keyword arguments present will be passed to the
    constructor when creating the button.  If the *text* keyword
    argument is not given, the *text* option of the button defaults to
    'componentName'.  The method returns the component widget.
    
"""

text['methods']['alignbuttons'] = """
    Set the widths of all the buttons to be the same as the width of
    the widest button.  If 'when' is *'later'*, this will occur when the
    interpreter next becomes idle, otherwise the resizing will occur
    immediately.
    
"""

text['methods']['button'] = """
    Return the button specified by 'buttonIndex', which may have any
    of the forms accepted by the /index()/ method.

"""

text['methods']['delete'] = """
    Delete the button given by 'index' from the button box.  'index'
    may have any of the forms accepted by the /index()/ method.
    
"""

text['methods']['index'] = """
    Return the numerical index of the button corresponding to 'index'. 
    This may be specified in any of the following forms:

    'name' --
	 Specifies the button named 'name'.
    
    'number' --
	 Specifies the button numerically, where *0* corresponds to
	 the left (or top) button.

    *Pmw.END* --
	 Specifies the right (or bottom) button.

    *Pmw.DEFAULT* --
	 Specifies the current default button.

    If 'forInsert' is true, *Pmw.END* returns the number of buttons rather
    than the index of the last button.

"""

text['methods']['insert'] = """
    Add a button to the button box as a component named
    'componentName'.  The button is added just before the button
    specified by 'beforeComponent', which may have any of the forms
    accepted by the /index()/ method.  Any keyword arguments present
    will be passed to the constructor when creating the button.  If
    the *text* keyword argument is not given, the *text* option of the
    button defaults to 'componentName'.  To add a button to the end of
    the button box, use /add()/.  The method returns the component
    widget.

"""

text['methods']['invoke'] = """
    Invoke the callback command associated with the button specified
    by 'index' and return the value returned by the callback.
    Unless 'noFlash' is true, flash the button to
    indicate to the user that something happened.
    'index' may have any of the forms accepted by the /index()/ method.
    
"""

text['methods']['numbuttons'] = """
    Return the number of buttons in the button box.
    
"""

text['methods']['setdefault'] = """
    Set the default button to the button given by 'index'.  This
    causes the specified button to be displayed with the platform
    specific appearance for a default button.  If 'index' is *None*,
    there will be no default button.  'index' may have any of the
    forms accepted by the /index()/ method.
    
"""
