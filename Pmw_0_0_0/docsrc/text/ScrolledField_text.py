complete = 1
reviewdate = "23 August 1998"

name = """
    single line scrollable output field
"""

description = """
    A scrolled field displays a single line of text.  If the text is
    too wide to display in the megawidget it can be scrolled to the
    left and right by the user by dragging with the middle mouse
    button.  The text is also selectable by clicking or dragging with
    the left mouse button.

    It can be used instead of a Tkinter.Label widget when displaying
    text of unknown width such as application status messages.

"""

text = {}
text['options'] = {}

text['options']['text'] = """
    Specifies the text to display in the scrolled field.

"""

text['components'] = {}

text['components']['entry'] = """
    This is used to display the text and allows the user to scroll and
    select the text.  The *state* of this component is set to
    *'readonly'* (or *'disabled'* in earlier versions of Tcl/Tk which do
    not support  *'readonly'*), so that the user is unable to modify the text.

"""

text['methods'] = {}
