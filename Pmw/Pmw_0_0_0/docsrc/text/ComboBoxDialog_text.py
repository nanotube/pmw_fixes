complete = 1
reviewdate = "18 May 2002"

name = """
    selection dialog displaying a list and an entry field
"""

description = """
    A combobox dialog is a dialog window which displays a list and
    an entry field which can be used to prompt the user for a value.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the combobox.

"""

text['options']['bordery'] = """
    The padding above and below the combobox.

"""

text['components'] = {}

text['components']['combobox'] = """
    The combobox for the user to enter a value.  By default it is
    created using the option /dropdown = 0/.

"""

text['methods'] = {}

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *combobox* component's
    /bbox()/ method.  Without this explicit forwarding, the /bbox()/
    method (aliased to /grid_bbox()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""

text['methods']['size'] = """
    This method is explicitly forwarded to the *combobox* component's
    /size()/ method.  Without this explicit forwarding, the /size()/
    method (aliased to /grid_size()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""
