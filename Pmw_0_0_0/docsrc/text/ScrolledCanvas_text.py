complete = 1
reviewdate = "20 September 1998"

name = """
    canvas with optional scrollbars
"""

description = """
    This megawidget consists of a standard canvas widget with optional
    scrollbars which can be used to scroll the canvas.  The scrollbars
    can be 'dynamic', which means that a scrollbar will only be
    displayed if it is necessary, that is, if the scrollregion of the
    canvas is larger than the canvas.

"""

text = {}
text['options'] = {}

text['options']['borderframe'] = """
    If true, the *borderframe* component will be created.

"""

text['options']['canvasmargin'] = """
    The margin around the items in the canvas.  Used by the
    *resizescrollregion()* method.

"""

text['options']['hscrollmode'] = """
    The horizontal scroll mode.  If *'none'*, the horizontal scrollbar
    will never be displayed.  If *'static'*, the scrollbar will always
    be displayed.  If *'dynamic'*, the scrollbar will be displayed
    only if necessary.

"""

text['options']['scrollmargin'] = """
    The distance between the scrollbars and the enclosing canvas
    widget.

"""

text['options']['usehullsize'] = """
    If true, the size of the megawidget is determined solely by the
    width and height options of the *hull* component.

    Otherwise, the size of the megawidget is determined by the width
    and height of the *canvas* component, along with the size and/or
    existence of the other components, such as the label, the
    scrollbars and the scrollmargin option.  All these affect the
    overall size of the megawidget.

"""

text['options']['vscrollmode'] = """
    The vertical scroll mode.  If *'none'*, the vertical scrollbar
    will never be displayed.  If *'static'*, the scrollbar will always
    be displayed.  If *'dynamic'*, the scrollbar will be displayed
    only if necessary.

"""

text['components'] = {}

text['components']['borderframe'] = """
    A frame widget which snuggly fits around the canvas, to give the
    appearance of a canvas border.  It is created with a border so
    that the canvas, which is created without a border, looks like it
    has a border.

"""

text['components']['canvas'] = """
    The canvas widget which is scrolled by the scrollbars.  If the
    *borderframe* option is true, this is created with a borderwidth
    of *0* to overcome a known problem with canvas widgets:  if a
    widget inside a canvas extends across one of the edges of the
    canvas, then the widget obscures the border of the canvas. 
    Therefore, if the canvas has no border, then this overlapping does
    not occur.

"""

text['components']['horizscrollbar'] = """
    The horizontal scrollbar.

"""

text['components']['vertscrollbar'] = """
    The vertical scrollbar.

"""

text['methods'] = {}

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *canvas* component's
    /bbox()/ method.  Without this explicit forwarding, the /bbox()/
    method (aliased to /grid_bbox()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""

text['methods']['interior'] = """
    Return the canvas widget within which the programmer should create
    graphical items and child widgets.  This is the same as
    /component(\\'canvas\\')/.

"""

text['methods']['resizescrollregion'] = """
    Resize the scrollregion of the *canvas* component to be the
    bounding box covering all the items in the canvas plus a margin on
    all sides, as specified by the *canvasmargin* option.

"""
