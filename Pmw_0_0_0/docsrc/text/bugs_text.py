text = """
This is a list of some of the known bugs in Pmw.  If you fix any of
these, please let me ('gregm@iname.com') know.

    - On NT, Pmw.MenuBar does not display message bar help for menu
      items.  It seems that Tk menu widgets do not support <Motion>
      events on MS.  This probably is an issue that should be taken up
      with the Tcl/Tk people.  (Reported by Stefan Schone.  Pmw.0.7)

    - Run the CounterDialog.py demo, select the show dialog button and
      press ok.  Now exit the dialog (either with the exit button or
      the close box).  The following error appears:

	# Menu ID 256 is already in use!Fatal Python Error: Tcl/Tk panic

      This may be a problem with Mac version of Tk.  (Reported by
      Anthony Wilson.)

    - Pmw.Balloons bind to widgets and canvas items.  This means that
      bindings made by other users are deleted when the balloon makes
      its bindings.

      The obvious solution is for Pmw.Balloon to add its bindings with
      a '+'.  But this would make the unbind and tagunbind methods
      inconsistent - they would remove all bindings, not just the ones
      added by the balloon.  A better way would be for the balloon to
      add a bindtag to each widget`s bindtag list - then it would not
      upset any other bindings and it could be deleted cleanly. 
      (Reported by Joe Saltiel)

	# import Tkinter
	# import Pmw
	# 
	# def foo(event):
	#     print '<Enter> event on text'
	# 
	# root = Pmw.initialise()
	# balloon = Pmw.Balloon()
	# 
	# canvas = Tkinter.Canvas()
	# canvas.pack()
	# 
	# text1 = canvas.create_text(50, 50, text = 'hello\nthere')
	# 
	# # As is, the balloon does not appear over the text, but foo
	# # is called.  Swap the following two lines and the balloon
	# # appears but foo will not be called.
	# canvas.tag_bind(text1, "<Enter>", foo)
	# balloon.tagbind(canvas, text1, 'text 1 help')
	# 
	# root.mainloop()

    - When a Pmw.Balloon is bound to a canvas item, moving the item
      becomes very slow.  (Reported by Joe Saltiel)

	# > Second, after I fixed my ordering problem I noticed, there
	# > is a pretty big delay in updating widgets that have balloon
	# > messages bound to them.  (For example dragging a box across
	# > a screen, the box has a delayed reaction.) I believe this is
	# > due to some of the timing functions used in PmwBalloon, I am
	# > not sure if there is a way around it.  I set all timers to
	# > zero, and still had the problem.

    - When running Pmw demos under ptui the busy cursor does not
      appear.

    - If a combobox has a horizontal scrollbar and it displays its
      listbox above the entry, then it is misplaced.

    - Bug in Pmw.PanedWidget:  repeat by creating new panes in Demo -
      existing panes jump to the right 1 or 2 pixels.

    - Bug in Pmw.PanedWidget:  repeat by setting hull_borderwidth to
      20 in demo - initial drag jumps to right by about 20 pixels. 
      Also right hand side border is missing.  (Fix may be similar to
      method used in Pmw.ScrolledFrame to give canvas border.)

    - Bug in Pmw.Balloon:  the following script demonstrates two bugs. 
      Firstly, if the mouse is moved into the button so that the
      balloon window appears before the toplevel is destroyed, then
      the balloon window will be stuck on the screen.  Secondly, if
      the mouse is moved in and out of the button so that the balloon
      window does not have time to appear (may need to increase the
      iniwait option to do this reliably), then an error occurs - see
      below.  (Reported by Stefan Schone.)
      
      Solution:  Balloon should bind to <Destroy> as well as <Leave> (but
      Tkinter gets an error in nametowidget!).  Perhaps the timer callback
      should check that the widget still exists.

	# import Pmw
	# import Tkinter
	# Pmw.initialise()
	# balloon = Pmw.Balloon()
	# top = Tkinter.Toplevel()
	# button= Tkinter.Button(top, text = 'My button')
	# button.pack()
	# balloon.bind(button, 'Help!')
	# balloon.after(5000, top.destroy)
	# top.mainloop()
	# # Now quickly move the mouse into the button, so that the balloon 
	# # window appears before the toplevel is destroyed.

      The error raised by the second bug is:

	# Error: 1
	# TclError Exception in Tk callback
	#   Function: <function callit at 311540> (type: <type 'function'>)
	#   Args: ()
	# Traceback (innermost last):
	#   File "/home/nmsse/workareas/INMS_TEST_AREA/python/imported/lib/1.5/Pmw/Pmw_0_7/lib/PmwBase.py", line 1349, in __call__
	#     None
	#   File "Tkinter.py", line 222, in callit
	#     apply(func, args)
	#   File "/home/nmsse/workareas/INMS_TEST_AREA/python/imported/lib/1.5/Pmw/Pmw_0_7/lib/PmwBalloon.py", line 133, in <lambda>
	#     None
	#   File "/home/nmsse/workareas/INMS_TEST_AREA/python/imported/lib/1.5/Pmw/Pmw_0_7/lib/PmwBalloon.py", line 154, in _showBalloon
	#     None
	#   File "Tkinter.py", line 380, in winfo_rootx
	#     return self.tk.getint(
	# TclError: bad window path name ".2318176.2320688"

    - Bug in Pmw.Balloon:  if a balloon is currently being displayed
      for a canvas item and that item is deleted (by a timer
      callback), then the balloon is not withdrawn (until another
      binding for the balloon is triggered).  Finish attempt at
      solving this problem using /self._currentTrigger/ in
      Pmw.Balloon (currently commented out).

    - Fix ButtonRelease events so they do not trigger without a
      corresponding ButtonPress event.

      From Joe Saltiel:  I was playing around with a scrolledlistbox
      and tkFileDialog.  When I have the dialog open above the list
      box and I doubleclick on it, I invoke the selectioncmd of the
      listbox as well as the tkFileDialog box, should this be
      happening?

      Attached is small sample program you can try.  To get the bug to
      show you must do two things.  First, when you open the file
      dialog box, make sure the item you are going to select if
      over(above) the scrolledlistbox.  Second, you have to double
      click on that item.  If you single click and hit "Open" you do
      not get the bug.  Nor do you get it unless the file you click on
      is directly over the clickable region of the scrolledlist box.

	  # import Tkinter
	  # import Pmw
	  # import tkFileDialog
	  # import string 
	  # 
	  # def askOpen():
	  #     file = tkFileDialog.askopenfile(filetypes=[("all files", "*")])  
	  #     print file
	  # 
	  # def printMe():
	  #     print "Me"
	  # 
	  # root = Tkinter.Tk()
	  # Pmw.initialise(root)
	  # 
	  # frame1 = Tkinter.Frame(root)
	  # lst = string.split("abc def ghi jkl mno pqr stu vwx yz")
	  # lstbox = Pmw.ScrolledListBox(frame1, items=lst, selectioncommand=printMe)
	  # lstbox.grid(row=0, column=0, columnspan=2)
	  # Tkinter.Button(frame1, text='open', command=askOpen).grid(row=1, column=0)
	  # Tkinter.Button(frame1, text='exit', command=root.destroy).grid(row=1, column=1)
	  # frame1.pack()
	  # 
	  # root.mainloop()

      Response:  I have found where the problem is but I am not sure
      how to fix it.  It appears that the tkFileDialog box closes on a
      ButtonPress event.  The corresponding ButtonRelease event is
      then sent to whichever widget is under the cursor at the time of
      the Release.  I have reproduced the problem with a Tcl-only
      script:

	  # listbox .l
	  # .l insert 0 1 2 3 4
	  # bind .l <ButtonRelease-1> {puts AAAGGHHH!}
	  #
	  # button .b -text open -command tk_getOpenFile
	  # pack .l .b

      If you do a quick Press-Release-Press over the file dialog, it
      is withdrawn.  If you then keep the mouse button down and move
      the mouse around, you will see that the button and the listbox
      still respond to it.  If you do the final button Release over
      the listbox, its <ButtonRelease-1> binding is invoked.
	  
      I think the correct solution is to modify Pmw to be very careful
      when to accept ButtonRelease events.  It will need to also bind
      to ButtonPress events and make sure that it gets a Press before
      it accepts the Release.  I'll try to do the change as soon as
      possible, but the code involved is fairly complex so I it may
      take a little time.

    - Investigate bug in Tk8.0:  When a dialog pops up over the
      pointer then the keyboard focus is not set and so <Return> does
      not invoke default button.

    - Under both X and NT, the arrows in the timecounter, counter and
      combobox do not match the scrollbar arrows.

    - Pmw.Group does not work correctly when the tag is a compound
      widget.  The tag is placed such that the top of the tag is cut
      off.  (Reported by Peter Stoehr.)

        # import Tkinter
        # import Pmw
        # 
        # root = Tkinter.Tk()
        # Pmw.initialise(root, fontScheme = 'pmw1')
        # exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
        # exitButton.pack(side = 'bottom')
        # 
        # def makeGroup(tagClassName):
        #     tagClass = eval(tagClassName)
        #     group = Pmw.Group(
        #         tag_pyclass = tagClass,
        #         hull_background = 'red',
        #         groupchildsite_background = 'blue',
        #     )
        #     group.pack(fill = 'both', expand = 1, padx = 6, pady = 6)
        #     child = Tkinter.Label(group.interior(),
        #         text = 'Group with tag ' + tagClassName,
        #         background = 'aliceblue',
        #     )
        #     child.pack(padx = 10, pady = 5, expand = 1, fill = 'both')
        #
        #     return group
        # 
        # grp1 = makeGroup('Pmw.EntryField')
        # grp2 = makeGroup('Pmw.ComboBox')
        # grp3 = makeGroup('Tkinter.Entry')
        # 
        # root.mainloop()

      Also, Pmw.Group does not resize correctly if the simple widget
      changes size.  For example:

      	# grp3.configure(tag_font = ('Helveltica', '-160'))

    - Bug(s) in PmwScrolledCanvas.  There is a bug in 0.8.1
      PmwScrolledCanvas._setRegion.  If there are no objects in the
      canvas, then error occurs on len(region) because region is None. 
      Below is an attempt to fix it.  Click on Show, then on Delete. 
      The window then continuously resizes.  If the ScrolledCanvas is
      created with canvasmargin = 0, the problem goes away.  (Reported
      by Anders Henja.)

      # import Tkinter
      # import Pmw
      # 
      # def _setRegion(self):
      #     # Attempt to fix PmwScrolledCanvas._setRegion.
      #     self.setregionTimer = None
      # 
      #     region = self._canvas.bbox('all')
      #     canvasmargin = self['canvasmargin']
      #     if region is None:
      #         region = (0, 0, 0, 0)
      #     region = (region[0] - canvasmargin, region[1] - canvasmargin,
      #         region[2] + canvasmargin, region[3] + canvasmargin)
      #     self._canvas.configure(scrollregion = region)
      # 
      # def show():
      #     canvas.component('canvas').delete('all')
      #     canvas.create_oval(0, 0, 800, 600, fill = 'red')
      #     canvas.configure(canvas_width = 600, canvas_height = 450)
      #     canvas.resizescrollregion()
      # 
      # def delete():
      #     canvas.component('canvas').delete('all')
      #     canvas.configure(canvas_width = 0, canvas_height = 0)
      #     canvas.resizescrollregion()
      # 
      # root=Tkinter.Tk()
      # Pmw.initialise(root)
      # 
      # buttonbox=Pmw.ButtonBox()
      # buttonbox.pack(fill='x',side='bottom',padx=5,pady=5)
      # buttonbox.add('Show',command=show)
      # buttonbox.add('Delete',command=delete)
      # buttonbox.alignbuttons()
      # 
      # canvas=Pmw.ScrolledCanvas(canvasmargin=2)
      # canvas.__class__._setRegion = _setRegion
      # canvas.pack(fill='both',side='right',expand=1)
      # 
      # root.mainloop()

    - Bug in Pmw.Dialog:  if *defaultbutton* is configured before
      *buttons* during *self.initialiseoptions()* (that is if
      *self._constructorKeywords.keys()* returns a different order),
      then *setdefault()* fails.

    - Bugs in Tk which affect Pmw.MainMenuBar:
    
        - Extra bindings assigned to a Tkinter.Menu widget using
          bindtags have no effect.  Hence the method used in
          Pmw.MenuBar for status help (bind_class followed by
          bindtags) does not work and therefore binding to the menu
          widget is used instead.

        - The *'active'* tag for the /index()/ method of Tkinter.Menu
          always returns *None*.  Hence, in the menu widget motion
          binding, /event.y/ and the *'@'* format is used instead, for
          all menus except the toplevel main menu.

        - For the toplevel main menu, /event.x/ must be used for the
          /index()/ method, but it returns the wrong index.  It
          appears that the Tk widget is assuming vertical layout
          to calculate distances, rather than horizontal.

        - For toplevel main menus, several Tk commands, such as
          /winfo_height()/, do not work.  This prevents the use of
          balloon help for Pmw.MainMenuBar.

"""
