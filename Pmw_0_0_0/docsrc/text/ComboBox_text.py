complete = 1
reviewdate = "1 November 1998"

name = """
    dropdown or simple combination box
"""

description = """
    A combobox contains an entry field and an associated scrolled
    listbox.  When an item in the listbox is selected, it is displayed
    in the entry field.  Optionally, the user may also edit the entry
    field directly.

    For a simple combobox, the scrolled listbox is displayed beneath
    the entry field.  For a dropdown combobox (the default), the
    scrolled listbox is displayed in a window which pops up beneath
    the entry field when the user clicks on an arrow button on the
    right of the entry field.  Either style allows an optional label.

"""

text = {}
text['options'] = {}

text['options']['autoclear'] = """
    If both *autoclear* and *history* are true, clear the entry field
    whenever *<Return>* is pressed, after adding the value to the
    history list.

"""

text['options']['buttonaspect'] = """
    The width of the arrow button as a proportion of the height.  The
    height of the arrow button is set to the height of the entry
    widget.

"""

text['options']['dropdown'] = """
    Specifies whether the combobox should be dropdown or simple.

"""

text['options']['fliparrow'] = """
    If true, the arrow button is draw upside down when the listbox is
    being displayed.  Used only in dropdown megawidgets.

"""

text['options']['history'] = """
    When *<Return>* is pressed in the entry field, the current value
    of the entry field is appended to the listbox if *history* is
    true.

"""

text['options']['listheight'] = """
    The height, in pixels, of the dropdown listbox.

"""

text['options']['selectioncommand'] = """
    The function to call when an item is selected.
    If this function takes a long time to run, and you want the entry
    field to be updated quickly, call /update_idletasks()/ at the
    beginning of the function.  Alternatively, wrap the function using
    /Pmw.busycallback()/.

"""

text['options']['unique'] = """
    If both *unique* and *history* are true, the current value of the
    entry field is not added to the listbox if it is already in the
    list.

"""

text['components'] = {}

text['components']['arrowbutton'] = """
    In a dropdown combobox, the button to popup the listbox.

"""

text['components']['entryfield'] = """
    The entry field where the current selection is displayed.

"""

text['components']['popup'] = """
    In a dropdown combobox, the dropdown window.

"""

text['components']['scrolledlist'] = """
    The scrolled listbox which displays the items to select.

"""

text['methods'] = {}

text['methods']['get'] = """
    This is the same as the /get()/ method of the *scrolledlist*
    component, except that if 'first' is *None* then
    the value of the entry field is returned.

"""

text['methods']['invoke'] = """
    If a dropdown combobox, display the dropdown listbox.  In a simple
    combobox, select the currently selected item in the listbox,
    call the *selectioncommand* and return the result.

"""

text['methods']['selectitem'] = """
    Select the item in the listbox specified by 'index' which may be
    either one of the items in the listbox or the integer index of one
    of the items in the listbox.

    If 'setentry' is true, also set the entry field to the selected
    item.

"""

text['methods']['clear'] = """
    Delete all items from the scrolled listbox and delete all text
    from the entry widget.

"""

text['methods']['size'] = """
    This method is explicitly forwarded to the *scrolledlist*
    component's /size()/ method.  Without this explicit forwarding,
    the /size()/ method (aliased to /grid_size()/) of the *hull* would
    be invoked, which is probably not what the programmer intended.

"""

text['methods']['bbox'] = """
    This method is explicitly forwarded to the *scrolledlist*
    component's /bbox()/ method.  Without this explicit forwarding,
    the /bbox()/ method (aliased to /grid_bbox()/) of the *hull* would
    be invoked, which is probably not what the programmer intended.

"""
