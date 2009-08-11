complete = 1
reviewdate = "8 November 1998"

name = """
    frame with label
"""

description = """
    This megawidget consists of an interior frame with an associated
    label which can be positioned on any side of the frame.  The
    programmer can create other widgets within the interior frame.

"""

text = {}
text['options'] = {}

text['components'] = {}

text['components']['labelchildsite'] = """
    The frame which can contain other widgets to be labelled.

"""

text['methods'] = {}

text['methods']['interior'] = """
    Return the frame within which the programmer may create widgets. 
    This is the same as /component(\\'labelchildsite\\')/.

"""
