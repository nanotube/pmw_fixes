name = """
    functions for handling colors and color schemes
    
"""

description = """
    This is a set of functions for manipulating colors and for
    modifying the color scheme of an application or a widget.
    Colors can be represented in a number of ways:

	*name* -- a standard color name, eg /\'orange\'/ or /\'#ffa500\'/

	*rgb* -- a 3-element sequence of red, green and blue intensities
	each between 0.0 (dark) and 1.0 (light), eg /[1.0, 0.6, 0.0]/.

	*hsi* -- a 3-element sequence ('hue', 'saturation',
	'intensity').  The value of 'hue' is between 0.0 and *2pi*
	(6.28318) giving a range of colors covering, in order, red,
	orange, yellow green, cyan, blue, magenta and back to red. 
	The value of 'saturation' is between 0.0 (grey) and 1.0
	(brilliant) and the value of 'intensity' is between 0.0 (dark)
	and 1.0 (bright).

    *brightness* As used in these functions, the brightness of a color
    is the brightness as registered by the human eye.  For example,
    even though the colors red, blue and yellow have the same
    intensity (1.0), they have different brightnesses, 0.299, 0.114
    and 0.886 respectively, reflecting the different way these colors
    appear to the eye.  The brightness of a color is a value between
    0.0 (dark) and 1.0 (bright).

    *color scheme* A color scheme is a set of colors defined for each
    of the default color options in the Tk option database.  Color
    schemes can be used in two ways.  Firstly, using
    /Pmw.Color.setscheme()/, the Tk option database can be set to the
    values in the color scheme.  This will not have any effect on
    currently existing widgets, but any new widgets created after
    setting the options will have these colors as their defaults. 
    Secondly, using /Pmw.Color.changecolor()/ the color scheme can be
    used to change the colors of a widget and all its child widgets.

    A color scheme is specified by defining one or more color options
    (one of the defined options must be /background/).  Not all
    options need be specified - if any options are not defined, they
    are calculated from the other colors.  These are the options used
    by a color scheme, together with their values if not specified:

      # background:            (must be specified)
      # foreground:            black
      # activeForeground:      same as foreground
      # insertBackground:      same as foreground
      # selectForeground:      same as foreground
      # highlightColor:        same as foreground
      # disabledForeground:    between fg and bg but closer to bg
      # highlightBackground:   same as background
      # activeBackground:      a little lighter that bg
      # selectBackground:      a little darker that bg
      # troughColor:           a little darker that bg
      # selectColor:           yellow

"""

text = {}

text['functions'] = {}

text['functions']['changebrightness'] = """
    Find the hue of the color 'colorName' and return a color of this
    hue with the required 'brightness'.

"""

text['functions']['changecolor'] = """
    Change the color of 'widget' and all its child widgets according
    to the color scheme specified by the other arguments.  This is done
    by modifying all of the color options of existing widgets that
    have the default value.  The color options are the lower case
    versions of those described in the *color scheme* section.  Any
    options which are different to the previous color scheme (or the
    defaults, if this is the first call) are not changed.

    For example to change a widget to have a red color scheme with a
    white foreground:

    # Pmw.Color.changecolor(widget,
    #     background = 'red3', foreground = 'white')

    The colors of widgets created after this call will not be
    affected.

    Note that 'widget' must be a Tk widget or toplevel.  To change the
    color of a Pmw megawidget, use it's *hull* component.  For example:

    # widget = megawidget.component('hull')
    # Pmw.Color.changecolor(widget, background = 'red3')

"""

text['functions']['getdefaultpalette'] = """
    Return a dictionary of the default values of the color options
    described in the *color scheme* section.

    To do this, a few widgets are created as children of 'root', their
    defaults are queried, and then the widgets are destroyed.  (Tk
    supplies no other way to get widget default values.)

    Note that 'root' must be a Tk widget or toplevel.  To use a Pmw
    megawidget as the root, use it's *hull* component.  For example:

    # root = megawidget.component('hull')
    # Pmw.Color.getdefaultpalette(root)

"""

text['functions']['hsi2rgb'] = """
    Return a list of *rgb* values of the color corresponding to 'hue',
    'saturation' and 'intensity'.

"""

text['functions']['hue2name'] = """
    Return the color with the specified 'hue' and 'brightness'.  If
    'hue' is *None*, return a grey of the requested brightness. 
    Otherwise, the value of 'hue' should be as described above.

"""

text['functions']['rgb2hsi'] = """
    Return a tuple ('hue', 'saturation', 'intensity') corresponding to
    the color specified by the 'rgb' sequence.

"""

text['functions']['setscheme'] = """
    Set the color scheme for the application by setting default colors
    (in the Tk option database of the root window of 'root') according
    to the color scheme specified by the other arguments.

    For example to initialise an application to have a red color
    scheme with a white foreground:

    # Pmw.Color.setscheme(root,
    #     background = 'red3', foreground = 'white')

    This function does not modify the colors of already existing
    widgets.  Use *Pmw.Color.changecolor()* to do this.

    Note that 'root' must be a Tk widget or toplevel.  To use the Tk
    option database of the root window or a Pmw megawidget, use the
    megawidget's *hull* component.  For example:

    # root = megawidget.component('hull')
    # Pmw.Color.setscheme(root, background = 'red3')

"""
