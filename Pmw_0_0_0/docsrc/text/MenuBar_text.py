complete = 1
reviewdate = "22 April 2000"

name = """
    manager widget for menu buttons and menus
"""

description = """
    This class creates a manager widget for containing menus.  There
    are methods to add menu buttons and menus to the menu bar and for
    adding menu items to the menus.  Menu buttons may be added to the
    left or right of the widget.  Each menu button and menu item may
    have help text to be displayed by a ~Balloon~ widget.  Each menu
    and cascaded menu (sub-menu) is referenced by name which is
    supplied on creation.

"""

sections = (
    ('Dynamic components', 1, 'Components', 
	"""
	Menu button components are created dynamically by the
        /addmenu()/ method.  By default, these are of type
        Tkinter.Menubutton and are created with a component group of
        *Button*.

        Menu components are created dynamically by the /addmenu()/ and
        /addcascademenu()/ methods.  By default, these are of type
        Tkinter.Menu and are created with a component group of *Menu*.

	"""
    ),
)

text = {}

text['options'] = {}

text['options']['balloon'] = """
    Specifies a ~Balloon~ widget to display the help text for menu
    buttons and menu items.  If *None*, no help is displayed.  If the
    balloon has an associated ~MessageBar~, the help text will also be
    displayed there.

"""

text['options']['hotkeys'] = """
    If true, keyboard accelerators will be assigned to each menu
    button and menu item.  Keyboard accelerators can be used to access
    the menus without using the mouse.  The accelerator character is
    always one of the alphanumeric characters in the text label of the
    menu or menu item and is indicated by an underline.
    
    To select a menu, simultaneously press the *<Alt>* key and the
    accelerator character indicated on a menu button.  The arrows keys
    can then be used to select other menus and menu items.  To invoke a
    menu item, press *<Return>* or press the accelerator character
    indicated on the menu item.

    Each accelerator character will be assigned automatically unless
    'traverseSpec' is supplied to the /addmenu()/, /addmenuitem()/ or
    /addcascademenu()/ methods.  The automatically selected
    accelerator character for a menu button (or menu item) is the
    first character in the label text that has not already been used
    as an accelerator for a menu button (or in the menu containing the
    menu item).

    If 'traverseSpec' is given, it must be either an integer or a
    character.  If an integer, it specifies the index of the character
    in the label text to use as the accelerator character.  If a
    character, it specifies the character to use as the accelerator
    character.

"""

text['options']['padx'] = """
    Specifies a padding distance to leave between each menu button in
    the x direction and also between the menu buttons and the outer
    edge of the menu bar.

"""

text['components'] = {}

text['methods'] = {}
text['methods']['addmenu'] = """
    Add a menu button and its associated menu to the menu bar.  The
    'menuName' argument must not be the same as any menu already
    created using the /addmenu()/ or /addcascademenu()/ methods.
    
    Any keyword arguments present (except *tearoff*) will be passed to
    the constructor of the menu button.  If the *text* keyword
    argument is not given, the *text* option of the menu button
    defaults to 'menuName'.  If the *underline* keyword argument is
    not given (and the *hotkeys* megawidget option is true) the
    *underline* option is determined as described under *hotkeys* and
    is used to specify the keyboard accelerator.  Each menu button is
    packed into the menu bar using the given 'side', which should be
    either *left* or *right*.  The menu button is created as a
    component named 'menuName'-*button*.

    If the *balloon* option has been defined, 'balloonHelp' and
    'statusHelp' are passed to the balloon as the help strings for the
    menu button.  See the /bind()/ method of ~Balloon~ for how these
    strings may be displayed.

    The *tearoff* keyword argument, if present, is passed to the
    constructor of the menu.  The menu is created as a component named
    'menuName'-*menu*.

"""

text['methods']['addcascademenu'] = """
    Add a cascade menu (sub-menu) to the menu 'parentMenuName'.  The
    'menuName' argument must not be the same as any menu already
    created using the /addmenu()/ or /addcascademenu()/ methods.
    
    A menu item in the parent menu is created (with the
    /add_cascade()/ method of the parent menu) using all keyword
    arguments except *tearoff*.

    If the *label* keyword argument is not given, the *label* option
    of the menu item defaults to 'menuName'.  If the *underline*
    keyword argument is not given (and the *hotkeys* megawidget option
    is true) the *underline* option is determined as described under
    *hotkeys* and is used to specify the keyboard accelerator.

    The 'statusHelp' argument is used as the help string for the menu
    item.  This is displayed using the /showstatus()/ method of the
    balloon.

    The *tearoff* keyword argument, if present, is passed to the
    constructor of the menu.  The menu is created as a component named
    'menuName'-*menu*.

"""

text['methods']['addmenuitem'] = """
    Add a menu item to the menu 'menuName'.  The kind of menu item is
    given by 'itemType' and may be one of *command*, *separator*,
    *checkbutton*, *radiobutton* or *cascade* (although cascade menus
    are better added using the /addcascademenu()/ method).  Any
    keyword arguments present will be passed to the menu when creating
    the menu item.  See Tkinter.Menu for the valid options for each
    item type.  In addition, a keyboard accelerator may be
    automatically given to the item, as described under *hotkeys*. 

    When the mouse is moved over the menu item, the 'helpString' will
    be displayed by the *balloon*'s *statuscommand*.
    
"""

text['methods']['deletemenuitems'] = """
    Delete menu items from the menu 'menuName'.  If 'end' is not
    given, the 'start' item is deleted.  Otherwise all items from
    'start' to 'end' are deleted.
    
"""

text['methods']['deletemenu'] = """
    Delete the menu 'menuName' and all its items.  The menu may either
    be a toplevel menu (in which case the corresponding menu button is
    also deleted) or a cascade menu.
    
"""

text['methods']['disableall'] = """
    Disable all toplevel menus.
    
"""

text['methods']['enableall'] = """
    Enable all toplevel menus.
    
"""
