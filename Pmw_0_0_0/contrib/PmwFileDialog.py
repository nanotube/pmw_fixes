#
__version__ = '$Id: PmwFileDialog.py,v 1.1 2001/01/23 12:06:27 gregm Exp $'
#
# Filename dialogs using Pmw
#
# (C) Rob W.W. Hooft, Nonius BV, 1998
#
# No Guarantees. Distribute Freely. 
# Please send bug-fixes/patches/features to <r.hooft@euromail.com>
#
import os,fnmatch
import Tkinter,Pmw

class PmwFileDialog(Pmw.Dialog):
    """File Dialog using Pmw"""
    def __init__(self, parent = None, **kw):
        # Define the megawidget options.
        optiondefs = (
            ('filter',    '*',              self.newfilter),
            ('directory', os.getcwd(),      self.newdir),
            ('filename',  '',               self.newfilename),
            ('historylen',10,               None),
            ('command',   None,             None),
            )
        self.defineoptions(kw, optiondefs)
        # Initialise base class (after defining options).
        Pmw.Dialog.__init__(self, parent)

        self.withdraw()

        # Create the components.
        interior = self.interior()

        dn = self.createcomponent(
            'dirname',
            (), None,
            Pmw.ComboBox, (interior,),
            entryfield_value=self['directory'],
            entryfield_entry_width=40,
            selectioncommand=self.setdir,
            labelpos='w',
            label_text='Directory:')
        dn.grid(row=0,column=0,columnspan=2,padx=3,pady=3)
        del dn

        # Create the directory list component.
        dnb = self.createcomponent(
            'dirnamebox',
            (), None,
            Pmw.ScrolledListBox, (interior,),
            label_text='directories',
            labelpos='n',
            hscrollmode='none',
            dblclickcommand=self.selectdir)
        dnb.grid(row=1,column=0,sticky='news',padx=3,pady=3)
        del dnb

        # Create the filename list component.
        fnb = self.createcomponent(
            'filenamebox',
            (), None,
            Pmw.ScrolledListBox, (interior,),
            label_text='files',
            labelpos='n',
            hscrollmode='none',
            selectioncommand=self.singleselectfile,
            dblclickcommand=self.selectfile)
        fnb.grid(row=1,column=1,sticky='news',padx=3,pady=3)
        del fnb

        # Create the filter entry
        ft = self.createcomponent(
            'filter',
            (), None,
            Pmw.ComboBox, (interior,),
            entryfield_value=self['filter'],
            entryfield_entry_width=40,
            selectioncommand=self.setfilter,
            labelpos='w',
            label_text='Filter:')
        ft.grid(row=2,column=0,columnspan=2,padx=3,pady=3)
        del ft

        # Create the filename entry
        fn = self.createcomponent(
            'filename',
            (), None,
            Pmw.ComboBox, (interior,),
            entryfield_value=self['filename'],
            entryfield_entry_width=40,
            selectioncommand=self.setfilename,
            labelpos='w',
            label_text='Filename:')
        fn.grid(row=3,column=0,columnspan=2,padx=3,pady=3)
        fn.bind('<Return>',self.okbutton)
        del fn

        # Buttonbox already exists
        bb=self.component('buttonbox')
        bb.add('OK',command=self.okbutton)
        bb.add('Cancel',command=self.cancelbutton)
        del bb

        Pmw.alignlabels([self.component('filename'),
                         self.component('filter'),
                         self.component('dirname')])

    def okbutton(self):
        """OK action: user thinks he has input valid data and wants to
           proceed. This is also called by <Return> in the filename entry"""
        fn=self.component('filename').get()
        self.setfilename(fn)
        if self.validate(fn):
            self.canceled=0
            self.deactivate()

    def cancelbutton(self):
        """Cancel the operation"""
        self.canceled=1
        self.deactivate()

    def tidy(self,w,v):
        """Insert text v into the entry and at the top of the list of 
           the combobox w, remove duplicates"""
        if not v:
            return
        entry=w.component('entry')
        entry.delete(0,'end')
        entry.insert(0,v)
        list=w.component('scrolledlist')
        list.insert(0,v)
        index=1
        while index<list.index('end'):
            k=list.get(index)
            if k==v or index>self['historylen']:
                list.delete(index)
            else:
                index=index+1

    def setfilename(self,value):
        if not value:
            return
        value=os.path.join(self['directory'],value)
        dir,fil=os.path.split(value)
        self.configure(directory=dir,filename=value)
        c=self['command']
        if callable(c):
            c()

    def newfilename(self):
        """Make sure a newly set filename makes it into the combobox list"""
        self.tidy(self.component('filename'),self['filename'])
        
    def setfilter(self,value):
        self.configure(filter=value)

    def newfilter(self):
        """Make sure a newly set filter makes it into the combobox list"""
        self.tidy(self.component('filter'),self['filter'])
        self.fillit()

    def setdir(self,value):
        self.configure(directory=value)

    def newdir(self):
        """Make sure a newly set dirname makes it into the combobox list"""
        self.tidy(self.component('dirname'),self['directory'])
        self.fillit()

    def singleselectfile(self):
        """Single click in file listbox. Move file to "filename" combobox"""
        cs=self.component('filenamebox').curselection()
        if cs!=():
            value=self.component('filenamebox').get(cs)
	    self.setfilename(value)

    def selectfile(self):
        """Take the selected file from the filename, normalize it, and OK"""
        value=self.component('filename').get()
        self.setfilename(value) 
        if value: 
            self.okbutton()

    def selectdir(self):
        """Take selected directory from the dirnamebox into the dirname"""
        cs=self.component('dirnamebox').curselection()
        if cs!=():
            value=self.component('dirnamebox').get(cs)
            dir=self['directory']
            if not dir:
                dir=os.getcwd()
            if value:
                if value=='..':
                    dir=os.path.split(dir)[0]
                else:
                    dir=os.path.join(dir,value)
            self.configure(directory=dir)
            self.fillit()

    def askfilename(self,directory=None,filter=None):
        """The actual client function. Activates the dialog, and
           returns only after a valid filename has been entered 
           (return value is that filename) or when canceled (return 
           value is None)"""
        if directory!=None:
            self.configure(directory=directory)
        if filter!=None:
            self.configure(filter=filter)
        self.fillit()
        self.activate()
        if self.canceled:
            return None
        else:
            return self.component('filename').get()
        
    lastdir=""
    lastfilter=None
    def fillit(self):
        """Get the directory list and show it in the two listboxes"""
        # Do not run unnecesarily 
        if self.lastdir==self['directory'] and self.lastfilter==self['filter']: 
            return 
        self.lastdir=self['directory'] 
        self.lastfilter=self['filter'] 
        dir=self['directory']
        if not dir:
            dir=os.getcwd()
        dirs=['..']
        files=[]
        fl=os.listdir(dir)
        fl.sort()
        for f in fl:
            if os.path.isdir(os.path.join(dir,f)):
                dirs.append(f)
            else:
                filter=self['filter']
                if not filter:
                    filter='*'
                if fnmatch.fnmatch(f,filter):
                    files.append(f)
        self.component('filenamebox').setlist(files)
        self.component('dirnamebox').setlist(dirs)
    
    def validate(self,filename):
        """Validation function. Should return 1 if the filename is valid, 
           0 if invalid. May pop up dialogs to tell user why. Especially 
           suited to subclasses: i.e. only return 1 if the file does/doesn't 
           exist"""
        return 1

if __name__=="__main__":
    root=Tkinter.Tk()
    root.withdraw()
    Pmw.initialise()
    f=PmwFileDialog(root)
    f.title('File name dialog')
    while 1:
        n=f.askfilename(filter='*')
        if n==None:
            break
        print "Filename : ",repr(n)
