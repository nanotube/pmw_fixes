complete = 1
reviewdate = "18 May 2002"

name = """
    selection dialog displaying an entry field
"""

description = """
    The prompt dialog is a dialog window which displays an entry field
    which can be used to prompt the user for a value.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the entry field.

"""

text['options']['bordery'] = """
    The padding above and below the entry field.

"""

text['components'] = {}

text['components']['entryfield'] = """
    The entry field for the user to enter a value.

"""

text['methods'] = {}

text['methods']['insertentry'] = """
    Insert text into the entry field's entry widget.  An alias for
    /component(\\'entry\\').insert()/.

"""

text['methods']['deleteentry'] = """
    Delete text from the entry field's entry widget.  An alias for
    /component(\\'entry\\').delete()/.

"""

text['methods']['indexentry'] = """
    An alias for /component(\\'entry\\').index()/.

"""
