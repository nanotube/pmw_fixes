complete = 1
reviewdate = "18 May 2002"

name = """
    selection dialog displaying a scrolled list
"""

description = """
    The selection dialog is a dialog window which displays a scrolled
    list which can be used to prompt the user for a value.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the scrolled list.

"""

text['options']['bordery'] = """
    The padding above and below the scrolled list.

"""

text['components'] = {}

text['components']['scrolledlist'] = """
    The scrolled list for the user to enter a value.

"""

text['methods'] = {}

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *listbox* component's
    /bbox()/ method.  Without this explicit forwarding, the /bbox()/
    method (aliased to /grid_bbox()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""

text['methods']['size'] = """
    This method is explicitly forwarded to the *listbox* component's
    /size()/ method.  Without this explicit forwarding, the /size()/
    method (aliased to /grid_size()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""
