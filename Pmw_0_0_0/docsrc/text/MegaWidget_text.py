complete = 1
reviewdate = "22 May 1998"

name = """
    base class for megawidgets within a frame
"""

description = """
    This class creates a megawidget contained within a Tkinter.Frame
    window.  The class acts as the base class for megawidgets that are
    not contained in their own toplevel window, such as ~ButtonBox~ and
    ~ComboBox~.  It creates a Tkinter.Frame component, named *hull*,
    to act as the container of the megawidget.  The window class name
    for the *hull* widget is set to the most-specific class name for
    the megawidget.  Derived classes specialise this class by
    creating other widget components as children of the *hull* widget.
    
"""

text = {}
text['options'] = {}

text['components'] = {}

text['components']['hull'] = """
    This acts as the body for the entire megawidget.  Other components
    are created as children of the hull to further specialise this
    class.

"""

text['methods'] = {}
