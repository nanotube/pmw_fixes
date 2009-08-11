reviewdate = "25 May 2002"

name = """
    contains functions for handling colors and color schemes
    
"""

description = """
    This module is a set of functions for manipulating colors and for
    modifying the color scheme of an application or a widget.  Many of
    the functions in this module take or return colors.  These values
    may represent colors in the following ways:

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

    As used in these functions, the *brightness* of a color is the
    perceived grey level of the color as registered by the human eye. 
    For example, even though the colors red, blue and yellow have the
    same intensity (1.0), they have different brightnesses, 0.299,
    0.114 and 0.886 respectively, reflecting the different way these
    colors appear to the eye.  The brightness of a color is a value
    between 0.0 (dark) and 1.0 (bright).

    A *color scheme* is a set of colors defined for each of the
    default color options in the Tk option database.  Color schemes
    can be used in two ways.  Firstly, using /Pmw.Color.setscheme()/,
    the Tk option database can be set to the values in the color
    scheme.  This will not have any effect on currently existing
    widgets, but any new widgets created after setting the options
    will have these colors as their defaults.  Secondly, using
    /Pmw.Color.changecolor()/ the color scheme can be used to change
    the colors of a widget and all its child widgets.

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

    There are many functions in this module.  As well as
    /Pmw.Color.setscheme()/ and /Pmw.Color.changecolor()/, some of the
    most useful are /Pmw.Color.spectrum()/,
    /Pmw.Color.changebrightness()/ and
    /Pmw.Color.getdefaultpalette()/.

"""

text = {}

text['functions'] = {}

text['functions']['average'] = """
    Return an *rgb* color 'fraction' of the way "between" the colors
    'rgb1' and 'rgb2', where 'fraction' must be between *0.0* and
    *1.0*.  If 'fraction' is close to *0.0*, then the color returned
    will be close to 'rgb1'.  If it is close to *1.0*, then the color
    returned will be close to 'rgb2'.  If it is near *0.5*, then the
    color returned will be half way between the two colors.

"""

text['functions']['bordercolors'] = """
    Return a tuple /(light, dark)/ of color names that can be used as
    the light and dark border shadows on a widget where the background
    is 'colorName'.  This is the same method that Tk uses for shadows
    when drawing reliefs on widget borders.  The 'root' argument is
    only used to query Tk for the *rgb* values of 'colorName'.

"""

text['functions']['name2rgb'] = """
    Return 'colorName' as an *rgb* value.  If 'asInt' is true, then
    the elements of the return sequence are in the range *0* to
    *65535* rather than *0.0* to *1.0*.  The 'root' argument is only
    used to query Tk for the *rgb* values of 'colorName'.

"""

text['functions']['correct'] = """
    Return the "corrected" value of 'rgb'.  This can be used to
    correct for dull monitors.  If 'correction' is less than *1.0*,
    the color is dulled.  If 'correction' is greater than *1.0*, the
    color is brightened.

"""

text['functions']['changebrightness'] = """
    Find the hue of the color 'colorName' and return a color of this
    hue with the required 'brightness'.  If 'brightness' is *None*,
    return the name of color with the given hue and with saturation
    and intensity both *1.0*.  The 'root' argument is only used to
    query Tk for the *rgb* values of 'colorName'.

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
    Return the *rgb* representation of the color represented by 'hue',
    'saturation' and 'intensity'.

"""

text['functions']['bhi2saturation'] = """
    Return the saturation of the color represented by 'brightness',
    'hue' and 'intensity'.

"""

text['functions']['rgb2brightness'] = """
    Return the brightness of the color represented by 'rgb'.

"""

text['functions']['rgb2name'] = """
    Return the name of the color represented by 'rgb' as a string of
    the form /\'#RRGGBB\'/ suitable for use with Tk color functions.

"""

text['functions']['spectrum'] = """
    Return a list of 'numColors' different colors making up a
    \'spectrum\'.  If 'extraOrange' is false, the colors are evenly
    spaced by hue from one end of the spectrum (red) to the other
    (magenta).  If 'extraOrange' is true, the hues are not quite
    evenly spaced - the hues around orange are emphasised, thus
    preventing the spectrum from appearing to have to many \'cool\'
    hues. 

    If 'returnHues' is false, the return values are the names of the
    colors represented by the hues together with 'saturation' and
    'intensity' and corrected by 'correction'.

    If 'returnHues' is true, the return values are hues.

"""

text['functions']['hue2name'] = """
    Return the name of the color with the specified 'hue' and
    'brightness'.  If 'hue' is *None*, return a grey of the requested
    brightness.  Otherwise, the value of 'hue' should be as described
    above.  If 'brightness' is *None*, return the name of color with
    the given hue and with saturation and intensity both *1.0*.

"""

text['functions']['rgb2hsi'] = """
    Return a tuple ('hue', 'saturation', 'intensity') corresponding to
    the color specified by the 'rgb' sequence.

"""

text['functions']['setscheme'] = """
    Set the color scheme for the application by setting default colors
    (in the Tk option database of the root window of 'root') according
    to the color scheme specified by the other arguments.  This will
    affect the initial colours of all widgets created after the call
    to this function.

    For example to initialise an application to have a red color
    scheme with a white foreground:

    # Pmw.Color.setscheme(root,
    #     background = 'red3', foreground = 'white')

    This function does not modify the colors of already existing
    widgets.  Use *Pmw.Color.changecolor()* to do this.

    Note that 'root' must be a Tk widget or toplevel.  To use the Tk
    option database of the root window of a Pmw megawidget, use the
    megawidget's *hull* component.  For example:

    # root = megawidget.component('hull')
    # Pmw.Color.setscheme(root, background = 'red3')

"""
