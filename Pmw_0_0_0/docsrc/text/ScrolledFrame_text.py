complete = 1
reviewdate = "18 February 2001"

name = """
    frame with optional scrollbars
"""

description = """
    This megawidget consists of a scrollable interior frame within a
    clipping frame.  The programmer can create other widgets within
    the interior frame.  If the frame becomes larger than the
    surrounding clipping frame, the user can position the frame using
    the horizontal and vertical scrollbars.

    The scrollbars can be 'dynamic', which means that a scrollbar will
    only be displayed if it is necessary.  That is, if the frame is
    smaller than the surrounding clipping frame, the scrollbar will be
    hidden.

"""

text = {}
text['options'] = {}

text['options']['borderframe'] = """
    If true, the *borderframe* component will be created.

"""

text['options']['horizflex'] = """
    Specifies how the width of the scrollable interior frame should be
    resized relative to the clipping frame.
    
    If *'fixed'*, the interior frame is set to the 'natural' width, as
    requested by the child widgets of the frame.  If *'expand'* and
    the requested width of the interior frame is less than the width
    of the clipping frame, the interior frame expands to fill the
    clipping frame.  If *'shrink'* and the requested width of the
    interior frame is more than the width of the clipping frame, the
    interior frame shrinks to the width of the clipping frame.  If
    *'elastic'*, the width of the interior frame is always set to the
    width of the clipping frame.

"""

text['options']['vertflex'] = """
    Specifies how the height of the scrollable interior frame should
    be resized relative to the clipping frame.
    
    If *'fixed'*, the interior frame is set to the 'natural' height,
    as requested by the child widgets of the frame.  If *'expand'* and
    the requested height of the interior frame is less than the height
    of the clipping frame, the interior frame expands to fill the
    clipping frame.  If *'shrink'* and the requested height of the
    interior frame is more than the height of the clipping frame, the
    interior frame shrinks to the height of the clipping frame.  If
    *'elastic'*, the height of the interior frame is always set to the
    height of the clipping frame.

"""

text['options']['hscrollmode'] = """
    The horizontal scroll mode.  If *'none'*, the horizontal scrollbar
    will never be displayed.  If *'static'*, the scrollbar will always
    be displayed.  If *'dynamic'*, the scrollbar will be displayed
    only if necessary.

"""

text['options']['vscrollmode'] = """
    The vertical scroll mode.  If *'none'*, the vertical scrollbar
    will never be displayed.  If *'static'*, the scrollbar will always
    be displayed.  If *'dynamic'*, the scrollbar will be displayed
    only if necessary.

"""

text['options']['horizfraction'] = """
    The fraction of the width of the clipper frame to scroll the
    interior frame when the user clicks on the horizontal scrollbar
    arrows.

"""

text['options']['vertfraction'] = """
    The fraction of the height of the clipper frame to scroll the
    interior frame when the user clicks on the vertical scrollbar
    arrows.

"""

text['options']['scrollmargin'] = """
    The distance between the scrollbars and the clipping frame.

"""

text['options']['usehullsize'] = """
    If true, the size of the megawidget is determined solely by the
    width and height options of the *hull* component.

    Otherwise, the size of the megawidget is determined by the width
    and height of the *clipper* component, along with the size and/or
    existence of the other components, such as the label, the
    scrollbars and the scrollmargin option.  All these affect the
    overall size of the megawidget.

"""

text['components'] = {}

text['components']['borderframe'] = """
    A frame widget which snuggly fits around the clipper, to give the
    appearance of a border.  It is created with a border so that the
    clipper, which is created without a border, looks like it has a
    border.

"""

text['components']['clipper'] = """
    The frame which is used to provide a clipped view of the *frame*
    component.  If the *borderframe* option is true, this is created
    with a borderwidth of *0* to overcome a known problem with using
    /place/ to position widgets:  if a widget (in this case the
    *frame* component) is /placed/ inside a frame (in this case the
    *clipper* component) and it extends across one of the edges of the
    frame, then the widget obscures the border of the frame. 
    Therefore, if the clipper has no border, then this overlapping
    does not occur.

"""

text['components']['frame'] = """
    The frame within the clipper to contain the widgets to be scrolled.

"""

text['components']['horizscrollbar'] = """
    The horizontal scrollbar.

"""

text['components']['vertscrollbar'] = """
    The vertical scrollbar.

"""

text['methods'] = {}

text['methods']['interior'] = """
    Return the frame within which the programmer may create widgets to
    be scrolled.  This is the same as /component(\\'frame\\')/.

"""

text['methods']['reposition'] = """
    Update the position of the *frame* component in the *clipper* and
    update the scrollbar.
    
    Usually, this method does not need to be called explicitly, since
    the position of the *frame* component and the scrollbars are
    automatically updated whenever the size of the *frame* or
    *clipper* components change or the user clicks in the scrollbars. 
    However, if *horizflex* or *vertflex* is *'expand'*, the
    megawidget cannot detect when the requested size of the *frame*
    increases to greater than the size of the *clipper*.  Therefore,
    this method should be called when a new widget is added to the
    *frame* (or a widget is increased in size) 'after' the initial
    megawidget construction.

"""

text['methods']['xview'] = """
    Query or change the horizontal position of the scrollable interior
    frame.  If 'mode' is *None*, return a tuple of two numbers, each
    between 0.0 and 1.0.  The first is the position of the left edge
    of the visible region of the contents of the scrolled frame,
    expressed as a fraction of the total width of the contents.  The
    second is the position of the right edge of the visible region.

    If 'mode' == *'moveto'*, adjust the view of the interior so that
    the fraction 'value' of the total width of the contents is
    off-screen to the left.  The 'value' must be between '0.0' and
    '1.0'.

    If 'mode' == *'scroll'*, adjust the view of the interior left or
    right by a fixed amount.  If 'what' is *'units'*, move the view in
    units of *horizfraction*.  If 'what' is 'pages', move the view in
    units of the width of the scrolled frame.  If 'value' is positive,
    move to the right, otherwise move to the left.
    
"""

text['methods']['yview'] = """
    Query or change the vertical position of the scrollable interior
    frame.  If 'mode' is *None*, return a tuple of two numbers, each
    between 0.0 and 1.0.  The first is the position of the top edge
    of the visible region of the contents of the scrolled frame,
    expressed as a fraction of the total height of the contents.  The
    second is the position of the bottom edge of the visible region.

    If 'mode' == *'moveto'*, adjust the view of the interior so that
    the fraction 'value' of the total height of the contents is
    off-screen to the top.  The 'value' must be between '0.0' and
    '1.0'.

    If 'mode' == *'scroll'*, adjust the view of the interior up or
    down by a fixed amount.  If 'what' is *'units'*, move the view in
    units of *vertfraction*.  If 'what' is 'pages', move the view in
    units of the height of the scrolled frame.  If 'value' is
    positive, move to down, otherwise move up.

"""
