complete = 1
reviewdate = "30 August 1998"

name = """
    listbox with optional scrollbars
"""

description = """
    This megawidget consists of a standard listbox widget with
    optional scrollbars which can be used to scroll the listbox.  The
    scrollbars can be 'dynamic', which means that a scrollbar will
    only be displayed if it is necessary.  That is, if the listbox
    does not contain enough entries, the vertical scrollbar will be
    automatically hidden and if the entries are not wide enough, the
    horizontal scrollbar will be automatically hidden.

"""

text = {}
text['options'] = {}

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

text['options']['scrollmargin'] = """
    The distance between the scrollbars and the listbox widget.

"""

text['options']['dblclickcommand'] = """
    This specifies a function to call when mouse button 1 is double
    clicked over an entry in the *listbox* component.

"""

text['options']['selectioncommand'] = """
    This specifies a function to call when mouse button 1 is single
    clicked over an entry in the *listbox* component or if the *<Space>*
    or *<Return>* key is hit while the *listbox* has focus.

"""

text['options']['items'] = """
    A tuple containing the initial items to be displayed by the
    *listbox* component.

"""

text['options']['usehullsize'] = """
    If true, the size of the megawidget is determined solely by the
    width and height options of the *hull* component.

    Otherwise, the size of the megawidget is determined by the width
    and height of the *listbox* component, along with the size and/or
    existence of the other components, such as the label, the
    scrollbars and the scrollmargin option.  All these affect the
    overall size of the megawidget.

"""

text['components'] = {}

text['components']['listbox'] = """
    The listbox widget which is scrolled by the scrollbars.

"""

text['components']['horizscrollbar'] = """
    The horizontal scrollbar.

"""

text['components']['vertscrollbar'] = """
    The vertical scrollbar.

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

text['methods']['get'] = """
    This is the same as the /get()/ method of the *listbox* component,
    except that if 'first' is *None* all list
    elements are returned.

"""

text['methods']['getcurselection'] = """
    Return the currently selected items of the listbox.  This returns
    the text of the selected items, rather than their indexes as
    returned by /curselection()/.

"""

text['methods']['setlist'] = """
    Replace all the items of the *listbox* component with those
    specified by the 'items' sequence.

"""
