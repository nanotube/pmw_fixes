complete = 1
reviewdate = "22 April 2000"

name = """
    manager for toplevel native menus
"""

description = """
    This class is a wrapper for the Tkinter.Menu class.  It should be
    used as the main menu of toplevel windows. The class is similar
    to ~MenuBar~, but should be used when native menus are required.
    See the Tkinter.Menu documentation for full details.

    This class should be created as the child of a Tkinter.Toplevel
    and should then be specified as the menu associated with the
    toplevel, using the toplevel's /configure()/ method.  For example:

        # # Create a Pmw.MegaToplevel.
        # megaToplevel = Pmw.MegaToplevel()
        # # Get the Tkinter.Toplevel from Pmw.MegaToplevel.
        # toplevel = megaToplevel.interior()
        # # Create the menu bar for the toplevel.
        # menuBar = Pmw.MainMenuBar(toplevel)
        # # Configure the toplevel to use the menuBar.
        # toplevel.configure(menu = menuBar)
    
    There are methods to add menus, both as toplevel menus and
    sub-menus, and for adding menu items to the menus.  Each menu item
    may have help text to be displayed by a ~Balloon~ widget.  Each
    menu and cascaded menu (sub-menu) is referenced by name which is
    supplied on creation.

    This megawidget is derived from ~MegaArchetype~ (not ~MegaWidget~
    like most other megawidgets), with the hull class being
    Tkinter.Menu.

    (Note that due to bugs in Tk's menubar functionality, balloon
    help has not been impleted and status help does not work properly.)

"""

sections = (
    ('Dynamic components', 1, 'Components', 
	"""
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
    items.  If *None*, no help is displayed.  If the balloon has an
    associated ~MessageBar~, the help text will also be displayed
    there.

    Due to a bug in some versions of Tk (8.0 and possible others),
    help text will not be displayed in the balloon widget.  However,
    help text will be displayed in the balloon's associated
    messagebar.

"""

text['options']['hotkeys'] = """
    If true, keyboard accelerators will be assigned to each menu item. 
    Keyboard accelerators can be used to access the menus without
    using the mouse.  The accelerator character is always one of the
    alphanumeric characters in the text label of the menu item and is
    indicated by an underline.
    
    To select a menu, simultaneously press the *<Alt>* key and the
    accelerator character indicated on a toplevel menu item.  The
    arrows keys can then be used to select other menus and menu items. 
    To invoke a menu item, press *<Return>* or press the accelerator
    character indicated on the menu item.

    Each accelerator character will be assigned automatically unless
    'traverseSpec' is supplied to the /addmenu()/, /addmenuitem()/ or
    /addcascademenu()/ methods.  The automatically selected
    accelerator character for a menu item is the first character in
    the label text that has not already been used as an accelerator in
    the menu containing the menu item.

    If 'traverseSpec' is given, it must be either an integer or a
    character.  If an integer, it specifies the index of the character
    in the label text to use as the accelerator character.  If a
    character, it specifies the character to use as the accelerator
    character.

"""

text['components'] = {}

text['components']['hull'] = """
    The toplevel menu widget.

"""

text['methods'] = {}
text['methods']['addmenu'] = """
    Add a cascade menu to the toplevel menu.  The 'menuName' argument
    must not be the same as any menu already created using the
    /addmenu()/ or /addcascademenu()/ methods.
    
    A menu item in the toplevel menu is created (with the
    /add_cascade()/ method) using all keyword arguments except
    *tearoff* and *name*.

    If the *label* keyword argument is not given, the *label* option
    of the menu button defaults to 'menuName'.  If the *underline*
    keyword argument is not given (and the *hotkeys* megawidget option
    is true) the *underline* option is determined as described under
    *hotkeys* and is used to specify the keyboard accelerator.

    The 'statusHelp' argument is used as the help string for the menu
    item.  This is displayed using the /showstatus()/ method of the
    balloon.  Currently 'balloonHelp' is not used, due to a bug in Tk
    version 8.0.

    The *tearoff* and *name* keyword arguments, if present, are passed
    to the constructor of the menu.  See Tkinter.Menu for details of
    these options.  The menu is created as a component named
    'menuName'.

"""

text['methods']['addcascademenu'] = """
    Add a cascade menu (sub-menu) to the menu 'parentMenuName'.  The
    'menuName' argument must not be the same as any menu already
    created using the /addmenu()/ or /addcascademenu()/ methods.
    
    A menu item in the parent menu is created (with the
    /add_cascade()/ method of the parent menu) using all keyword
    arguments except *tearoff* and *name*.

    If the *label* keyword argument is not given, the *label* option
    of the menu item defaults to 'menuName'.  If the *underline*
    keyword argument is not given (and the *hotkeys* megawidget option
    is true) the *underline* option is determined as described under
    *hotkeys* and is used to specify the keyboard accelerator.

    The 'statusHelp' argument is used as the help string for the menu
    item.  This is displayed using the /showstatus()/ method of the
    balloon.

    The *tearoff* and *name* keyword arguments, if present, are passed
    to the constructor of the menu.  See Tkinter.Menu for details of
    these options.  The menu is created as a component named
    'menuName'.

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
    be a toplevel menu or a cascade menu.
    
"""

text['methods']['disableall'] = """
    Disable all toplevel menus.
    
"""

text['methods']['enableall'] = """
    Enable all toplevel menus.
    
"""
