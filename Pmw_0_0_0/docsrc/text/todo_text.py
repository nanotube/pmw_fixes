text = """
This is a long list of suggestions and enhancements for Pmw.  If
you are interested in doing any of these, please let me
('gregm@iname.com') know.

*New Pmw megawidgets*

    - Multicolumn listbox.

      Useful features - smooth scrolling, embedded images, different
      fonts and colours, text correctly masked when it is longer than
      its column width, interactive resizing of columns.

      Probably should be implemented as canvas widget rather than by
      using multiple frames or multiple listboxes.  There would be a
      lot of work needed to position all the elements - you can't just
      pack or grid them.

    - File dialog.

    - Main window class (App class), with menu bar, information line
      with status boxes and an about box.  (See iwidgets' mainwindow
      class for example.) This should handle creation of multiple main
      windows, recycling of unused main windows and should exit if
      last open main window is closed.

    - Searchable text megawidget.

    - Tree browser.

    - Check out Doug Hellmann's contributed megawidgets at
      <http://www.mindspring.com/~doughellmann/Projects/PmwContribD> or
      <http://members.home.net/doughellmann/PmwContribD/>
      and integrate into Pmw.

*Changes to current megawidgets*

    MegaToplevel

	- Modify activate() geometry argument to allow window positioning
	  relative to the pointer, another window or the screen and
	  allow the centering of the window relative to the
	  positioning point or by a specified offset.  Also add the
	  ability to position the window so that the mouse is over a
	  particular widget in the toplevel.

	  Should handle all combinations of

	    # when (always/first)
	    # where (center/geometry/mouse)
	    # parent (screen/window)
	    #
	    # and None (don't position)

	  Check Tix4.1.0/library/DialogS.tcl center method for how to
	  center over another window

	  Check iwidget's shell.itk for code to center widget over
	  screen or another widget.

          See Pmw.Balloon code for how to position over pointer.

          Tcl code to center over another (parent) window:

            # # center client relative to master (default xoff, yoff = -1)
            # set geomaster [split [wm geometry $master] "x+"]
            # set geoclient [split [wm geometry $client] "x+"]
            #
            # if {$xoff == -1} {
            #   set xoff [expr (
            #     ([lindex $geomaster 0] - [lindex $geoclient 0]) / 2)]
            # }
            # set newxpos [expr [lindex $geomaster 2] + $xoff]
            #
            # if {$yoff == -1} {
            #   set yoff [expr (
            #     ([lindex $geomaster 1] - [lindex $geoclient 1]) / 2)]
            # }
            # set newypos [expr [lindex $geomaster 3] + $yoff]
            #
            # wm geometry $client +$newxpos+$newypos

          More tcl code to center dialog over another (parent) window:

            # (args: parent dlg)
            # # First, display the dialog offscreen to get dimensions.
            # set screenW [winfo screenwidth $parent]
            # set screenH [winfo screenheight $parent]
            # set w [expr $screenW + 1]
            # wm geometry $dlg +$w+0
            # update
            #
            # # Get relative center of parent. 
            # set w [winfo width $parent]
            # set h [winfo height $parent]
            # set w [expr $w/2]
            # set h [expr $h/2]
            #
            # # Get and add screen offset of parent.
            # set w [expr $w + [winfo rootx $parent]]
            # set h [expr $h + [winfo rooty $parent]]
            #
            # # Get dimensions of dialog.
            # set dlgW [winfo width $dlg]
            # set dlgH [winfo height $dlg]
            #
            # # Make adjustments for actual dimensions of dialog.
            # set w [expr $w - $dlgW / 2]
            # set h [expr $h - $dlgH / 2]
            #
            # # Let's keep the entire dialog onscreen at all times.
            # # Center in screen if things are awry.
            # set recenter 0
            # if { $w < 0 } { set recenter 1 }
            # if { $h < 0 } { set recenter 1 }
            # if { [expr $w + $dlgW] > $screenW } { set recenter 1 }
            # if { [expr $h + $dlgH] > $screenH } { set recenter 1 }
            # if { $recenter } {
            #   set w [expr ($screenW -$dlgW) / 2]
            #   set h [expr ($screenH - $dlgH) / 2]
            # }
            #
            # wm geometry $dlg +$w+$h

	- Add geometry argument to show() (same as activate() above).

    Dialog

	- Add label (header?) to Dialog class.  May not be necessary, or
	  too complicated.

    ButtonBox

        - When a horizontal ButtonBox is stretched, the left button
          stays anchored to the left edge and there is too much space
          between the last button and the right edge.

        - Add an option to either evenly space the buttons across the
          button box, or to keep them together and justify them to the
          left, right or center.  Check that deleting buttons works
          correctly.

    ComboBox

	- Remove arrowrelief option from ComboBox and do what counter
	  does:  gets value of arrow's relief just before sinking it,
	  then restores it later.

	- Change bindings: remove all bindings from arrow key and remove
	  arrow key from <tab> focus sequence; only implement these
	  bindings on the entry widget:

	    # Up    popup dropdown list, scroll up if already displayed
	    # Down  popup dropdown list, scroll down if already displayed
	    # Esc   popdown dropdown list, return entry to previous value
	    # Enter popdown dropdown list, execute current selection

	  Remove bindings from listbox and scrollbar(s), so that all
	  bindings are via the entry widget?

	- When entering keys when list is displayed, scroll list to
	  first entry beginning with entered keys.  If no match,
	  scroll list to top.

	- Remove many of the arrow bindings from Pmw.ComboBox - there
	  are just too many key bindings on the arrow button.  There
	  is no need for it to respond to keys such as the up/down
	  keys when the adjacent Entry widget already does so.  I
	  propose to remove all Pmw.ComboBox arrow button key bindings
	  except for <space>, which can be used to bring up the
	  dropdown list.  The Entry widget behaviour would remain
	  unchanged:  when it has focus, you can use the up/down keys
	  to go to the next/previous entries and then use <Return> to
	  invoke the selection command.

	  Alternatively, make the bindings the same as the MS-Windows
	  combobox. (Use the url entry field in Navigator or IE as an
	  example of MS-Windows behaviour).  These have been reported
	  to be:

	    - All mouse actions are exclusively triggered by the left
	      button.

	    - Right button displays "Direkthilfe" on my german system
	      ("Direct Help").  This is a floating button, that
	      triggers display of a tool tip like the |?| button that
	      appears next to the |x| at the right end of the title
	      bar of some native windows dialogs.

	    - The arrow is very slim (acutally flat:  width/height is
	      about 2/1)

	    - Entry and popup have the same color ("window color")

	    - The popup has a 1 pixel dark border, no spacing between
	      popup and scrollbar.

	    - If the box has the focus, the full entry is displayed in
	      "selected" style.

	    - If the box has the focus, up and left keys rotate items
	      up, down and right keys rotate items down, all with
	      immediate effect.

	    - If the box has the focus, keys a-z (not case sensitive)
	      rotate through the items with same first character, with
	      immediate effect.

	    - No separate focus for the arrowbutton

	    - Discussing how the combobox behaves with arrow keys when
	      it has the focus:  "The concept is almost identical to
	      what you already have, just gives more visual feedback. 
	      In your current implementation you allow to rotate
	      through the values with the up and down arrow keys,
	      showing the strings in the entryfield, and accepting the
	      values when the user presses the spacebar (hmmm, how can
	      I exit this without moving back to the original value
	      manually?).  On Windows, the choice is not shown in the
	      entryfield, but the popup opens when you press the up or
	      down arrow keys, as if you clicked on the arrowbutton,
	      and you then navigate the values in the listbox.  This
	      avoids the display of not finally selected values in the
	      entryfield and is a lot more obvious and less confusing. 
	      The current behaviour certainly confused me, which is
	      why I first proposed the changes to the moveup/down
	      methods." (Georg Mischler)

	  Also, check bindings on other megawidgets for consistency.

	- Modify Pmw.ComboBox so that the width of the entry widget is
          forced to be the same as the width of the dropdown listbox. 
          If the "width" option to the standard listbox is 0, Tk sets
          the requested width of the listbox to be just large enough
          to hold the widest element in the listbox.  Using this
          option, I can see that listbox.winfo_reqwidth() is changing
          as I insert items into an unmapped listbox.  The question
          is, how do I get notified of these events so that I can set
          the width of the entry?

          The problem is that the listbox is in another toplevel which
          has not yet been displayed, so I can't bind to <Configure>
          to determine its width.

          One suggestion is to override the insert and delete methods
          of the Listbox class.  The problem with this is what if the
          font changed, or the borderwidth, etc?  You would need to
          override and check many more methods.

    Counter

	- Add option for different increment/decrement behaviour.  For
	  example, assuming increment is 1:

	    1. Current behaviour - move to the next multiple of the
	       increment, eg:  1.0 -> 2.0, 1.234 -> 2.0

	    2. Add or subtract the increment to whatever is displayed,
	       eg:  1.0 -> 2.0, 1.234 -> 2.234

	    3. Move to the next multiple of the increment, offset by some value.
	       eg: (if offset is 0.5) 0.5 -> 1.5, 1.234 -> 1.5, 1.678 -> 2.5

	- Add wrap option (to wrap around at limits) (then don't need
	  time24 arg to *'time'* datatype).

	- Add a state option to disable Counter.

	- Add option to Counter to allow the buttons to be on the same
	  side, one on top of the other, like Tix, Itcl, Motif,
	  Windows 95, etc.  There should probably also be an option to
	  lay the current large buttons on the same side of the entry
	  field, next to each other.

	- Redo TimeCounter using vertical Counter, add limitcommand
	  option to Counter to allow overflow from seconds to minutes
	  to hours

    Arrowed megawidgets (Counter, ComboBox, TimeCounter)

	- Potential construction speed up if Canvas arrows are replaced 
	  by Label with Bitmap or BitmapImage.  The hard part would be
	  to make the bitmap change size depending on size of Label.

        - Pmw.drawarrow should draw arrows which look like Tk cascade
          menu arrows.

    EntryField

	- Can it be modified to change all entered characters to upper
          or lower case automatically?  Or first-upper or
          first-of-each-word-upper?

        - If the validity of the currently displayed text is ERROR,
          allow any changes, even those which result in invalid text. 
          This is useful when invalid data has been given to the
          *value* option and the user is trying to correct it.

    LabeledWidget

	- Add tix-style border.

    MenuBar

	- Maybe Pmw.MenuBar should also have (optional) balloon help
	  for menu items as well as menu buttons.  I am not sure
	  whether users would find this useful.

	- The status help hints do not appear when using F10/arrow
	  keys.

	- Look at the Tk8.0 menu demo and check the help bindings for
	  ideas, in particular, how can you get help when using
	  keyboard bindings.

	- Check the new menu features in Tk8.0 for creating "native"
	  menu bars and the special ".help" menu.

	- Add index() method.
	
	- Add a *'position'* option to addmenu and deletemenu methods. 
	  This option should accept an index number, a menuName or
	  *Pmw.END*.

	- Look at itcl menubar for ideas.

    Balloon

	- Positioning of the balloon with respect to the target
	  widget or canvas item: There are a number of ways that
	  Pmw.Balloon could be improved.  For example, currently the
	  the top left corner of the balloon is positioned relative to
	  the bottom left corner of the target, offset by the
	  [xy]offset options.  These options apply to all targets -
	  they can not be set differently for different targets.

	  To make it more configurable, the user should be able to
	  specify, for each target:

	    - the base position in the target relative to which the
	      balloon should be placed (n, s, e, w, nw, sw, ne, se, c)
	      (Currently sw)

	    - the x and y offsets (Default (20, 1))

	    - the position in the balloon that should be placed at the
	      offset position (n, s, e, w, nw, sw, ne, se, c)
	      (Currently nw)

	      Note, if this is anything other than nw,
	      update_idletasks() will need to be called to get the
	      size of the balloon before it is positioned - there is a
	      possibility that this may cause weird ugly flashing.

	    - whether either the base x or y position should be taken
	      relative to the current mouse position rather than as
	      one of the corners of the target.  This would be useful
	      for large targets, such as text widgets, or strange
	      shaped canvas items.  This could be specified using
	      special base positions, such as (nm, sm, em, wm).  For
	      example, for *'sm'*, the x base position is the mouse x
	      position and y base position is the bottom (south) edge
	      of the target.

	  The user should be able to specify global defaults for all
	  of these, as well as be able to override them for each
	  target.  The Pmw.Balloon options and their defaults could
	  be:

	    # basepoint   sw        # Position on target.
	    # anchor      nw        # Position on the balloon
	    # xoffset     20        # x distance between basepoint and anchor
	    # yoffset     1         # y distance between basepoint and anchor

	  To be able to override these, the bind() and tagbind()
	  methods would have to accept these as additional arguments. 
	  Each would default to None, in which case the default values
	  at the time the balloon is deiconified would be used.

	  I'm not sure about how to handle the case when the balloon
	  is configured to come up under the mouse.  When this happens
	  the balloon flashes on and off continuously.  This can
	  happen now if you set the yoffset to a negative number. 
	  Should the balloon widget detect this and do something about
	  it?

	- Add showballoon(x, y, text) method to Balloon and use in
	  balloon help for a listbox:

	  On 3 Dec, Michael Lackhoff wrote:

	  # And another question:
	  # Is it possible to create a balloon-help for the entries
	  # in the listbox?  Not all the information is in the
	  # listbox and it would be nice if a balloon help could
	  # give addtional information.

	  Rather than popup a balloon help window as the mouse moves
	  over items in the listbox, I think it would be better if it
	  pops up after you clicked on an item (or a short time
	  afterwards).  Pmw.Balloon displays the balloon help a short
	  time after the mouse enters a widget, so is not directly
	  usable in this case.  However, a method could be added to
	  Pmw.Balloon to request it to popup the balloon at a
	  particular x,y position.  This method could be called from
	  the listbox_focus method above.  Something like:

	    # def listbox_focus(self, event):
	    #     self.indexlist.component('listbox').focus_set()

	    #     text = self.indexlist.getcurselection()
	    #     # expand text to whatever you want:
	    #     text = 'This is ' + text
	    #     self.balloon.showballoon(x, y, text)

	  The Pmw.Balloon showballoon() method would have to set a
	  timer which sometime later calls another method which
	  displays the text.  You would also need to bind
	  <ButtonRelease-1> to a hideballoon() method which withdraws
	  the popup.

	- The balloon can be displayed off-screen if the window is
	  near the edge of the screen.  Add a fix so that the balloon
	  always stays on the screen (but does not popup under the
	  mouse, otherwise it will immediately pop down).

	- Add a fix so that the balloon does not disappear if the
	  mouse enters it.  Could do this by setting a short timer on
	  the Leave event before withdrawing the balloon and if there
	  is an Enter event on the balloon itself, do not withdraw it.

	- For tagged items in text widgets, the balloon is placed
	  relative to the character in the tagged item closest to the
	  mouse.  This is not consistent:  in the other cases
	  (including canvas), the balloon is placed relative to the
	  bottom left corner of the widget or canvas item.  This
	  should also be the case for text items.

	- Is the new (in Tk8) "<<MenuSelect>>" event useful for
	  balloon and/or status help.

    MessageBar

	- Finish logmessage functionality.

	- Add colours and fonts to MessageBar message types.  For
	  example, systemerror message types could have bold font on a
	  red background.

	- Add message logging history view (like the ddd debugger).

    NoteBook

	- Notebook should recalculate layout if the requested size of a tab
          changes (eg font size, text, etc).

        - The tabpos option should accept 's', 'e' and 'w' as well as 'n'.

	- Possible new options (borrowed from iwidgets):

            - *equaltabs*

                If set to true, causes horizontal tabs to be equal in
                in width and vertical tabs to equal in height.

                Specifies whether to force tabs to be  equal  sized  or
                not.  A  value of true means constrain tabs to be equal
                sized. A value of false allows each tab to  size  based
                on  the  text label size. The value may have any of the
                forms accepted by the  Tcl_GetBoolean,  such  as  true,
                false, 0, 1, yes, or no.

                For horizontally positioned tabs (tabpos is either s or
                n),  true  forces all tabs to be equal width (the width
                being equal to the longest label plus any  padX  speci-
                fied). Horizontal tabs are always equal in height.

                For vertically positioned tabs (tabpos is either  w  or
                e), true forces all tabs to be equal height (the height
                being equal to the height of the label with the largest
                font).  Vertically  oriented  tabs  are always equal in
                width.

                Could have a special value which sets equal sized and
                also forces tabs to completely fill notebook width
                (apparently like
                Windows).

            - *tabgap*

                Specifies the amount of pixel space  to  place  between
                each tab. Value may be any pixel offset value. In addi-
                tion, a special keyword overlap  can  be  used  as  the
                value to achieve a standard overlap of tabs. This value
                may have any of the forms acceptable to Tk_GetPixels.  

            - *raiseselect*

                Sets whether to raise selected tabs slightly (2 pixels).

                Specifes whether to slightly  raise  the  selected  tab
                from  the rest of the tabs. The selected tab is drawn 2
                pixels closer to the outside of  the  tabnotebook  than
                the  unselected  tabs.  A  value  of true says to raise
                selected tabs, a value of false turns this feature off.
                The  default  is  false.  The value may have any of the
                forms accepted by the  Tcl_GetBoolean,  such  as  true,
                false, 0, 1, yes, or no.

            - *bevelamount*

                Specifies pixel size of tab corners. 0 means no corners.

    OptionMenu

	- Should accept focus and obey up and down arrow keys.

    PanedWidget

	- Add index() method
	
	- Modify all methods so that they accept *Pmw.END* as a pane
	  identifier as well as an index or a name.

	- Check iwidgets pane and panedwindow classes.

    RadioSelect
    
	- Add insert() and delete() methods.
	
	- The index method should have *forInsert* argument.

        - Add Pmw.SELECT to index() method.  For single selectmode
          this returns an integer, for multiple selectmode this
          returns a list of integers.

    LogicalFont

	- Add boldFixed fonts,

        - Search for closest size font if no exact match.

	- Maybe replace with Tk8.0 font mechanism.

	- Can the Tk8.0 font measuring functionality be used in Pmw somehow?

    Scrolled widgets

	- Can some common scrolling methods be factored out, either as
	  a base class, "ScrolledMixin" mixin class or as helper functions? 
	  Candidate methods: constructor, destroy, interior, _hscrollMode,
          _vscrollMode, _configureScrollCommands, _scrollXNow, _scrollYNow,
          _scrollBothLater, _scrollBothNow, _toggleHorizScrollbar,
          _toggleVertScrollbar.

	- ScrolledField should have optional arrow buttons, so that it
          can still be scrolled even if the mouse does not have a
          middle button.

    Miscellaneous

	- Add a button to the Pmw "Stack trace window" which
	  optionally removes all grabs:

	    I normally interact with the "Stack trace window"
	    immediately, and dismiss it afterwards.  In many cases
	    where a bug appears like this, the rest of the application
	    is still functional (many of the problems appearing at
	    this stage of development of my application are unforeseen
	    exceptions communicating with a robot on the other end of
	    a socket, not affecting the GUI per se).  For that reason
	    I'd prefer if the "stack trace window" would push another
	    grab on the grab stack (if any grabs are active at the
	    moment the exception occurs).  Could the window have an
	    extra "Terminate application" option for this case?

	- need to handle component option queries in configure():

	  # foo = Pmw.AboutDialog(applicationname = 'abc XYZ')
	  # foo.component('message').configure('text')    - works
	  # foo.cget('message_text')                      - works
	  # foo.configure('message_text')                 - doesn't

	- Implement bindings (ComboBox, etc) via a dictionary lookup,
	  to allow people to invent new bindings, such as for
	  handicapped users.  (Suggested by Michael McLay)

	- Modify bundlepmw.py so that it checks Pmw.def to see that no
	  files have been missed.

	- Potential cheap speedup by adding this to each module, or
	  inside functions if it has a loop containing calls to
	  builtins:

	    # from __builtin__ import *

	- Look at how update_idletasks and after_* are used in Pmw -
	  are they consistent?  could it be improved?  What are the
	  problems of using these on other bits of an application
	  (such as when the size of the toplevel is being determined
	  for the window manager).

	- If lots of errors occur (such as in a fast time callback)
	  the error window may not appear, since Tk will wait until it
	  is idle - which may never occur.  The solution is to call
	  update_idletask when updating the error window, but only
	  after a short time has passed.  This will provide better
	  user response.  However, it may not be possible to do this
	  if some python interpretes (omppython, for example) do not
	  handle calls to update_idletasks at certain times.

	- In the Pmw FAQ, in the "Why don't Pmw megawidgets have a
	  *'state'* option?" section, it mentions several Pmw
	  megawidgets that can not be disabled.  Fix them.

	- Add RCSID version string to all files.

	- When raising exceptions use the third argument to raise:

	    # raise SimulationException, msg, sys.exc_info()[2]

	- When update_idletasks is called all pending changes are
	  flushed to the window system server.  However, it may take
	  some time for the server to display the changes.  If it is
	  required that the display be up-to-date, update_idletasks
	  should be followed by a call that blocks until processed by
	  the server and a reply received.  This may be useful in
	  Pmw.busycallback to ensure the busy cursor remains visible
	  until the display is actually modified.

	- There is a small bug which appears only with Tk8.0 (the bug
	  is not apparent with Tk4.2).  If a dialog is activated and
	  pops up directly over the cursor and the dialog has a
	  default button, then pressing the <strong>Return</strong>
	  key will not invoke the default button.  If you move the
	  mouse out of and then back into the dialog, pressing the
	  <strong>Return</strong> key will work.  This behaviour has
	  been noticed in Tcl-only programs, so it is probably a bug
	  in Tk.  (Tested on Solaris.)

	- Modify PmwBlt.py to use blt2.4 instead of blt8.0.unoff.
	  Nick Belshaw <nickb@earth.ox.ac.uk> is looking at wrapping
	  the new BLT StripChart and TabSet into Pmw.

	- Perhaps Pmw should have its own exception defined, like
	  TkInters's TclError, perhaps called PmwError.

	- This one is caused by a bug in the implementation of Tcl/Tk
	  for Microsoft Windows NT (and maybe other Microsoft
	  products).  Mouse release events can get lost if the
	  grab_set and grab_release commands are used and the mouse
	  goes outside of the window while the mouse button is down. 
	  This can occur while Pmw modal dialogs are active.  Below
	  is some Tkinter-only code which demonstrates the problem.
	  Maybe there is a work around.

	    # # Test script to demonstrate bug in Tk
	    # #implementation of grab under NT.
	    #                                 
	    # # Click on "Dialog" to bring up the modal
	    # # dialog window.  Then button down on the scale,
	    # # move the mouse outside the window,
	    # # then button up.  The scale slider will still
	    # # be sunken and clicks on the "OK" button
	    # # will be ineffective.
	    # 
	    # import Tkinter
	    # 
	    # def activate():
	    #     waitVar.set(0)
	    #     toplevel.deiconify()
	    #     toplevel.wait_visibility()
	    #     toplevel.grab_set()        # Problem here
	    #     toplevel.focus_set()
	    #     toplevel.wait_variable(waitVar)
	    # 
	    # def deactivate():
	    #     toplevel.withdraw()
	    #     toplevel.grab_release()    # and here
	    #     waitVar.set(1)
	    # 
	    # root = Tkinter.Tk()
	    # toplevel = Tkinter.Toplevel()
	    # waitVar = Tkinter.IntVar()
	    # toplevel.withdraw()
	    # scale = Tkinter.Scale(toplevel, orient='horizontal', length=200)
	    # scale.pack()
	    # button = Tkinter.Button(toplevel, text='OK', command=deactivate)
	    # button.pack()
	    # 
	    # button = Tkinter.Button(text='Dialog', command=activate)
	    # button.pack()
	    # button = Tkinter.Button(text='Exit', command=root.destroy)
	    # button.pack()
	    # 
	    # root.mainloop()

*Documentation*

    - Complete all doco.

    - Add short examples to all megawidget manual pages.

    - Check if time24 is documented in EntryField/Counter man page.

    - Add a comment to Blt.html doco that it also covers the blt busy
      command.

    - Document how to get Pmw working on a Mac, for example:

	- Unzip and untar

	    This depends on what you use to unpack the tar file.  If
	    you use (macgzip and) SunTar you have to tell it that files
	    with ".py" extensions are text files (in the
	    preferences/file type section).  If you use stuffit
	    expander:  this can be made to do the conversion
	    correctly, but it could be that this only works if you set
	    the .py extension correctly in Internet Config.

	    - Where do you untar Pmw?

	    - How do you get line terminators correct (carriage
	      return/line feed)?

	    - Is there any problem with file name case?  (mixed
	      upper/lower case)

	    - Is there any problem with file name length?

	    (Joseph Saltiel says:  It was the same type of operation
	    as in Windows/Unix.  Run a program that unzips it and
	    untars it.  It seems to get case and length right on its
	    own.)

	- Let python know where Pmw is

	    - If Pmw is in its own folder you will have to add the
	      parent of that folder to the sys paths in Edit
	      PythonPaths.  If it is in the Python home folder, you
	      do not need to do this.

	    - Make sure that the Pmw folder is called "Pmw" and not
	      something else.  Since Pmw is a package, python expects
	      to find a "Pmw" folder somewhere in sys.path.

	    (Joseph Saltiel says:  With the Python distribution on the
	    Mac there is an application called editPythonPrefs, when
	    you run it it gives you a list of a paths.  These paths
	    are similiar to the PYTHONPATH variable.  I just added the
	    path to Pmw at the bottom of this list.)

    - Error in Counter doco: add *'yyyy'* argument to *'date'* datatype:
      The *'date'* counter also accepts a *'yyyy'* argument.  If 0, the year
      field will be displayed with 2 digits, otherwise it will be
      displayed with 4 digits.  The default is 0.

    - Add this explanation to MessageBar doco (from email reply):

      Pmw.MessageBar can be used for both interactive help messages
      (when the mouse enters certain widgets) and also for other
      general messages.

      To perform the help function it is integrated with the Balloon
      help widget so that the programmer (or user) can choose either
      balloon help, message bar help, both or neither.

      The MessageBar supports a configurable number of message types. 
      The default types include *'state'*, *'help'*, *'usererror'* and
      *'systemerror'*.  The difference between these are the length of
      time they are displayed, the number of bells that are rung and
      the priority of the message.  For example, the *'help'* message
      type is lower in priority than the *'usererror'*, so that error
      messages will always be displayed in preference to help messages
      regardless of the order the messages are created in.  The
      *'state'* message type is lowest in priority but has no timeout,
      so it should contain messages describing the current state of
      the application, such as 'Waiting for
      database connection' or
      'Waiting for
      file to be unlocked'.  I generally set this to the
      empty string when the application is running normally.  By
      default the help messages (with message type *'help'*) time out
      after 5 seconds, so that if the cursor happens to be left over a
      widget, the application state will be redisplayed after a short
      time.

    - Document general ideas about building guis, eg:

      When I write gui applications, I usually defer creation of windows
      as much as possible - this means that the application starts up
      quickly because it usually only has to create the main window. 
      Whenever another window is required for the first time, it is
      created then.  When the user has finished with the window, the
      window is withdrawn, not deleted, so that next time it is required
      it much faster to come up.

      In summary - don't create a window until you need and
      don't destroy a window if you may want it again.

      The amount of memory required to keep the windows should not be
      very much - except for very long running programs where the user
      may create thousands of different windows.

    - Add class hierarchy diagram to documentation:

      # MegaArchetype
      #     MegaToplevel
      #        etc
      #     MegaWidget
      #        etc

    - Add to doco something like:  "Another way to extend a Pmw
      megawidget is to specify a non-default type for one of the
      components.  For example /text_pytype = FontText/."

    - Document pyclass and pyclass = None (options for null components
      are ignored; the only time this can be used is with the
      Group's tag component - all
      other's use the component widget in some way)

    - Doc: Pmw.Color.setscheme: this changes the initial colours of all
      widgets created after the call to this function.

    - Create index of all Pmw methods, functions, options, components.

    - Add description of how to run the Pmw demos without installing.

    - Add description of how to install Pmw.

    - Describe grid structure of megawidgets, so that it is possible
      to extend megawidgets by adding new widgets into the interior
      (hence avoiding a childsite in most megawidgets)

    - Document error display and difference between callback and
      binding error reports.

    - Document difference between *'Helvetica 12'* and *'Helvetica size: 12'*
      in logicalfont.

    - Add to howtouse, to describe using the option database to set
        options for a specific megawidget:

	# import Pmw
	# root = Pmw.initialise(useTkOptionDb = 1)
	# root.option_add('*entryfield24*Label.text', 'German')
	# e = Pmw.EntryField(hull_name = 'entryfield24', labelpos = 'w')
	# e.pack()
	# root.update()

    - Also document hull_name and hull_class.

    - Finish FAQ, ReleaseProcedure and StructuredText test.

    - Put html through gifwizard and html lint.

       # http://www.cen.uiuc.edu/cgi-bin/weblint
       # (eg: http://www.cre.canon.co.uk/~neilb/weblint/manpage.html)

    - Delete comments from source if they have been added to docs
      (should not have two copies of anything).

    - Add name and short description for each megawidget, even if rest
      of reference manual in incomplete.

    - Need to document non-standard initial values for component
      options, such as border in ButtonBox and Dialog's childsite.

    - Docs should have DEFAULT BINDINGS section (like iwidget combobox).

    - Promote home page:

       # http://www.geocities.com/homestead/promote.html
       # http://www.submit-it.com/subopt.htm, etc

    - Document font functions.

    - Create man pages as well as html (modify createmanuals to produce both).

    - Maybe something with html frames like: itcl2.2/html/index.html

    - Add to Pmw coding conventions:
    
	- Surround *=* with spaces when used with keyword parameters.

	- Multi-line function calls should have one keyword parameter
	  per line.

    - Add to starting.html a note that Pmw is a python "package" and add
      a pointer to python documentation on packages.

    - Document scrolled widget implementations, explaining why they
      are all slightly different (because the underlying widgets which
      are being scrolled have different behaviors).

    - Make copyright clearer. Maybe borrow python's?

*Demos*

    - Check for missing demos.

    - In all demos can move the three lines beginning with "Import Pmw
      from the sibling directory", to inside "if __name__" clause.
      Also, "sibling directory" is now incorrect.  Also, add note that
      this is only necessary when running demos without installing Pmw.

    - Change demo/All.py so that it displays the traceback if it
      cannot load or run a demo (easier for users to report errors).

    - Add option to demo/All.py:  "Display demos in separate window"
      to allow resizing of sub-demos

    - TimeCounter and Spectrum demos beep when they come up, using:

      # root.option_add('*EntryField*value', 'VALUE')

    - In demos, add /title = 'blah'/ to top of file and replace
      /root.title(..)/ with /root.title(title)/ at bottom.

    - Add comprehensive speed test demo which creates one or more of
      each (common) megawidget.  Remove old SpeedTest demo.

    - Check demos work when called from ptui.  (Changes have to do
      with calling compile/exec where __name__ is not the name of the
      All.py script, but is *'__builtin__'*)

    - PromptDialog demo should not remember password.

    - Finish Counter, Radioselect demos.

    - Modify the All demo so that you can reload a demo module.

    - The syntax-coloured code viewer looks strange on Microsoft NT,
      because the size of the fonts differ.  Check out Guido's
      idle-0.1 text colouring for Pmw code viewer.

    - Document restrictions on adding bindings to a megawidget:  you
      probably need to bind to components of the megawidget and also
      check that you are not destroying bindings set up by the
      megawidget itself.

    - Add a demo that demonstrates setting the color scheme at run time.

*Tests*

    - Check for missing tests, such as TimeCounter, RadioSelect,
      SelectionDialog, MessageBar, MenuBar, ComboBoxDialog, Balloon.

    - Create test for useTkOptionDb option to Pmw.initialise().

    - Check that destroyed widgets' python classes are garbage
      collected (add test and/or demo).

    - Add tests for changecolor, setscheme, etc.

    - Need Resources test.

    - Create tests for deriving from Pmw classes (eg ComboBox).

*Ideas*

    - Add more Tix (www.xpi.com/tix/screenshot.html) and iwidgets widgets.

    - Look at spinner.itk for how to do vertical orientation on
      same side for Counter.

    - Investigate these new features in Tk8.0 and see if they could be
      used in Pmw:

      # embedded images in text widgets
      # destroy command ignores windows that don't exist
"""
