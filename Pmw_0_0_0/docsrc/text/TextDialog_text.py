complete = 1
reviewdate = "18 May 2002"

name = """
    a dialog displaying a scrolled text
"""

description = """
    A text dialog is a dialog window which displays a text message to
    the user along with one or more buttons to press.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the scrolled text.

"""

text['options']['bordery'] = """
    The padding above and below the scrolled text.

"""

text['components'] = {}

text['components']['scrolledtext'] = """
    The scrolled text to contain the text for the dialog.

"""

text['methods'] = {}

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *text* component's
    /bbox()/ method.  Without this explicit forwarding, the /bbox()/
    method (aliased to /grid_bbox()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""
