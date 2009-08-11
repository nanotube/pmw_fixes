complete = 1
reviewdate = "6 June 2002"

name = """
    a set of buttons, some of which may be selected
"""

description = """
    A radio select is a container megawidget which manages a number of
    buttons.  The buttons may be laid out either horizontally or
    vertically.  In single selection mode, only one button may be
    selected at any one time.  In multiple selection mode, several
    buttons may be selected at the same time and clicking on a
    selected button will deselect it. 

    The buttons displayed can be either standard buttons, radio
    buttons or check buttons.  When selected, standard buttons are
    displayed sunken and radio and check buttons are displayed with
    the appropriate indicator color and relief.

"""

sections = (
    ('Dynamic components', 1, 'Components', 
	"""
	Button components are created dynamically by the /add()/
	method.  The default type of the buttons depends on the value
	of the *buttontype* option.

	Button components are created with a component group of *Button*.

	"""
    ),
)

text = {}
text['options'] = {}

text['options']['command'] = """
    Specifies a function to call when one of the buttons is clicked on
    or when /invoke()/ is called.
    
    In single selection mode, the function is called with a single
    argument, which is the name of the selected button.

    In multiple selection mode, the function is called with the first
    argument being the name of the button and the second argument
    being true if the button is now selected or false if it is now
    deselected.

"""

text['options']['orient'] = """
    Specifies the direction in which the buttons are laid out.  This
    may be *'horizontal'* or *'vertical'*.

"""

text['options']['padx'] = """
    Specifies a padding distance to leave between each button in the x
    direction and also between the buttons and the outer edge of the
    radio select.

"""

text['options']['pady'] = """
    Specifies a padding distance to leave between each button in the y
    direction and also between the buttons and the outer edge of the
    radio select.

"""

text['options']['selectmode'] = """
    Specifies the selection mode:  whether a single button or multiple
    buttons can be selected at one time.  If *'single'*, clicking on
    an unselected button selects it and deselects all other buttons. 
    If *'multiple'*, clicking on an unselected button selects it and
    clicking on a selected button deselects it.  This option is
    ignored if *buttontype* is *'radiobutton'* or *'checkbutton'*.

"""

text['options']['buttontype'] = """
    Specifies the default type of buttons created by the /add()/
    method.  If *'button'*, the default type is Tkinter.Button.  If
    *'radiobutton'*, the default type is Tkinter.Radiobutton.  If
    *'checkbutton'*, the default type is Tkinter.Checkbutton.

    If *'radiobutton'*, single selection mode is automatically set. 
    If *'checkbutton'*, multiple selection mode is automatically set.

"""

text['components'] = {}

text['components']['frame'] = """
    If the *label* component has been created (that is, the *labelpos*
    option is not *None*), the *frame* component is created to act as
    the container of the buttons created by the /add()/ method.  If
    there is no *label* component, then no *frame* component is
    created and the *hull* component acts as the container.

"""

text['methods'] = {}

text['methods']['add'] = """
    Add a button to the end of the radio select as a component
    named 'componentName'.  with a default type as specified by
    *buttontype*.  Any keyword arguments present (except *command*)
    will be passed to the constructor when creating the button.  If
    the *text* keyword argument is not given, the *text* option of the
    button defaults to 'componentName'.  The method returns the
    component widget.

"""

text['methods']['button'] = """
    Return the button specified by 'buttonIndex', which may have any
    of the forms accepted by the /index()/ method.

"""

text['methods']['deleteall'] = """
    Delete all buttons and clear the current selection.

"""

text['methods']['getvalue'] = """
    In single selection mode, return the name of the currently
    selected button, or *None* if no buttons have been selected yet.

    In multiple selection mode, return a list of the names of the
    currently selected buttons.

"""

text['methods']['setvalue'] = """
    Set the current selection for the radio select to 'textOrList',
    but do not invoke *command*.

    In single selection mode, select only the button specified by the
    string 'textOrList'.

    In multiple selection mode, select only the buttons specified by
    the list 'textOrList'.
    
"""

text['methods']['getcurselection'] = """
    Same as /getvalue()/ method.

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

"""

text['methods']['invoke'] = """
    Calling this method is the same as clicking on the button
    specified by 'index':  the buttons are displayed selected or
    deselected according to the selection mode and *command* is
    called.  'index' may have any of the forms accepted by the
    /index()/ method.  The value returned by *command* is returned.

"""

text['methods']['numbuttons'] = """
    Return the number of buttons in the radio select.

"""
