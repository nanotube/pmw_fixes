complete = 1
reviewdate = "15 November 1998"

name = """
    frame with ring border and tag
"""

description = """
    This megawidget consists of an interior frame with an exterior
    ring border and an identifying tag displayed over the top edge of
    the ring.  The programmer can create other widgets within the
    interior frame.

"""

text = {}
text['options'] = {}

text['options']['tagindent'] = """
    The distance from the left edge of the ring to the left side of
    the tag component.

"""

text['components'] = {}

text['components']['ring'] = """
    This component acts as the enclosing ring around the
    *groupchildsite*.  The default *borderwidth* is *2* and the
    default *relief* is *'groove'*.

"""

text['components']['groupchildsite'] = """
    The frame which can contain other widgets to be grouped.

"""

text['components']['tag'] = """
    The identifying tag displayed over the top edge of the enclosing
    ring.  If this is *None*, no tag is displayed.

"""

text['methods'] = {}

text['methods']['interior'] = """
    Return the frame within which the programmer may create widgets. 
    This is the same as /component(\\'groupchildsite\\')/.

"""
