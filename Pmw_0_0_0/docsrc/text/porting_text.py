text = """
    This document contains a brief guide to porting existing code
    between different versions of Pmw.  It includes significant
    functionality changes but does not include bug fixes or compatible
    enhancements.  For details of all changes, see
    ~~changes.html~~Changes to Pmw versions~~.
    
    *Porting from 0.8.5 to 1.0*

    - Bug fix, documention and new features only.  No
      backwards-incompatible changes.

    *Porting from 0.8.4 to 0.8.5*

    - Bug fix release only. No interface changes.

    *Porting from 0.8.3 to 0.8.4*

    - Change the /setnaturalpagesize()/ method of Pmw.NoteBook to
      /setnaturalsize()/ (to be consistent with Pmw.PanedWidget).

    - Change Pmw.excludefrombusycursor() to Pmw.setbusycursorattributes().
      Replace busyCursorName option of Pmw.initialise() with
      cursorName attribute of Pmw.setbusycursorattributes().

    - Several rarely used key bindings for Pmw.ScrolledListBox were
      removed, changing the behaviour of the megawidget.

    *Porting from 0.8.1 to 0.8.3*

    - The megawidgets Pmw.NoteBookR and Pmw.NoteBookS have been
      replaced by a new Pmw.NoteBook.  The interfaces are not
      compatible, so see the Pmw.NoteBook reference manual for
      details.

    - Change the get() method of Pmw.OptionMenu to getcurselection()
      and the remove() method of Pmw.PanedWidget to delete().

    - If you use *'end'*, *'default'* or *None* in calls to the
      index() method of several megawidgets, change these to
      *Pmw.END*, *Pmw.DEFAULT* and *Pmw.SELECT*, respectively.

    - The exclude argument has been removed from Pmw.showbusycursor(). 
      Use Pmw.excludefrombusycursor() instead.

    - The names of some of the positional arguments in the following
      methods have changed:  MegaArchetype.createcomponent(),
      ButtonBox.insert(), ButtonBox.add(), MenuBar.addcascademenu(),
      MenuBar.addmenuitem() and RadioSelect.add().

    - The Pmw.maxfontwidth() function has been removed.  Use the
      /font_measure()/ Tkinter method, or if that has not yet been
      implemented:

      # someWidget.tk.call('font', 'measure', someFont, 'W')

    - The Pmw.fontexists() function has been removed.  This is
      because, since Tk8.0, all fonts exist, so it no longer has
      any meaning.

    *Porting from 0.8 to 0.8.1*

    - The Blt.Graph now supports blt2.4i which is not backwards
      compatible with blt2.1.

    *Porting from 0.7 to 0.8*

    - The 'format' argument of Pmw.datestringtojdn() now defaults to
      *'ymd'*.  If you want to display dates with year, month and day
      in a different order, add a 'format' option to
      Pmw.datestringtojdn() or to the *datatype* option of Pmw.Counter
      or the *validate* option of Pmw.EntryField.

    - The justify() method from Pmw.ScrolledListBox has been removed. 
      Use the xview() or yview() methods instead.

    - Replace the getFrame() method of Pmw.ScrolledFrame with the
      interior() method.

    - Replace the *ringpadx* and *ringpady* options of Pmw.Group by
      padding the megawidget itself or by padding the children of the
      megawidget. 

    - Replace the canvasbind() and canvasunbind() methods of
      Pmw.Balloon with tagbind() and tagunbind().

    - The return value of Pmw.EntryField *command* callback is now
      ignored.  Previously, if the callback destroyed the megawidget,
      it was required to return the string *'break'*, to work around a
      problem in the event handling mechanism in Tkinter.  With python
      1.5.2, Tkinter has been fixed.  Therefore, user-supplied
      callback functions should use Pmw.hulldestroyed to check if the
      megawidget has been destroyed before performing any operations
      on it.

    - If you require the *'pmw1'* fontScheme when running under
      Microsoft Windows and Macintosh, you will need to set the Tk
      font options manually.

    *Porting from 0.6 to 0.7*

    - Replace the *maxwidth* option of Pmw.EntryField with the *'max'*
      field of the *validate* option.

    - To specify that there should be no validation performed for a
      Pmw.EntryField, the *validate* option must be None, not *''* as
      before.

    - The date and time values of the Pmw.EntryField *validate* option
      (such as *'date_dmy'* and *'time24'*, etc) are no longer supported. 
      Instead use a dictionary as the value of the *validate* option
      with *'date'* or *'time'* in the *'validator'* field.  Include
      other fields in the dictionary to further specify the
      validation.

    - Pmw.Counter no longer supports the old date and time values for
      the *datatype* option.  Use a dictionary with a *'counter'*
      field of *'date'* or *'time'* and other fields to further
      specify the counting.

    - Pmw.Counter no longer supports the *min* and *max* options.  Use
      the Pmw.EntryField *validate* option instead.

    - The bbox method of Pmw.ScrolledListBox now refers to the bbox
      method of the *listbox* component, not the *hull* component.

    - By default, Pmw.MenuBar now automatically adds hotkeys to menus
      and menu items for keyboard traversal.  To turn this off, use the
      /hotkeys = 0/ option.

    - The createcomponent() method now disallows the creation of
      component names containing an underscore.  If any component
      names contain an underscore, rename them.

    *Porting from 0.5 to 0.6*

    To port applications using Pmw version 0.5 to version 0.6, make
    sure you are using python1.5.  Then, simply change any lines in
    your application like this:

    # from PmwLazy import Pmw

    to this:

    # import Pmw

    Also, if you have added the /lib/ directory of a specific version
    of Pmw to /sys.path/ or /PYTHONPATH/, this can be removed, as long
    as Pmw can now be found from the default path, such as in the
    python /site-packages/ directory.

    *Porting from 0.2 to 0.4*

    - To get Pmw.0.2 default fonts (helvetica with bold italic menus
      and italic scales) initialise with:

      # Pmw.initialise(fontScheme = 'pmw1')

      If no *fontScheme* is given, the standard Tk default fonts are used.

    - Remove all calls to setdefaultresources(), usual(), keep(),
      renameoptions(), ignore() and defineoptiontypes().

    - Move call to defineoptions() to before call to base class
      constructor, create optiondefs tuple from self.defineoptions
      arguments, then call defineoptions().

    - Remove resource class and name from optiondefs.

    - The last element in the optiondefs tuple (callback function)
      must be given (may be None).

    - Add to classes currently without any options:

      # optiondefs = ()
      # self.defineoptions(kw, optiondefs)

    - Use createcomponent() to create components - this replaces the
      calls to the component widget constructor and to
      registercomponent().

    - Do not inherit from Pmw.LabeledWidget.  Instead, replace with
      Pmw.MegaWidget with labelpos and labelmargin options and a call
      to self.createlabel().  If calling createlabel(), must replace
      pack() with grid().

    - When calling a megawidget constructor, include subcomponent name when
      setting subcomponent options (eg labeltext -> label_text)

    - The items option of ScrolledListBox is an initialisation option
      only - use setlist() method after initialisation.

    - The *autorelief* option for Counter, EntryField, ScrolledText,
      TextDialog has been removed.

    - ScrolledListBox.getcurselection() always returns a tuple of strings,
      possibly of zero length.

    - Counter increment is always initialised to 1.

    - The *'time'* Counter *datatype* option has been replaced by
      *'timeN'* and *'time24'*.

    - The *'time'* EntryField *validate* option has been replaced by
      *'timeN'* and *'time24'*.

    - Replace call to initialise() with initialiseoptions(), removing
      "kw" arg.  This should always be the last line in a megawidget
      constructor.

    - Replace hide() with withdraw().

    - Now need iconpos option for MessageDialogs with icon_bitmap option set.

    - Example megawidget class definition:

    #class MyBigWidget(Pmw.MegaWidget):
    #    def __init__(self, parent = None, **kw):
    #
    #        # Define the megawidget options.
    #        optiondefs = (
    #            ('errorbackground',   'pink',      None),
    #            ('maxwidth',          0,           self._myfunc),
    #            ('myinit',            'good',      Pmw.INITOPT),
    #        )
    #        self.defineoptions(kw, optiondefs)
    #
    #        # Initialise the base class (after defining the options).
    #        Pmw.MegaWidget.__init__(self, parent)
    #
    #        # Create the components.
    #        interior = self.interior()
    #        self._widget = self.createcomponent('component',
    #                (('alias', 'component_alias'),), None,
    #                Tkinter.Button, (interior,))
    #        self._widget.grid(column=0, row=0, sticky='nsew')
    #
    #        self.createlabel(interior)
    #
    #        # Initialise instance variables.
    #        self.deriveddummy = None
    #
    #        # Check keywords and initialise options.
    #        self.initialiseoptions(MyBigWidget)
"""
