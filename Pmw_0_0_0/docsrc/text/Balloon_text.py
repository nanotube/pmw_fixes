complete = 1
reviewdate = "20 May 2002"

name = """
    display "tool tips" for a number of widgets
"""

description = """
    A balloon megawidget can be used to give short help messages to
    the user when they place the mouse over a button or other widget
    for a short time.  It can also be used to display help messages
    for canvas or text items.

    One balloon megawidget can be used to display help for many
    widgets or items.  For each widget or item that requires balloon
    help, the /bind()/ or /bindtag()/ method is used to specify the
    help text that should be displayed.
    
    The help message is displayed in a popup balloon window when the
    mouse remains over the widget or item for a short time.  The popup
    balloon is withdrawn when the mouse leaves the widget or item, or
    any mouse buttons are pressed.

    The position of the popup balloon is configurable and may appear
    either relative to the widget or item or relative to the position
    of the mouse.

    The popup balloon is displayed without any window manager
    decorations.

    The megawidget can cooperate with a ~MessageBar~ to display a
    single-line help message as well as the balloon help.

"""

text = {}
text['options'] = {}

text['options']['initwait'] = """
    The number of milliseconds delay between when the mouse enters a
    widget or item and when the popup balloon window should be
    displayed.

"""

text['options']['relmouse'] = """
    This may be one of *'both'*, *'x'*, *'y'* or *'none'* and
    indicates that the top left corner of the popup balloon window
    should be placed relative to the current position of the mouse
    rather than relative to the bottom left corner of the widget or
    item (the default).  The positioning may be set for the horizontal
    (x) and vertical (y) axes independently.

"""

text['options']['state'] = """
    This may be one of *'both'*, *'balloon'*, *'status'* or *'none'*
    and indicates whether the help message should be displayed in the
    popup balloon window, in an associated messagebar (via the
    *statuscommand* option), or both.
    
"""

text['options']['statuscommand'] = """
    This specifies a function to call when the mouse enters a widget
    or item bound to this balloon megawidget.  To configure a
    ~MessageBar~ to display help, set this option to the /helpmessage/
    method of the messagebar.
    
"""

text['options']['xoffset'] = """
    This specifies the horizontal offset of the position of the left
    side of the popup balloon window relative the point determined by
    the *relmouse* option.
    
"""

text['options']['yoffset'] = """
    This specifies the vertical offset of the position of the top of
    the popup balloon window relative the point determined by the
    *relmouse* option.
    
"""

text['components'] = {}

text['components']['label'] = """
    This component displays the text of the help message in the popup
    balloon window.  By default it is created with a *'lightyellow'*
    background, a *'black'* foreground and is *'left'* justified.

"""

text['methods'] = {}

text['methods']['bind'] = """
    Create bindings for 'widget' so that balloon help and/or status
    help is displayed when the mouse enters the widget.  The balloon
    help message is given by 'balloonHelp' and the status help message
    is given by 'statusHelp'.  If 'balloonHelp' is *None*, no balloon
    is displayed.  If 'statusHelp' is not set, it defaults to
    'balloonHelp'.  Any previous bindings for this widget are removed.

"""

text['methods']['tagbind'] = """
    Create bindings for the tag or item specified by 'tagOrItem' in
    the text or canvas 'widget' so that balloon help and/or status
    help is displayed when the mouse enters the tag or item.  The
    balloon help message is given by 'balloonHelp' and the status help
    message is given by 'statusHelp'.  If 'balloonHelp' is *None*, no
    balloon is displayed.  If 'statusHelp' is not set, it defaults to
    'balloonHelp'.  Any previous bindings for this tag or item are
    removed.

"""

text['methods']['unbind'] = """
    Remove the balloon help bindings from 'widget'.

"""

text['methods']['tagunbind'] = """
    Remove the balloon help bindings from the tag or item specified by
    'tagOrItem' in the text or canvas 'widget'.

    Note that /tagunbind()/ must be called when deleting a canvas
    item, so that the popup balloon window can be withdrawn if it was
    triggered by the item.  (Unfortunately this can not be automated
    as is done for widgets since Tk does not support /<Destroy>/
    bindings on canvas items, so there is no way that Pmw.Balloon can
    be notified of the deletion of an item.)

"""

text['methods']['clearstatus'] = """
    Clear the text in the associated messagebar by passing *None* to
    the *statuscommand* function.

"""

text['methods']['showstatus'] = """
    Set the text in the associated messagebar by passing 'statusHelp'
    to the *statuscommand* function.

"""
