text = """
  6 January 1997

  - Release of version 0.1

  14 February 1997

  - Fixed bug in Counter demo for the Macintosh - the maximum size of an
    integer is smaller than the value returned by time.time().

  - Fixed bug in Grid demo for Tk 4.2 - grid_bbox returns garbage if it is
    called without update_idletasks.  Also, grid_bbox can only have two
    arguments in Tk 4.1.

  - Modified ScrolledText demo so that the text widget contains enough text
    to require a vertical scrollbar.

  - Changes to PmwBase:

    - Prefixed the name of several private variables with a double underscore.

    - Added symbolic constants for the indexes into an optionInfo list.

    - Changed names of several methods and variables to be more descriptive.

    - Removed options() method.

    - Simplified configuration option data structures.  Modified option
      handling code so that default options are set correctly.  If an
      option is created before initialise() is called then initialise()
      checks if the option is set by the keyword arguments to
      initialise().  If not, then it is given the value found in the
      Tk option database, if a value exists, or the default value.  If an
      option is created after initialise() is called, then it is given the
      value found in the Tk option database, if a value exists, or the
      default value.

  - Replaced usage of self._hull in megawidgets by interior() method.

  - Added autoclear option to ComboBox.

  - Fixed bug in ComboBox - fast clicking on the arrow button could result
    in an attempt to grab a window that was not yet visible.

  - Added "sys.exc_traceback = None" to the except clauses of all try
    statements so that references to objects in the stack trace would not
    be left.

  - Added takefocus option to PushButton.

  - Modified the getcurselection() method of ScrolledListBox so that it
    returns a string if the selection mode is *'single'* or *'browse'*, rather
    than a tuple with one element.  This also affects methods forwarded and
    derived from ScrolledListBox.

  - Modified ScrolledListBox so that it avoids unnecessary updates by
    using idle timer.

  - Modified ScrolledText to use grid instead of pack.

  - Added shutdown() function to Tk module to clean up all references to
    the Tcl interpreter and then delete it.

  - Fixed bug in Tk module for the Macintosh - update() was being called in
    initialise() before the Tcl interpreter was created.

  14 February 1997

  - Version 0.1.1 completed and released internally.

  6 March 1997

  - Pmw now uses the standard Tkinter module.  The Tk module has been
    dropped.  This means that the Tk module functions such as after,
    bell, bind, update, etc, are no longer available and the equivalent
    Tkinter methods should be used.
    
  - To restore some of the features of the Tk module, Pmw.initialise()
    now adds run-time hooks into Tkinter to get notification of when Tk
    widgets are created and destroyed.  It also modifies the CallWrapper
    class so that errors during callbacks and bindings can be displayed
    in a window.  If Pmw.initialise() is not called, Tkinter is not
    modified and these features are not available.

  - If a Tk widget which is acting as the hull of a megawidget is
    destroyed, then the megawidget is destroyed as well.  This can
    only happen if Pmw.initialise() is called.

  - Pmw.initialise() now takes the Tkinter root as its argument.

  - The parent of megawidgets now defaults to the Tk root.  Previously,
    the parent of non-toplevel megawidgets had to be given.

  - Added PmwBase.tracetk() function to get trace of calls to the Tcl
    interpreter for debugging.

  - Added functions to PmwBase to display a busy cursor over the
    application such as when a modal dialog is displayed or it is
    blocked doing a long calculation.  Uses busy command of the blt
    extension, if present.

  - Created a nifty new demo which demonstrates most of the megawidgets
    in a convenient way.

  - Added a TextDialog.

  - Added functionality to handle the grabbing of nested modal dialogs
    correctly.

  - Added an activatecommand option to Dialog which allows, for example,
    the PromptDialog widget to set the keyboard focus when it is
    activated.

  - Added tests for Counter and logicalfont.

  - The ScrolledListBox selectioncommand is no longer given the widget
    as its first argument.

  - Several method, function and component names were changed, to be
    consistent with the coding conventions.

  - Some of the effects of moving from the Tk module to Tkinter are:

    - The Tk module used to exit if there were no non-root toplevel
      windows shown.  This is no longer the case and so the application
      must handle this explicitly, particularly if the root window is
      withdrawn and the last non-root toplevel is deleted by the window
      manager.

    - The Tk module bind functions and methods used to take a noEvent
      argument to indicate that the Tk event should not be passed to the
      callback.  Tkinter does not support this.

    - The Tk module initialise() function should be replaced by
      "root = Tkinter.Tk()" and root should be used instead of "Tk.Root()"

    - The Tk module quit() function should be replace by "root.destroy()".

    - Toplevels are not hidden when created.  To be consistent,
      MegaToplevels are not hidden either.

    - The hide and show methods are not available for Tkinter Toplevels,
      only MegaToplevels

    - There is no grid_configure method.

    - Tkinter.Canvas.coords() returns a python list, not a tuple.

    - The Tkinter cget and configure widget methods always return
      strings for the option values.  The Tk module used to convert the
      string to the appropriate python type (such as string, integer,
      float, Variable, Image, callback function).

    - Tkinter Menu and Toplevel classes incorrectly have a pack method.

    - Menu class has no geometry method.

    - Canvas focus returns *''* rather than None.

    - Text mark_gravity returns *''* rather than None.

  13 March 1997

  - Release of version 0.2

  17 March 1997

  - Set default WM_DELETE_WINDOW protocol of Tkinter.Toplevel to
    destroy() and removed duplicated protocol request from all demos.

  - Modified text of ShowBusy demo to indicate that busy cursor will
    only be seen if the BLT extension is present.

  - Replaced call to update() in PmwLabeledWidget.py with update_idletasks().

  - Changed name of PromptDialog component from *'entry'* to *'entryfield'*.

  28 April 1997

  - Version 0.3 released internally

  19 August 1997

  - Many changes made (see the version 0.4 porting guide for
    more details).

  - The option propagation mechanism that iwidgets uses is too
    cumbersome, too hard to understand and, in python, too slow. 
    Developed a new mechanism which is more explicit in naming
    options.  This resulted in most options which were simply
    propagated to components being removed.  Removed keep(), rename()
    and ignore() methods and "usual" options.

  - For speed, Pmw no longer queries the Tk option database for
    default values for megawidget options.  Hence, resource names and
    classes do not need to be supplied when creating options and
    *None* is returned for the resource name and class when using
    /configure()/ to query the options.  Option "types" no longer
    used.

  - Changed method and component names to be more consistent.

  - Replaced most uses of pack() with grid().

  - Megawidgets no longer inherit from LabeledWidget.  Instead they
    call createlabel() to optionally create the label component.

  - Removed child site from EntryField and rewrote ComboBox
    accordingly.

  - Wrote lots more documentation, including automatically generated
    reference manuals.

  - Removed PushButton and rewrote ButtonBox to directly create
    Tkinter.Buttons rather than PushButtons.

  - Added initialisation options - options which can be set at
    creation time but not later using configure().

  - Added aliases for components.

  - Modified the base classes so that during option configuration,
    components are configured 'before' configuration called functions
    are called.

  - Added several more megawidgets.

  - Added interface to BLT graph and vector commands.

  - Created PmwLazy module for lazy importing of Pmw - avoids loading
    megawidgets which are not used.

  - Added several more functions for handling color and fonts.

  - Replaced Counter and EntryField 'time' with 'timeN' and 'time24'

  - Pmw.initialise() will now create Tkinter.Tk if not given root.

  1 September 1997

  - Release of version 0.4

  5 September 1997

  - Modified the base classes so that the Tk option database resource
    class of megawidgets can be overridden in the call to the
    constructor using the *hull_class* option.

  - The separators in Pmw.PanedWidget are now active - they can be
    grabbed, like the handles, and moved around.  The cursor now
    changes to the correct left/right or up/down cursor when over a
    separator or handle.  (Clemens Hintze)

  - Fixed bug in MessageInfo demo Dismiss button.  If it is invoked,
    an error occurs saying "not enough arguments".  (Mark Colclough)

  9 September 1997

  - Added the *useTkOptionDb* argument to Pmw.initialise which
    specifies that the initial values of megawidget options are to be
    set by querying the Tk option database.

  - When used to query options, the configure() method now returns the
    resource class and name of the options.

  19 September 1997

  - Changed functions datestringtoint() and timestringtoint() to
    datestringtojdn() and timestringtoseconds().  Changed return value
    of datestringtojdn() to be Julian Day Numbers rather than seconds
    since the epoch.
    
  - Fixed a bug in the date Counter due to use of time.timezone, by
    replacing, when calculating date increments, calls to the time
    module with calls to datestringtojdn().

  - Added century pivot year (setyearpivot function) to Counter date
    datatypes to handle two-digit years.

  - Added date_dmy4, date_mdy4 and date_y4md datatypes to Counter.
    
  - Modified demos All.py and ScrolledText.py so that demos can be called
    from directories other than the demos directory.  (Case Roole and 
    Guido van Rossum)

  - Changed the default for the Pmw.Balloon 'label_justify' option to
    'left' to improve appearance of multi-line balloons.  Pmw.Balloon
    now replaces newlines with spaces in the statusHelp string so that
    the strings look better when displayed in a Pmw.MessageBar. 
    (Andreas Kostyrka)

  - Pmw.Blt now calls 'package require BLT' when checking for the
    existence of Blt, so that it can be loaded if it is not statically
    linked.  (Clemens Hintze, Matthias Klose)

  - Copied earthris.gif and flagup.bmp files from Tcl distribution to
    test directory, just in case they have not been installed. 
    (Jonathan Kelly)

  - Lots of improvements to the documentation and documenting recent
    changes.

  16 October 1997

  - Modified Pmw.Balloon and Pmw.ComboBox to work around a bug in the
    Windows95 version of Tk which caused the popup windows to appear
    in the wrong place.  (Fredrik Lundh and Jerome Gay)

  - Added Pmw.maxfontwidth() function. (Rob Pearson)

  24 October 1997

  - Changed PmwBase._reporterror to handle the class exceptions of
    python 1.5.  (Case Roole)

  29 October 1997

  - Fixed a bug in forwardmethods() function which occurred if the
    'toClass' class had a method called *type*.
    
  7 November 1997

  - Changed tests/Test._getErrorValue to handle the class exceptions of
    python 1.5.  (Michael McLay)

  - Changed bug fix in forwardmethods() function to use the
    /exec execString in d/ construct. (Guido van Rossum)

  - Can now use Pmw.MegaArchetype as a base class just to get option
    handling; it will not create the hull component unless requested. 
    Moved __str__() and interior() methods from Pmw.MegaToplevel and
    Pmw.MegaWidget to Pmw.MegaArchetype class.

  10 November 1997

  - Added 'textclass' option to Pmw.ScrolledText and 'listboxclass'
    option for Pmw.ScrolledListBox to allow embedding of custom
    widgets.

  - Added Mitch Chapman's *FontText* module to the /demos/ directory
    and used it to display the demo source code in color.

  - Added two notebook megawwidgets, Pmw.NoteBookR and Pmw.NoteBookS. 
    (Case Roole and Joe Saltiel)

  - Added Pmw.ScrolledCanvas megawidget. (Joe Saltiel)

  - Added Pmw.TreeBrowse megawidget. (Michael McLay)

  - Added Pmw.Group megawidget and modified to use /grid()/ instead
    of /pack()/. (Case Roole)

  - Release of version 0.5

  12 November 1997

  - Added 'pyclass' option to components and removed 'textclass'
    option from Pmw.ScrolledText and 'listboxclass' option from
    Pmw.ScrolledListBox.  (Suggested by Shen Wang)

  - Added label component to Pmw.ButtonBox megawidget.

  - Fixed mis-spelling of PmwTreeBrowse in Pmw.py.

  - Release of version 0.5.1

  5 December 1997

  - The pyclass option can now be None.  If so, createcomponent
    returns None.

  - Removed tagtype option from Pmw.Group.  Can now use the more
    general tag_pyclass instead.

  - Added tcl call to /load {} Blt/ when testing for presence of Blt.

  - Added julian and papal options to Pmw.ymdtojulian and
    Pmw.juliantoymd functions and made sure divisions give the same
    result as C even when operands are negative.

  - Exported ymdtojulian and juliantoymd functions.

  - Fixed bug in activate method.  Did not prepend TclError with Tkinter.

  - When the Blt busy hold command is called from showbusycursor, the
    bindtags on the busy window are set so that no events cause
    callbacks to occur for the toplevel or all bindings.  Also, while
    a busy window is up, the focus is changed to the busy window so
    that no keyboard events are accepted.  This fixes a bug where the
    Tkinter._nametowidget function could crash with a /KeyError: _Busy/
    if there was a binding on a toplevel window and the mouse
    was pressed while the busy cursor was up.

  9 December 1997

  - Fixed bug in Pmw.datestringtojdn() when dealing with century year,
    such as 2000.

  10 December 1997

  - Added 'where' option to /Pmw.ScrolledText.importfile()/.  (Graham
    Matthews)

  16 December 1997

  - Modified Pmw.RadioSelect and Pmw.ButtonBox so that you can no
    longer index their buttons using regular expressions.  This
    feature seemed to have little use and caused problems with buttons
    labeled for example 'a*' and 'b*'.  (Problem reported by Rob
    Hooft)

  - Added updateFunction option to Pmw.busycallback().  If set, the
    function will be called just after the command given to
    Pmw.busycallback().  If the function is set the Tkinter update()
    method, then this will clear any events that may have occurred
    while the command was executing.

  30 December 1997

  - Changed ymdtojulian and juliantoymd functions to jdntoymd and
    ymdtojdn, because the meaning of "julian" is ambiguous, whereas
    the meaning of "Julian Day Number" is not (maybe).

  - Converted Pmw to use python 1.5 package mechanism.  (Michael McLay
    and Case Roole)

  - Removed Pmw.py and PmwLazy files.  Added __init__.py, PmwLoader.py
    and Pmw.def files.  (Case Roole)

  - Applications can now specify at runtime which version of Pmw to
    use and also which alpha versions, if any.  (Case Roole)

  - Modified Pmw code for the version of Tkinter released with python
    1.5.

  - Release of version 0.6

  5 January 1998

  - Fixed alpha version handling so that alpha versions do not have to
    supply PmwBase.py and PmwUtils.py.  (Case Roole)

  - Added example alpha directory and documentation.  (Case Roole)

  7 January 1998

  - Added selectmode option to Pmw.RadioSelect megawidget.  (Roman
    Sulzhyk)

  - Added some changes to Pmw.ScrolledCanvas to get around some bugs. 
    (Joe Saltiel)

  - Release of version 0.6.1

  8 January 1998

  - Added some more changes to Pmw.ScrolledCanvas.  (from Joe Saltiel)

  12 January 1998

  - Added Pmw.OptionMenu megawidget. (Roman Sulzhyk)

  20 February 1998

  - Added new Pmw.MenuBar features to delete menus and menuitems,
    enable and disable menu bar and to add cascade menus.  (Rob Pearson)

  - Added extra arguments to Pmw.Color.spectrum for more control over
    color choice.

  23 February 1998

  - Added canvasbind() method to Pmw.Balloon.

  - Fixed demos/All.py so that it will correctly determine which Pmw
    version to use even if it is in a directory symlinked to the demos
    directory.
   
  - Removed "import DemoVersion" from all demos, except All.py, so
    that they will work unchanged when copied outside of the Pmw
    distribution.

  - Release of version 0.6.2

  26 February 1998

  - Fixed PmwLoader so that it works on Macintoshes.  (Jack Jansen)

  2 March 1998

  - Fixed PmwBase and PmwBlt so that an attempt is made to dynamically
    load Blt before it is used.  Previously only attempted to load Blt
    when calling showbusycursor.

  16 March 1998

  - Added hulldestroyed() method.

  - Modified displayerror() function to use value given to
    reporterrorstofile() if it is set.

  - Fixed bug in Pmw.EntryField which occurred when the 'command'
    option destroyed the megawidget.

  - Pmw.EntryField invoke method now passes on the value returned by
    the 'command' function.

  3 April 1998

  - Added Pmw.ScrolledFrame megawidget.  (Joe Saltiel)

  - Color.rgb2hsi() now uses the built-in /min()/ and /max()/ functions.

  20 April 1998

  - Moved time and date functions from PmwCounter.py to new file,
    PmwTimeFuncs.py.

  - Added optional 'separator' argument to /timestringtoseconds/ and
    /datestringtojdn/ functions.  These functions are now stricter
    when checking if a string is a valid date or time.  For example,
    it now checks for correct day in month, month in year, etc.  These
    changes also affect the Pmw.Counter date and time validators.

  - The /datestringtojdn/ function now accepts all combinations of
    *'d'*, *'m'*, *'y'* as format string.

  - Moved functions to bottom of file and class to top of file in
    PmwEntryField.py and PmwCounter.py.

  - The validation for Pmw.EntryField 'integer', 'hexadecimal' and
    'real' types now use string.atol or string.atof rather than
    regular expressions.

  - The validation for the Pmw.EntryField 'real' type accepts a
    'separator' argument, for those who prefer a comma instead of a
    full stop/period/point as the decimal dividing symbol.

  - The Pmw.EntryField 'time*' and 'date_*' validators have been
    removed.  The functionality can be replaced by using the new
    'time' and 'date' validators with 'min' and 'max' fields.

  - The Pmw.EntryField 'maxwidth' option has been removed.  The
    functionality can be replaced by using the 'max' field of the
    validator.

  - Added an 'extravalidators' option to Pmw.EntryField.  This allows
    new types of validation to be added, particularly in classes
    derived from Pmw.EntryField.  It also allows the use of different
    names for the same validation, by using aliases.  Added
    SpecialEntry demo to show 'extravalidators' option, based on work
    by Joachim Schmitz.

  - Fixed a bug in Pmw.EntryField when combining use of 'value' and
    'entry_textvariable' options.

  - The Pmw.EntryField 'validate' option now also accepts a dictionary
    to handle minimum and maximum validation and to allow the passing
    of other arguments to the validating functions, such as date, time
    and number formats and separators.

  - Fixed bug in Pmw.EntryField where the entry would scroll to the
    start of the text if an invalid character was typed.

  - Added checkentry() method to Pmw.EntryField, so that it can be
    updated if the entry widget is tied to a textvariable.

  10 May 1998

  - The activate() method now takes a geometry option to allow more
    flexible positioning of the modal dialog.

  - Fixed rarely occurring bug in deactivate() method if it is called
    (perhaps from a timer) during the call to wait_visibility() in the
    activate() method.  This bug used to generate an error and the
    application would not exit properly.

  - Fixed another rarely occurring bug in deactivate() method if it is
    called while another application has the grab.

  - Removed "sys.exc_traceback = None" for except clauses which used
    to be required by python 1.4 so that references to objects in the
    stack trace would not be left.

  - Now uses sys.exc_info() function when displaying exception
    traceback.

  - The *state* option of Pmw.Balloon and the *orient* option of
    several others now generate an exception if they have a bad value.

  - Added a deactivatecommand option to Pmw.MegaToplevel which can be
    used, for example, to cancel timers.

  - Made changes to Pmw.Counter so that the entry display continuously
    changes when arrow key presses are repeated quickly.

  - Made changes to Pmw.Counter so that the insertion cursor is maintained
    while counting and the entry scrolls to the end if the value is long.

  - Pmw.Counter now behaves correctly when counting past the maximum
    and minimum values of the EntryField.

  28 May 1998

  - Made all Pmw.EntryField standard validators publicly available
    as /Pmw.numericvalidator/, etc.

  - Now uses faster /string.replace()/ instead of /regsub.gsub()/ when
    applicable.

  - If the 'balloonHelp' argument of the Pmw.Balloon bind methods is
    *None*, no balloon is displayed.

  - Merged the code from the PmwUtils module (forwardmethods()) into
    PmwBase, since it was always used, was used nowhere else, and made
    freezing a little more complicated.

  - Added a short delay between calling Tkinter bell() method (sounds nicer).

  - The functions /datestringtojdn()/ and /timestringtoseconds()/ now
    return ValueError on invalid input.

  - Created bundlepmw.py, to help when freezing in Pmw.  Placed in bin
    directory.

  29 May 1998

  - Fixed rare bug in Pmw.Counter which occured if the counter was
    unmapped while the mouse button was held down over an arrow button.

  - Created contrib directory and placed PmwVerticalGuage.py in it. 
    (Chris Wright)

  - Patched PmwNoteBookR.py.  (Siggy Brentrup)

  - Added addoptions() method to Pmw.MegaArchetype class. (Dieter Maurer)

  - By default, MenuBar creates hotkeys for menus and menu items for
    keyboard traversal.  Added traversSpec argument to MenuBar add
    methods.  (Michael McLay)
  
  31 May 1998

  - Cleaned up bbox() methods in Pmw.ScrolledCanvas and
    Pmw.ScrolledListBox.

  - The createcomponent() method now disallows the creation of
    component names containing an underscore, since the query
    functions would not be able to find them.

  2 June 1998

  - Release of version 0.7

  3 June 1998

  - Moved Pmw.TreeBrowse megawidget to contrib directory.

  17 June 1998

  - Added PmwFullTimeCounter.py to contrib directory (Daniel Michelson)

  1 July 1998

  - Changed mispelt file PmwVerticalGuage.py to PmwVerticalGauge.py
    in contrib directory.

  7 July 1998

  - Fixed bug in Pmw.Counter real datatype.  Sometimes incorrectly
    counted negative decimal fractions.  (Reported by David Ascher)

  12 July 1998

  - The 'format' argument of Pmw.datestringtojdn() now defaults to
    *'ymd'*.

  - Removed Tkinter_test.py from tests since it does not test any Pmw
    functionality (only Tkinter) and it fails under MS-Windows 95.

  23 August 1998

  - Changed several exception types to be more consistent.

  - Made the interface to Pmw.Blt.Vector more like the builtin python
    list type.

  - It is no longer an error to call Pmw.setversion() or
    Pmw.setalphaversions() after initialisation, as long as the
    requested version matches the actual version.

  - Fixed Pmw.NoteBookR so that it behaves better when the
    highlightthickness is changed.

  - The setyearpivot() function now returns a tuple containing the old
    values of 'pivot' and 'century'.

  - Added PmwFileDialog.py to contrib directory (Rob Hooft)

  - Modified demos so that full tracebacks are displayed if an error
    occurs when importing a module.

  - Removed justify() method from Pmw.ScrolledListBox, since it is
    just a wrapper around the xview and yview methods of the listbox. 
    Also, it was not a permanent justification, as the name implied.

  20 September 1998

  - Changed implementation of Pmw.ScrolledCanvas.

  - Added *borderframe* option to Pmw.ScrolledText and Pmw.ScrolledCanvas.

  18 October 1998

  - Major overhaul of all scrolled widgets.  Modified all to use
    similar structure, given the peculiarities of each.  Fixed several
    subtle bugs.

  - Pmw.ScrolledFrame: now uses a frame positioned within a clipping
    frame using the place geometry manager.  Added borderframe,
    horizflex, horizfraction, usehullsize, vertflex, vertfraction
    options.  Added reposition() method.  Removed getFrame() method;
    use interior() method instead.

  - Pmw.ScrolledListBox: added usehullsize option.

  - Pmw.ScrolledText: added borderframe and usehullsize options.

  - Pmw.ScrolledCanvas:  simplified widget structure.  Added
    borderframe, canvasmargin, scrollmargin and usehullsize options. 
    Added label.

  - Modified Pmw.OptionMenu to use standard widgets rather than call
    tcl procedure.  Added *initialitem* option.  Now handles
    *menubutton_textvariable* component option correctly.

  1 November 1998

  - Documented more Pmw functions and Pmw.ComboBox.

  15 November 1998

  - Fixed some bugs, cleaned up code and wrote documentation for
    Pmw.Group.  Removed *ringpadx* and *ringpady* options, since this
    functionality is more generally available by padding the
    megawidget itself and by padding the children of the megawidget. 
    Modified Pmw.aligngrouptags so that it takes into account the
    borderwidth and highlightthickness of the ring and so that it
    works when there is no tag widget.  Added *tagindent* option.

  18 November 1998

  - Renamed canvasbind() and canvasunbind() methods of Pmw.Balloon to
    tagbind() and tagunbind() and modified so that they work with both
    Tkinter.Canvas items and Tkinter.Text tagged items.

  19 November 1998

  - Added havebltbusy() method to Pmw.Blt. (Robin Becker)

  21 November 1998

  - Modified contrib/PmwFileDialog.py so that when a file is selected
    with the mouse, the highlight (in the file list) persists and the
    file list does not scroll to the top. (Rob Hooft)

  - Modified Pmw.Balloon so that it can be bound to a tag associated
    with several Canvas or Text items.  (Magnus Kessler)

  21 November 1998

  - Cleaned up appearance and colors of Pmw.NoteBookR tabs.  (Georg
    Mischler)

  - Added *buttontype* option to Pmw.RadioSelect to support
    radiobuttons and checkbuttons.  (Georg Mischler)

  23 November 1998

  - Updated usage of /bind_class(tag)/ due to change in return value
    in Tkinter module in python 1.5.2.  (Magnus Kessler, Fredrik Lundh)

  - The default time displayed in Pmw.TimeCounter is now the current
    local time, not GMT as before.

  - The times displayed in the Counter demonstration are now the
    current local time, not GMT as before.

  7 December 1998

  - Modified Pmw.ComboBox to take advantage of the fix to the Tkinter
    /bind()/ method callback handling of /Event.widget/ in python
    1.5.2.  It works even if the *selectioncommand* destroys the
    combobox.  For simple comboboxes, the invoke() method now returns
    the return value of the *selectioncommand*.

  - Modified Pmw.EntryField to take advantage of the fix to the
    Tkinter /bind()/ method callback handling of /Event.widget/ in
    python 1.5.2.  It works even if a user-supplied callback
    (*command*, *invalidcommand*, *validator* or *stringtovalue*)
    destroys the entryfield.  Cleans up correctly when destroyed.  The
    invoke() method now returns the return value of the *command*.

  - The invoke() method of Pmw.TimeCounter now returns the return
    value of the *command*.

  - Modified Pmw.ButtonBox to use the new (in Tk8.0) *default* option
    of the Tkinter *Button* widget instead of a separate frame. 
    Changed default padding to be more compact.  Removed "ring" frame
    component and "ringborderwidth", "ringpadx" and "ringpady"
    options.  (Georg Mischler)

  - Changed *'pmw1'* fontScheme to set default fonts only when running
    under posix, since the default fonts on other systems look better.

  10 December 1998

  - Release of version 0.8

  20 January 1999

  - Added *master* option to Pmw.MegaToplevel and removed *master*
    argument from the activate method.

  - Replaced rand module in demos with a simple random number
    generator (since rand is not built-in on all versions of python).

  22 February 1999

  - Modified /__init__.py/ so that it only accepts directories whose
    names begin with *Pmw_M_N* and which have a /lib/PmwLoader.py/
    file.

  13 May 1999

  - Changed Pmw.ScrolledCanvas, Pmw.ScrolledText and Pmw.ScrolledListBox
    to speed up scrolling if the scrollmodes are not both dynamic.

  - Changed busy cursor and activate/deactivate code so that it works
    correctly under fast mouse clicking or fast keyboarding (using
    accelerators).  Also fixed so that grab is correctly restored
    after a Pmw.ComboBox popup list is unmapped inside a modal dialog. 
    (Clemens Hintze)

  - Several dialogs now give focus to one of their components (listbox
    or entry widget) when activated.  (Clemens Hintze)

  - Fixed Pmw.ComboBox so that it unposts popup if the combobox is
    unmapped and returns grab and focus correctly if destroyed.

  - Improved tracetk() output to be more readable.  Also displays
    nested calls to the Tk mainloop better and shows callbacks from
    tcl to python.

  - Upgraded Blt support to blt2.4i.  Graph widget is not backwards
    compatible with blt2.1.

  19 May 1999

  - Fixed bug in Pmw.Balloon in placement of balloons over canvas
    items when the canvas was scrolled. (Tessa Lau)

  20 May 1999

  - Added new Tk event types (new in Tk 8.0 and 8.0.5) to PmwBase
    error display method.  Also added check for unknown event types to
    safeguard against future changes.  (Magnus Kessler)

  - Added *exclude* argument to /showbusycursor()/.  (Rob Hooft)

  1 June 1999

  - Added wrappers for Blt Stripchart and Tabset widgets.  (Nick Belshaw)

  - Changed createcomponent() so that arguments to the constructor of
    the component can now be specified as either multiple trailing
    arguments to createcomponent() or as a single tuple argument.

  7 June 1999
        
  - Added call to update_idletasks() in Pmw.ScrolledCanvas,
    Pmw.ScrolledFrame, Pmw.ScrolledText and Pmw.ScrolledListBox to
    avoid endless mapping/unmapping of two dynamic scrollbars when the
    window is first mapped and only one scrollbar is needed.
    (Reported by Mark C Favas, solution suggested by Dieter Maurer.)

  10 June 1999
        
  - Fixed bug in bundlepmw.py when called with -noblt option. 
    (Reported by Kevin O'Connor)

  - Pmw.ComboBox now unposts the dropdown listbox before the selection
    callback is invoked, to avoid problems when the callback takes a
    long time to run.  (Reported by Randall Hopper)

  11 June 1999

  - Release of version 0.8.1

  29 June 1999

  - PmwMessageBar.message() now replaces newlines with spaces before
    displaying message.  Also applies to helpmessage().

  2 July 1999

  - Improved toplevel window positioning under NT, and stopped most of
    the ugly flashing.

  5 July 1999

  - The *pmw1* fontScheme is now supported under NT, as is the 'size'
    option to /Pmw.initialise()/.

  6 July 1999

  - Changed the names of positional arguments in the following
    methods, so that they have less chance of conflicting with keyword
    arguments:  MegaArchetype.createcomponent(), ButtonBox.insert(),
    ButtonBox.add(), MenuBar.addcascademenu(), MenuBar.addmenuitem()
    and RadioSelect.add().

  9 July 1999

  - Added images and example code to the megawidget reference manuals.
    (Suggested by Joerg Henrichs)

  - Fixed showbusycursor() under NT.  It now calls update() instead of
    update_idletasks() to force display of cursor.  (Solution
    suggested by George Howlett)

  - Improved display of arrows in ComboBox, Counter and TimeCounter.

  16 July 1999

  - Removed Pmw.maxfontwidth() function, since better functionality is
    now supplied by the Tk "font measure" command.

  - Removed Pmw.fontexists() function, since in Tk8.0 all fonts exist.

  28 July 1999

  - Fixed bug in date counter with separator other than *'/'* and time
    counter with separator other than *':'*.  (David M.  Cooke, Alan
    Robinson)

  - Under NT, the font named *'fixed'* is not fixed width, so added
    alias from *'Fixed'* to *'Courier'*.

  - Changed the /bind()/ and /tagbind()/ methods of Pmw.Balloon to
    remove a potential memory leak.  The methods now store the
    'funcids' of the callback functions, so that if the same widget or
    tag is bound twice, the balloon can remove the old bindings. 
    (Peter Stoehr)

  - Changed NoteBookR so that lowercmd, creatcmd and raisecmd are
    called in that order when a page is selected.  Also fixed bug
    which always raised page 0 when notebook is resized.  (Scott
    Evans, Charles Choi)

  1 August 1999

  - Added *dynamicGroups* argument to /defineoptions()/ method and
    modified ButtonBox, MenuBar, PanedWidget, RadioSelect to register
    their dynamic groups.

  - /Pmw.initialise()/ can now be called multiple times, with
    different 'root' arguments, but only sequentially.  Pmw does not
    (yet) support multiple simultaneous interpreters.  Modified
    Pmw.EntryField so that it recreates class bindings when
    Tkinter.root changes.

  4 August 1999

  - Added relmouse option to Pmw.Balloon.  Fixed Pmw.Balloon so that
    the balloon is not displayed off-screen.  (Tessa Lau)

  16 August 1999

  - Added disableKeyboardWhileBusy option to initialise().  To ignore
    keyboard input while displaying the busy cursor, Pmw sets the
    focus for each toplevel window to the Blt busy window.  However,
    under NT, this causes each window to be raised.  If this is not
    acceptable, programs running on NT can request show/hidebusycursor
    not to ignore keyboard input. 

  25 August 1999

  - Added Pmw.Blt.busy_forget() and used it in Pmw.hidebusycursor()
    when running under NT.  There is a bug in the Blt busy release
    command under NT where it sometimes fails to display the busy
    cursor.  Using busy forget avoids the problem.

  27 September 1999

  - Added busyCursorName option to Pmw.initialise() and added cursor
    argument to Pmw.Blt.busy_hold().  (Mark Favas)

  20 October 1999

  - Replaced Pmw.NoteBookR and Pmw.NoteBookS with completely rewritten
    Pmw.NoteBook.

  - Renamed Pmw.OptionMenu.get() to Pmw.OptionMenu.getcurselection()
    and Pmw.PanedWidget.remove() to Pmw.PanedWidget.delete(), to be
    more consistent with other megawidgets.

  - The index() method of several megawidgets now use Pmw.END,
    Pmw.SELECT and Pmw.DEFAULT instead of strings, since these may
    conflict with component names. 

  - Pmw.OptionMenu.index() now uses Pmw.SELECT to return
    index of the currently selected menu item, rather than None.

  - Added destroy() method to Pmw.MegaArchetype to handle cleaning up
    of _hullToMegaWidget mapping. 

  - Removed exclude argument from Pmw.showbusycursor() and added
    Pmw.excludefrombusycursor() function instead.  (Rob Hooft)

  - Fixed several bugs for Windows NT.

  - Added Pmw.ButtonBox.button() and Pmw.RadioSelect.button().

  - Added Pmw.Color.bordercolors().

  21 October 1999

  - Release of version 0.8.3. (Version 0.8.2 was not released.)

  30 October 1999

  - Added arrownavigation option and previouspage() and nextpage()
    methods to Pmw.NoteBook.  (Peter Funk)

  - Renamed the /setnaturalpagesize()/ method of Pmw.NoteBook to
    /setnaturalsize()/ to be consistent with Pmw.PanedWidget.

  - Changed Pmw.excludefrombusycursor() to Pmw.setbusycursorattributes().
    Removed busyCursorName option from Pmw.initialise() and added
    cursorName attribute to Pmw.setbusycursorattributes().

  - Added documentation source and build scripts to ftp site.

  6 November 1999

  - Fixed memory leaks when destroying megawidgets.  Added automatic
    check for memory leak to test script used by all tests. 
    Pmw.initialise() now uses a hook into Tkinter.Widget.destroy
    rather than Tkinter.Frame.destroy to handle the case of
    Pmw.NoteBook being destroyed (since the notebook hull is a canvas
    and not a frame).  Window manager delete protocol callbacks are
    now cleaned up.  Pmw.ScrolledListBox event bindings now do not
    leak.  (Reported by Jeff Weeks)

  - Removed key bindings for Pmw.ScrolledListBox except space and return keys.

  20 November 1999

  - Fixed bug in Pmw.Balloon when the canvas or text item that
    triggered the balloon is deleted before the balloon is displayed
    by the *initwait* timer.  (Magnus Kessler)

  - Added *'nograb'* to 'globalMode' option of /activate()/ method. (Rob Hooft)

  - Added __setitem__ method to Pmw.MegaArchetype, so that megawidget
    options can be now set using /megawidget['option'] = value/ style.
    (Oliver Gathmann)

  27 December 1999

  - Converted from /regex/ module to /re/ module, since /regex/ is not
    implemented for Jpython.  (Finn Bock)

  30 December 1999

  - Added /clear()/ method to Pmw.ScrolledListBox (suggested by Carson
    Fenimore).

  15 March 2000

  - Fixed problem in PmwBase when deleting windows that were created
    before Pmw was initialised (such as splash windows displayed while
    the application is coming up).  (Mark Favas)

  - Added splash window to Pmw demo.  (Mark Favas)

  30 April 2000

  - Added Pmw.MainMenuBar megawidget, which uses the menubar feature
    of Tk to provide platform specific menu bars.

  - Fixed Pmw.Counter and several other megawidgets so that certain
    *hull* constructor keywords, such as *hull_relief* and
    *hull_borderwidth*, are not overriden in the constructor.

  - Thanks to Peter Cashin for his help on how to unpack gzipped tar
    files on Microsoft Windows operating systems.

  - Added Pmw.HistoryText megawidget.  This can be used as the basis
    of an interactive text-based database query gui.  It maintains a
    history of each query and allows editing of prior queries.

  - Added references to the Pmw.Blt.Graph documentation by Bjørn Ove
    Thue and Hans Petter Langtangen.

  - Searched for and fixed memory leaks. There are no more known memory leaks.
  
    - For commands created by /bind/:  these are cleaned up by Tkinter
      when the widget is destroyed.  Pmw.Balloon, which repeatedly
      binds to the same widget (or item, using /tag_bind/), has been
      fixed by passing the old command into the call to /unbind/ or
      /tag_unbind/ which is cleaned up by Tkinter.

    - For commands created by /class_bind/:  most class bindings are
      only created once (per Tk interpreter) and so do not need to be
      cleaned up.  The exception is adding and deleting menus in
      Pmw.MenuBar.  This has now been fixed to clean up /class_bind/
      commands when deleting menus.

    - Callbacks given to command, xscrollcommand, yscrollcommand, etc
      options are cleaned up by Tkinter when the widget is destroyed. 
      Cases where Pmw repeatedly sets such options have now been fixed
      to clean up the old command before configuring the new one. 
      These are in /setitems/ in Pmw.OptionMenu and when modifying the
      scrollcommand options in several of the scrolled widgets.

    - Pmw now cleans up calbacks it registers with the
      WM_DELETE_WINDOW protocol for toplevel windows.

  - Added ManualTests.py to tests directory for tests which need to be
    run by hand.

  12 May 2000

  - Release of version 0.8.4.

  17 May 2000

  - Modified Pmw.Counter to deal with the presence (python up to
    1.5.2) or absence (python 1.6 and after) of an *L* at the end of
    the ascii representation of a long.  (Mark Favas)

  - Fixed bug in Pmw.ScrolledFrame when given invalid flex options. 
    (Stephen D Evans)

  23 January 2001

  - Moved Pmw home from www.dscpl.com.au to pmw.sourceforge.net.

  - Added pmw2 font scheme, since the font used for balloon text with
    pmw1 is too small on Linux.

  - Removed syntax coloring from code window in demos.  It did not
    look good and the pattern matching was not always correct.

  - Changed font size used for demos to 12 for Unix, since 14 looked
    too big under Linux.

  - Minor fixes to tests for Tk 8.3.

  8 February 2001

  - Release of version 0.8.5

  18 February 2001

  - Added xview() and yview() methods to Pmw.ScrolledFrame (suggested
    by Christer Fernstrom).

  - Made tktrace output more readable.

  - Added noBltBusy option to Pmw.initialise.

  - Fixed bug where combobox dropdown list could stay mapped after
    entryfield was unmapped.

  - Improved scrolling in scrolled frame.

  21 February 2001

  - Fixed tests for recent version of Blt graph (reported by
    Venkatesh Prasad Ranganath).

  - Fixed problem in Pmw.ScrolledFrame in python 1.5 - string.atof
    does not accept a number as argument, but it does in python 2.0.

  24 February 2001

  - Modified Pmw.OptionMenu documentation to specify that list
    elements must be strings (problem reported by Guy Middleton).

  - Fixed bug in Pmw.OptionMenu where the wrong item was displayed
    when an integer item in the menu was selected with the mouse (even
    though items should be strings).

  - Added work around to Pmw.ScrolledFrame for bug in Tk when
    retrieving value from scrollbars soon after creation.

  27 February 2001

  - Added HistoryText and MainMenuBar to bin/bundlepmw.py - accidently
    left out.

  13 April 2001

  - Changed default foreground (text) of Pmw.Balloown to black.  (Eric
    Pettersen)

  - Added default fontScheme to Pmw.initialise().

  - Added -fontscheme and -fontsize options to demo.

  - Added updatelayout() to Pmw.PanedWidget for use when dynamically
    adding and deleting panes.  (G Cash)

  - Added move() to Pmw.PanedWidget to move panes.  (G Cash)

  20 April 2001

  - Fixed bug in Pmw.Balloon where the balloon would reappear if the
    mouse button was pressed down inside a widget and then, while the
    mouse button was being held down, the mouse was moved outside of
    the widget and then moved back over the widget.

  - Fixed bug in Pmw.Balloon when destroying widgets while the balloon
    was up.  In this case, the balloon remained displayed even though
    the widget had been destroyed. (Reported by Stefan Schone.)

  - Fixed bug in Pmw.Balloon when destroying widgets during the
    initwait period.  In this case, an error occurred when the
    initwait timer went off when it tried to access the destroyed
    widget. (Reported by Stefan Schone.)

  - Fixed Pmw.Balloon so that unbinding withdraws the balloon if
    the widget being unbound is the widget which triggered the balloon.

  - Modified Pmw.Balloon so that when deleting a canvas or text item,
    /tagunbind()/ can be called which will withdraw the balloon if it
    was triggered by the item.  Unfortunately this can not be
    automated as for widgets since Tk does not support <Destroy>
    bindings on canvas or text items, so there is no way that
    Pmw.Balloon can be notified of the deletion of an item.

  - Updated tests for python 2.1.

  21 May 2001

  - Pmw.OptionMenu now defaults to taking focus (on <Tab> key).

  15 May 2002

  - Fixed bug in Pmw.Graph.element_closest() where element names
    should follow option arguments.  (Val Shkolnikov)

  5 June 2002

  - Added command option to Pmw.TimeCounter.

  - Finished all documentation.

  - Fixed bug in documentation creation script which, since python
    2.0, printed default values of real options (such as the
    horizfraction option of Pmw.ScrolledFrame) with too many digits
    (such as 0.050000000000000003).

  - Fixed bug in setgeometryanddeiconify for cygwin python (John
    Williams).

  4 July 2002

  - Added master option to /MegaToplevel.show()/

  - Improved /MegaToplevel.show()/ so that tkraise is not called
    unecessarily, thus avoiding 2 second delay under certain window
    managers (such as sawfish) in most circumstances.  There are still
    problems with the Enlightenment window manager.

  18 August 2002

  - Added columnheader, rowheader and rowcolumnheader components to
    Pmw.ScrolledText.  (Rob Pearson)

  - Added /getvalue()/ and /setvalue()/ methods to several megawidgets
    as a consistent way to set and get the user-modifiable state. 
    (Cimarron Taylor)

  - Made sub-classing simpler when no new options or components are
    being created.  A sub-class of a Pmw megawidget does not need to
    have an __init__() method.  If it does, it does not need to call
    defineoptions().  Also, initialiseoptions() no longer requires an
    argument (for backwards compatibility it may take an argument, but
    it is ignored).

  24 August 2002

  - Release of version 1.0

"""
