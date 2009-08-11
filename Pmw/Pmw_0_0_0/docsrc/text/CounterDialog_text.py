complete = 1
reviewdate = "18 May 2002"

name = """
    selection dialog displaying a counter
"""

description = """
    A counter dialog is a dialog window which displays a counter
    which can be used to prompt the user for a value.

"""

text = {}
text['options'] = {}

text['options']['borderx'] = """
    The padding to the left and right of the counter.

"""

text['options']['bordery'] = """
    The padding above and below the counter.

"""

text['components'] = {}

text['components']['counter'] = """
    The counter for the user to enter a value.

"""

text['methods'] = {}

text['methods']['insertentry'] = """
    Insert text into the counter's entry widget.  An alias for
    /component(\\'entry\\').insert()/.

"""

text['methods']['deleteentry'] = """
    Delete text from the counter's entry widget.  An alias for
    /component(\\'entry\\').delete()/.

"""

text['methods']['indexentry'] = """
    An alias for /component(\\'entry\\').index()/.

"""
