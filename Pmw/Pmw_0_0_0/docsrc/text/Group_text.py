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

text['options']['collapsedsize'] = """
    The distance from the bottom of the tag to the bottom of the ring
    when the groupchildsite is collapsed.

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
    ring.  If the pyclass for this component is *None*, (ie: 
    /tag_pyclass = None/, then no tag component is created.

"""

text['methods'] = {}

text['methods']['interior'] = """
    Return the frame within which the programmer may create widgets. 
    This is the same as /component(\\'groupchildsite\\')/.

"""

text['methods']['collapse'] = """
    Do not display the groupchildsite component.

"""

text['methods']['expand'] = """
    Display the groupchildsite component.

"""

text['methods']['toggle'] = """
    Display the groupchildsite component if it is currently hidden and
    hide it if it is currently displayed.

"""
