complete = 1
reviewdate = "30 October 1999"

name = """
    a set of tabbed pages
"""

description = """
    A notebook contains a set of tabbed pages.  At any one time only
    one of these pages (the 'selected' page) is visible, with the
    other pages being hidden "beneath" it.  Another page in the
    notebook may be displayed by clicking on the tab attached to the
    page.  The tabs are displayed along the top edge.

    Optionally, the notebook may be displayed without tabs.  In this
    case, another selection widget, such as ~OptionMenu~, may be used
    to select the pages.

    This megawidget is derived from ~MegaArchetype~ (not ~MegaWidget~
    like most other megawidgets), with the hull class being
    Tkinter.Canvas.

"""

sections = (
    ('Dynamic components', 1, 'Components',
	"""
	Page and tab components are created dynamically by the /add()/
        and /insert()/ methods.  By default, the pages are of type
        Tkinter.Frame and are created with a component group of *Page*
        and the tabs are of type Tkinter.Button and are created with a
        component group of *Tab*.

	"""
    ),
)

text = {}

text['options'] = {}

text['options']['arrownavigation'] = """
    If true and a tab button has the keyboard focus, then the Left and
    Right arrow keys can be used to select the page before or after
    the tab button with the focus.

"""

text['options']['borderwidth'] = """
    The width of the border drawn around each tab and around the
    selected page.

"""

text['options']['createcommand'] = """
    Specifies a function to call when a page is selected for the first
    time.  The function is called with a single argument, which is the
    name of the selected page, and is called before the *raisecommand*
    function.  This allows the creation of the page contents to be
    deferred until the page is first displayed.

"""

text['options']['lowercommand'] = """
    Specifies a function to call when the selected page is replaced
    with a new selected page.  The function is called with a single
    argument, which is the name of the previously selected page, and
    is called before the *createcommand* or *raisecommand* functions.

"""

text['options']['pagemargin'] = """
    The margin (in pixels) around the selected page inside the
    notebook's page border.

"""

text['options']['raisecommand'] = """
    Specifies a function to call when a new page is selected.  The
    function is called with a single argument, which is the name of
    the selected page.

"""

text['options']['tabpos'] = """
    Specifies the location of the tabs.  If *'n'*, tabs are created
    for each page and positioned at the top of the notebook.  If
    *None*, no tabs are created, in which case another selection
    widget can be used to select pages by calling the /selectpage()/
    method.

"""

text['components'] = {}

text['components']['hull'] = """
    This acts as the body for the megawidget.  The contents of the
    megawidget are created as canvas items and positioned in the
    hull using the canvas coordinate system.

"""

text['methods'] = {}

text['methods']['add'] = """
    Add a page at the end of the notebook. See the /insert()/ method
    for full details.

"""

text['methods']['delete'] = """
    Delete the pages given by 'pageNames' from the notebook.  Each of
    the 'pageNames' may have any of the forms accepted by the
    /index()/ method.

    If the currently selected page is deleted, then the next page, in
    index order, is selected.  If the *end* page is deleted, then the
    previous page is selected.

"""

text['methods']['insert'] = """
    Add a page to the notebook as a component named 'pageName'.  The
    page is added just before the page specified by 'before', which
    may have any of the forms accepted by the /index()/ method.  If
    *tabpos* is not *None*, also create a tab as a component named
    'pageName'-*tab*.  Keyword arguments prefixed with *page_* or
    *tab_* are passed to the respective constructors when creating the
    page or tab.  If the *tab_text* keyword argument is not given, the
    *text* option of the tab defaults to 'pageName'.  If a page is
    inserted into an empty notebook, the page is selected.  To add a
    page to the end of the notebook, use /add()/.  The method returns
    the 'pageName' component widget.

"""

text['methods']['index'] = """
    Return the numerical index of the page corresponding to 'index'. 
    This may be specified in any of the following forms:

    'name' --
         Specifies the page labelled 'name'.
    
    'number' --
         Specifies the page numerically, where *0* corresponds to
         the first page.

    *Pmw.END* --
         Specifies the last page.

    *Pmw.SELECT* --
         Specifies the currently selected page.
    
    If 'forInsert' is true, *Pmw.END* returns the number of pages
    rather than the index of the last page.

"""

text['methods']['nextpage'] = """
    If 'pageIndex' is *None*, then select the page after the
    currently selected page.  Otherwise select the page after
    'pageIndex', which may have any of the forms accepted by the
    /index()/ method.

"""

text['methods']['previouspage'] = """
    If 'pageIndex' is *None*, then select the page before the
    currently selected page.  Otherwise select the page before
    'pageIndex', which may have any of the forms accepted by the
    /index()/ method.

"""

text['methods']['page'] = """
    Return the frame component widget of the page 'pageIndex', where
    'pageIndex' may have any of the forms accepted by the /index()/
    method.

"""

text['methods']['tab'] = """
    Return the tab component widget of the page 'pageIndex', where
    'pageIndex' may have any of the forms accepted by the /index()/
    method.  If *tabpos* is *None*, return *None*.

"""

text['methods']['pagenames'] = """
    Return a list of the names of the pages, in display order.

"""

text['methods']['getcurselection'] = """
    Return the name of the currently selected page.

"""

text['methods']['selectpage'] = """
    Select 'page' to be the currently selected page.  The page will be
    raised and the previous selected page will be lowered.

"""

text['methods']['setnaturalsize'] = """
    Set the width and height of the notebook to be the maximum
    requested width and height of the pages specified by 'pageNames'.
    If 'pageNames' is *None*, the size of all pages are used to
    determine the size of the notebook.  Otherwise, 'pageNames' must
    be a list of page names whose sizes are to be used to determine
    the size of the notebook.  This method should be called after all
    pages and their contents have been created.  It calls
    /update_idletasks()/ so that the width and height of the pages can
    be determined.  This may cause the notebook to flash onto the
    screen at the default size before resizing to the natural size.

"""

text['methods']['recolorborders'] = """
    Change the color of the page and tab borders.  This method is
    required because the borders are created as canvas polygons and
    hence do not respond to normal color changing techniques, such as
    /Pmw.Color.changecolor()/.

"""
