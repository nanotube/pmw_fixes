complete = 1
reviewdate = "30 August 1998"

name = """
    text widget with optional scrollbars
"""

description = """
    A scrolled text consists of a standard text widget with optional
    scrollbars which can be used to scroll the text.  The
    scrollbars can be 'dynamic', which means that a scrollbar will
    only be displayed if it is necessary.  That is, if the text widget
    does not contain enough text (either horizontally or vertically),
    the scrollbar will be automatically hidden.  If it is displayed,
    the horizontal scrollbar is under the text widget.  Similarly, if
    it is displayed, the vertical scrollbar is to the right of the
    text widget.

    Row and column headers may also be displayed, which scroll in sync
    with the text widget and may be useful when displaying tabular
    data.  To assist in ensuring that columns line up when using a
    column header, a fixed width font should be used.

"""

text = {}
text['options'] = {}

text['options']['borderframe'] = """
    If true, the *borderframe* component will be created.

"""

text['options']['columnheader'] = """
    If true, the *columnheader* component will be created.

"""

text['options']['rowcolumnheader'] = """
    If true, the *rowcolumnheader* component will be created.

"""

text['options']['rowheader'] = """
    If true, the *rowheader* component will be created.

"""

text['options']['hscrollmode'] = """
    The horizontal scroll mode.  If *'none'*, the horizontal scrollbar
    will never be displayed.  If *'static'*, the scrollbar will always
    be displayed.  If *'dynamic'*, the scrollbar will be displayed
    only if necessary.

"""

text['options']['scrollmargin'] = """
    The distance between the scrollbars and the text widget.

"""

text['options']['usehullsize'] = """
    If true, the size of the megawidget is determined solely by the
    width and height options of the *hull* component.

    Otherwise, the size of the megawidget is determined by the width
    and height of the *text* component, along with the size and/or
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
    A frame widget which snuggly fits around the text widget, to give
    the appearance of a text border.  It is created with a border so
    that the text widget, which is created without a border, looks
    like it has a border.

"""

text['components']['columnheader'] = """
    A text widget with a default height of 1 displayed above the main
    text widget and which scrolls horizontally in sync with the
    horizontal scrolling of the main text widget.

"""

text['components']['rowcolumnheader'] = """
    A text widget displayed to the top left of the main text widget,
    above the row header and to the left of the column header if they
    exist.  The widget is not scrolled  automatically.

"""

text['components']['rowheader'] = """
    A text widget displayed to the left of the main text widget and
    which scrolls vertically in sync with the vertical scrolling of
    the main text widget.

"""

text['components']['horizscrollbar'] = """
    The horizontal scrollbar.

"""

text['components']['text'] = """
    The text widget which is scrolled by the scrollbars.  If the
    *borderframe* option is true, this is created with a borderwidth
    of *0* to overcome a known problem with text widgets:  if a widget
    inside a text widget extends across one of the edges of the text
    widget, then the widget obscures the border of the text widget. 
    Therefore, if the text widget has no border, then this overlapping
    does not occur.

"""

text['components']['vertscrollbar'] = """
    The vertical scrollbar.

"""

text['methods'] = {}

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *text* component's
    /bbox()/ method.  Without this explicit forwarding, the /bbox()/
    method (aliased to /grid_bbox()/) of the *hull* would be invoked,
    which is probably not what the programmer intended.

"""

text['methods']['clear'] = """
    Delete all text from the *text* component.

"""

text['methods']['exportfile'] = """
    Write the contents of the *text* component to the file 'fileName'.

"""

text['methods']['get'] = """
    This is the same as the /get()/ method of the *text* component,
    except that if 'first' is *None* the entire
    contents of the text widget are returned.

"""

text['methods']['getvalue'] = """
    Return the entire contents of the text widget.

"""

text['methods']['setvalue'] = """
    Replace the entire contents of the *text* component with 'text'.
    
"""

text['methods']['importfile'] = """
    Read the contents of the file 'fileName' and insert into the
    *text* component at the position given by 'where'.

"""

text['methods']['settext'] = """
    Same as /setvalue()/ method.

"""

text['methods']['appendtext'] = """
    Add 'text' to the end of the *text* component.  Scroll to the
    bottom of the text, but only if it was already visible before the
    new text was added.

"""
