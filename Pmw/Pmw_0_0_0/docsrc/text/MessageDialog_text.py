complete = 1
reviewdate = "18 May 2002"

name = """
    a dialog displaying a text message and an icon
"""

description = """
    A message dialog is a dialog window which displays a simple
    message to the user along with one or more buttons to press.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the text message and icon.

"""

text['options']['bordery'] = """
    The padding above and below the text message and icon.

"""

text['options']['iconmargin'] = """
    The padding between the text message and icon.

"""

text['options']['iconpos'] = """
    Specifies on which side of the text message to place the icon. 
    Must be one of *'n'*, *'s'*, *'e'* or *'w'*.

"""

text['components'] = {}

text['components']['icon'] = """
    If the *iconpos* option is not *None*, this component is created
    to contain the icon label for the dialog.  To display a bitmap as
    an icon, set the *icon_bitmap* component option to any of the
    forms acceptable to Tk, such as *'warning'* or *'error'*.

"""

text['components']['message'] = """
    The label to contain the text message for the dialog.  To set
    the text, use the *message_text* component option.

"""

text['methods'] = {}
