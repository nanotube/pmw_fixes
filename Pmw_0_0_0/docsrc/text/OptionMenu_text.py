complete = 1
reviewdate = "23 October 1998"

name = """
    single item selection widget
"""

description = """
    This class creates an option menu which consists of a menu button
    and an associated menu which pops up when the button is pressed. 
    The text displayed in the menu button is updated whenever an item
    is selected in the menu.  The currently selected value can be
    retrieved from the megawidget.

"""

text = {}
text['options'] = {}

text['options']['command'] = """
    Specifies a function to call whenever a menu item is selected or
    the /invoke()/ method is called.  The function is called with the
    currently selected value as its single argument.

"""

text['options']['initialitem'] = """
    Specifies the initial selected value.  This option is treated in
    the same way as the 'index' argument of the /setitems()/ method.

"""

text['options']['items'] = """
    A sequence containing the initial items to be displayed in the
    *menu* component.

"""

text['components'] = {}

text['components']['menubutton'] = """
    The menu button displaying the currently selected value.

"""

text['components']['menu'] = """
    The popup menu displayed when the *menubutton* is pressed.

"""

text['methods'] = {}

text['methods']['setitems'] = """
    Replace all the items in the *menu* component with those specified
    by the 'items' sequence.  If 'index' is not *None*, set the
    selected value to 'index', which may have any of the forms
    accepted by the /index()/ method.

    If 'index' is *None* and the *textvariable* option of the
    *menubutton* component is the empty string, then if
    the previous selected value is one of the 'items', then do not
    change the selection.  If the previous selected value is no longer
    in 'items', then set the selected value to the first value in
    'items'.  If 'items' is empty, set the selected value to the empty
    string.

    If 'index' is *None* and the *textvariable* option of the
    *menubutton* component is not the empty string, then do not set
    the selected value.  This assumes that the variable is already (or
    will be) set to the desired value.
    
"""

text['methods']['getcurselection'] = """
    Return the currently selected value.
    
"""

text['methods']['index'] = """
    Return the numerical index of the menu item corresponding to
    'index'.  This may be specified in any of the following forms:

    'name' --
	 Specifies the menu item labelled 'name'.

    'number' --
	 Specifies the menu item numerically, where *0* corresponds to
         the first menu item.

    *Pmw.END* --
	 Specifies the last menu item.

    *Pmw.SELECT* --
	 Specifies the currently selected menu item.

"""

text['methods']['invoke'] = """
    Calling this method is the same as selecting the menu item
    specified by 'index':  the text displayed by the
    *menubutton* component is updated and the function specified by
    the *command* option is called.  'index' may have any of the
    forms accepted by the /index()/ method.  The value returned by
    *command* is returned.
    
"""
