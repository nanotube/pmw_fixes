complete = 1

name = """
    frame subdivided into several resizable panes
"""

description = """
    This class creates a manager widget for containing resizable
    frames, known as panes.  Each pane may act as the container for
    other widgets.  The user may resize the panes by dragging a small
    rectangle (the handle) or the line between the panes (the separator).
    The panes may be arranged horizontally or vertically.

"""

sections = (
    ('Dynamic components', 1, 'Components', 
	"""
	Frame, separator and handle components are created dynamically
	by the /add()/ and /insert()/ methods.  The components are of type
	Tkinter.Frame and are created with component groups of
	*Frame*, *Separator* and *Handle* respectively.

	"""
    ),
    ('Pane options', 1, 'Options', 
	"""
	Each pane has the following options.  These may be set when
	creating or configuring a pane.  The value of each option may
	be an integer, which specifies a pane size in pixels, or a
	real number between 0.0 and 1.0, which specifies a pane size
        proportional to the size of the entire paned widget.

	*size* -- Specifies the initial size of the pane.  The default is *0*.

	*min* -- Specifies the minimum size of the pane.  The default is *0*.

	*max* -- Specifies the maximum size of the pane.  The default is a
	    very large number.

	"""
    ),
)

text = {}
text['options'] = {}

text['options']['command'] = """
    Specifies a function to be called whenever the size of any of the
    panes changes.  The function is called with a single argument,
    being a list of the sizes of the panes, in order.  For *vertical*
    orientation, the size is the height of the panes.  For
    *horizontal* orientation, the size is the width of the panes.

"""

text['options']['orient'] = """
    Specifies the orientation of the paned widget.  This may be
    *'horizontal'* or *'vertical'*.  If *'vertical'*, the panes are
    stacked above and below each other, otherwise the panes are laid
    out side by side.

"""

text['options']['separatorrelief'] = """
    Specifies the relief of the line separating the panes.

"""

text['components'] = {}

text['methods'] = {}

text['methods']['add'] = """
    Add a pane to the end of the paned widget as a component named
    'name'.  This is equivalent to calling /insert()/ with 'before'
    set to the current number of panes.  The method returns the 'name'
    component widget.

"""

text['methods']['configurepane'] = """
    Configure the pane specified by 'name', where 'name' is either an
    integer, specifying the index of the pane, or a string, specifying
    the name of the pane.  The keyword arguments specify the new
    values for the options for the pane.  These options are described
    in the *Pane options* section.

"""

text['methods']['insert'] = """
    Add a pane to the paned widget as a component named 'name'.  The
    pane is added just before the pane specified by 'before', where
    'before' may be either an integer, specifying the index of the
    pane, or a string, specifying the name of the pane.  The keyword
    arguments specify the initial values for the options for the new
    pane.  These options are described in the *Pane options* section. 
    To add a pane to the end of the paned widget, use /add()/.

    The new pane is created as a Tkinter.Frame component named 'name'. 
    If this is not the only pane, a separator and handle are also
    created as components named *separator*-'n' and *handle*-'n',
    where 'n' is one less than the number of panes.  The method
    returns the 'name' component widget.
    
"""

text['methods']['pane'] = """
    Return the Tkinter.Frame pane widget for the pane specified by
    'name', where 'name' is either an integer, specifying the index of
    the pane, or a string, specifying the name of the pane.

"""

text['methods']['panes'] = """
    Return a list of the names of the panes, in display order.

"""

text['methods']['delete'] = """
    Delete the pane specified by 'name', where 'name' is either an
    integer, specifying the index of the pane, or a string, specifying
    the name of the pane.

    If the pane deleted was not the only pane in the paned widget,
    also delete the separator and handle components named
    *separator*-'n' and *handle*-'n', where 'n' is the number of
    panes remaining.
    
"""
