complete = 1

name = """
    toplevel window with button box
"""

description = """
    This class creates a toplevel window composed of a button box and
    a child site area.  The child site area can be used to specialise
    the megawidget by creating other widgets within it.  This can be
    done by using this class directly or by deriving from it.

"""

no_auto_default = ('buttons',)

text = {}
text['options'] = {}

text['options']['buttonboxpos'] = """
    Specifies on which side of the dialog window to place the button
    box.  Must be one of *'n'*, *'s'*, *'e'* or *'w'*.

"""

text['options']['buttons'] = """
    This must be a tuple or a list and specifies the names on the
    buttons in the button box.  The default is *(\\'OK\\',)*.

"""

text['options']['command'] = """
    Specifies a function to call whenever a button in the button box
    is invoked or the window is deleted by the window manager.  The
    function is called with a single argument, which is the name of
    the button which was invoked, or *None* if the window was deleted
    by the window manager.

    If the value of *command* is not callable, the default behaviour
    is to deactivate the window if it is active, or withdraw the
    window if it is not active.  If it is deactivated, /deactivate()/
    is called with the button name or *None* as described above.

"""

text['options']['defaultbutton'] = """
    Specifies the default button in the button box.  If the *<Return>*
    key is hit when the dialog has focus, the default button will be
    invoked.  If *defaultbutton* is *None*, there will be no default
    button and hitting the *<Return>* key will have no effect.

"""

text['options']['separatorwidth'] = """
    If this is greater than *0*, a separator line with the specified
    width will be created between the button box and the child site,
    as a component named *separator*.  Since the default border of the
    button box and child site is *raised*, this option does not
    usually need to be set for there to be a visual separation between
    the button box and child site.

"""

text['components'] = {}

text['components']['buttonbox'] = """
    This is the button box containing the buttons for the dialog.  By
    default it is created with the options
    /(hull_borderwidth = 1, hull_relief = \\'raised\\')/.

"""

text['components']['dialogchildsite'] = """
    This is the child site for the dialog, which may be used to
    specialise the megawidget by creating other widgets within it.  By
    default it is created with the options
    /(borderwidth = 1, relief = \\'raised\\')/.
    
"""

text['components']['separator'] = """
    If the *separatorwidth* initialisation option is non-zero, the
    *separator* component is the line dividing the area between the
    button box and the child site.

"""

text['methods'] = {}

text['methods']['interior'] = """
    Return the child site for the dialog.  This is the same as
    /component(\\'dialogchildsite\\')/.

"""

text['methods']['invoke'] = """
    Invoke the command specified by the *command* option as if the
    button specified by 'index' had been pressed and return the
    result.  'index' may have any of the forms accepted by the
    ~ButtonBox~ /index()/ method.

"""
