complete = 1
reviewdate = "22 May 1998"

name = """
    abstract base class for all Pmw megawidgets
"""

description = """
    This class is the basis for all Pmw megawidgets.  It provides
    methods to manage options and component widgets.

    This class is normally used as a base class for other classes.  If
    the 'hullClass' argument is specified, such as in the ~MegaWidget~
    and ~MegaToplevel~ classes, a container widget is created to act
    as the parent of all other component widgets.  Classes derived
    from these sub classes create other component widgets and options
    to implement megawidgets that can be used in applications. 

    If no 'hullClass' argument is given to the constructor, no
    container widget is created and only the option configuration
    functionality is available.

"""

sections = (
    ('Components', 1, 'Description', 
    """
	A megawidget is generally made up of other widgets packed
	within the megawidget's containing widget.  These sub-widgets
	are called the 'components' of the megawidget and are given
	logical names for easy reference.  The component mechanism
	allows the user of a megawidget to gain controlled access to
	some of the internals of the megawidget, for example to call a
	method of a component or to set a component's configuration
	options.
	
	*Sub components:* If a component is itself a megawidget containing
	sub-components, then these sub-components can be referred to
	using the notation 'component_subcomponent'.  For example,
	~ComboBox~ has a component named *entryfield* which is an
	instance of ~EntryField~, which itself has a Tkinter.Entry
	component named *entry*.  In the context of the combobox, this
	entry widget can be referred to as *entryfield_entry*.

	*Component aliases:* Because the sub-component notation may
	make component names inconveniently long, components and
	sub-components can be aliased to simpler names.  For example,
	the *entryfield_entry* sub-component of ~ComboBox~ is aliased
	to simply *entry*.  If there is no conflict in component
	names, sub-component names are usually aliased to the name of
	the "leaf" component.

	*Component groups:* Similar components of a megawidget can be
	given a 'group' name, which allows all components of a group
	to be referenced using the one group name.  For example, the
	two arrow components of ~Counter~ have a group name of *Arrow*. 
	Also, megawidgets that can create an unlimited number of
	similar components, such as ~ButtonBox~, create each of these
	components with the same group name.  By convention, group
	names begin with a capital letter.

	"""
    ),
    ('Options', 1, 'Description', 
    """
	A megawidget defines options which allow the megawidget user
	to modify the appearance and behaviour of the megawidget. 
	Using the same technique as Tkinter widgets, the values of
	megawidget options may be set in calls to the constructor and
	to /configure()/ and the values may be queried by calls to
	/cget()/ and /configure()/.  Like Tkinter widgets, megawidget
	options are initialised with default values.  Also, if the
	'useTkOptionDb' option to /Pmw.initialise()/ has been set,
	then the Tk option database will be queried to get the initial
	values.  Strings found in the option database are converted
	to python objects (integer, float, tuple, dictionary, etc)
	using a restricted /eval()/ call.  Anything that is not accepted by
	/eval()/ is treated as a string.

	*Inherited options:* As well as the options defined in a class,
	a derived class inherits all options of its base classes.  The
	default value of an option defined by a base class may be
	modified by the derived class.

	*Initialisation options:* Some megawidget options can only be
	set in the call to the constructor.  These are called
	'initialisation options'.  Unlike normal configuration
	options, they cannot be set by calling the /configure()/
	method.

	*Component options:* Options of the components of a megawidget
	can be referred to using the notation 'component_option'. 
	Like the megawidget options, component options can be used in
	calls to the constructor and to the /cget()/ and /configure()/
	methods.  For example, the *state* option of the Tkinter.Text
	*text* component of ~ScrolledText~ may be set by calling

	    # widget.configure(text_state = 'disabled')

	Sub-components, component aliases and component groups may
	also be combined with options.  For example, the *state*
	option of the *entryfield_entry* component of ~ComboBox~
	may be set by calling

	    # combobox.configure(entryfield_entry_state = 'normal')

	Since it has an alias, it is more convenient to use the
	equivalent form

	    # combobox.configure(entry_state = 'normal')

	Also, the background color of both arrows of ~Counter~
	can be set using the *Arrow* component group.

	    # counter.configure(Arrow_background = 'aliceblue')

    """
    ),
    ('The pyclass component option', 1, 'Description', 
    """
	The *pyclass* component option is a special notation that can
	be used to specify a non-default python class for a component. 
	This can only be used when the component is being constructed. 
	For a component created during the construction of its parent
	megawidget, this option must be given to the constructor in
	the form 'component_pyclass'.  For example, to change the
	python class of the *text* sub-component of ~TextDialog~
	to a class *FontText.Text*

	    # dialog = Pmw.TextDialog(text_pyclass = FontText.Text)
	
	For components created after the construction of the parent
	megawidget, the *pyclass* option must be passed into the
	method which constructs the component.  For example, to set
	the python class of a button in ~ButtonBox~ to a class
	*MyButton*:

	    # buttonBox.add('special', pyclass = MyButton)
	
	The new python class of the component must support all methods
	and options that are used by the megawidget when operating on
	the component.  The exact interface required for each
	component is not documented.  You will have to examine the Pmw
	source code.  However, any class derived from the default
	class of a component can be used as the new class of the
	component, as long as all of the original methods and options
	are still supported.  For example, any class derived from
	*Tkinter.Text* can be used as the class of the *text*
	sub-component of ~TextDialog~. 

	The *pyclass* component option should not be confused with the
	*class* option that some of the Tk widgets support.  The
	*class* option sets the Tk option database class for the
	widget and is used by Tk to query the database for the default
	values of the widget's other options.  The name *pyclass* was
	chosen so that it did not conflict with any known Tk options.

    """
    ),
    ('Construction', 1, 'Description', 
    """
	The constructors of classes derived from this class all accept
	the same arguments:  one positional argument and any number of
	keyword arguments.  The positional argument defaults to *None*
	(meaning the root window) and specifies the widget to use as
	the parent when creating the 
	megawidget's *hull* component.  The keyword arguments define
	initial values for options.  The format for the constructors
	of derived classes is:

	#   def __init__(self, parent = None, **kw):
	
	"""
    ),
)

text = {}
text['methods'] = {}

text['methods']['cget'] = """
    Return the current value of 'option' (which should be in the
    format described in the *Options* section).  This method is also
    available using object subscripting, for example
    /myWidget['font']/.  Unlike Tkinter's cget(), which always returns
    a string, this method returns the same value and type as used when
    the option was set (except where 'option' is a component option
    and the component is a Tkinter widget, in which case it returns
    the string returned by Tcl/Tk).

"""

text['methods']['component'] = """
    Return the component widget whose name is 'name'.  This
    allows the user of a megawidget to access and configure component
    widgets directly.

"""

text['methods']['componentaliases'] = """
    Return the list of aliases for components.  Each item in the list
    is a tuple whose first item is the name of the alias and whose
    second item is the name of the component or sub-component it
    refers to.

"""

text['methods']['componentgroup'] = """
    Return the group of the component whose name is 'name' or *None*
    if it does not have a group.

"""

text['methods']['components'] = """
    Return a sorted list of names of the components of this
    megawidget.

"""

text['methods']['configure'] = """
    Query or configure the megawidget options.

    If no arguments are given, return a tuple consisting of all
    megawidget options and values, each as a 5-element tuple
    ('name', 'resourceName', 'resourceClass', 'default', 'value').
    This is in the same format as the value returned by the standard
    Tkinter /configure()/ method, except that the resource name is
    always the same as the option name and the resource class is the
    option name with the first letter capitalised.
    
    If one argument is given, return the 5 element tuple for 'option'.

    Otherwise, set the configuration options specified by the keyword
    arguments.  Each key should be in the format described in the
    *Options* section.

"""

text['methods']['createcomponent'] = """
    Create a component widget by calling 'widgetClass' with the
    arguments given by 'widgetArgs' and any keyword arguments.  The
    'componentName' argument is the name by which the component will
    be known and must not contain the underscore, *'_'*, character. 
    The 'componentGroup' argument specifies the group of the
    component.  The 'componentAliases' argument is a sequence of
    2-element tuples, whose first item is an alias name and whose
    second item is the name of the component or sub-component it is to
    refer to.

    If this method is called during megawidget construction, any
    component options supplied to the megawidget constructor which
    refer to this component (by 'componentName' or 'componentGroup')
    are added to the 'kw' dictionary before calling 'widgetClass'.  If
    the dictionary contains a *'pyclass'* key, then this item is
    removed from the dictionary and the value is used instead of
    'widgetClass'.  For more details see *The pyclass component option*
    section.
    
    This method may be called by derived classes during or after
    megawidget construction.  It returns the instance of the class
    created.

"""

text['methods']['createlabel'] = """
    Create a *Tkinter.Label* component named *'label'* in the 'parent'
    widget.  This is a convenience method used by several megawidgets
    that require an optional label.  The widget must have options
    named *labelpos* and *labelmargin*.  If *labelpos* is *None*, no
    label is created.  Otherwise, a label is created and positioned
    according to the value of *labelpos* and *labelmargin*.  The label
    is added to the parent using the /grid()/ method, with 'childCols'
    and 'childRows' indicating how many rows and columns the label
    should span.  Note that all other child widgets of the parent
    'must' be added to the parent using the /grid()/ method.  The
    /createlabel()/ method may be called by derived classes during
    megawidget construction.

"""

text['methods']['defineoptions'] = """
    Create options for this megawidget.  The 'optionDefs' argument
    defines the options.  It is a sequence of 3-element tuples,
    ('name', 'default', 'callback'), where 'name' is the name of the
    option, 'default' is its default value and 'callback' is the
    function to call when the value of the option is set by a call to
    /configure()/.  The 'keywords' argument should be the keyword
    arguments passed in to the constructor of a megawidget.  The user
    may override the default value of an option by supplying a keyword
    argument to the constructor.

    If any option already created by a base class is redefined by
    'optionDefs', then the base class's value will be overridden.  If
    the 'callback' field is not *None*, then this will also override
    the callback set by the base class.

    This should be called before the constructor of the base class, so
    that default values defined in a derived class override those in a
    base class.

    If 'callback' is *Pmw.INITOPT*, then the option is an
    'initialisation option'.

    The 'dynamicGroups' argument contains a list of the groups of the
    components created dynamically by this megawidget.  If a group is
    included in this list, then it not an error if a keyword argument
    for the group is given to the constructor or to /configure()/,
    even when no components with this group have been created.

"""

text['methods']['addoptions'] = """
    Add additional options for this megawidget.  The 'optionDefs'
    argument is treated in the same way as for the /defineoptions()/
    method.

    This method is for use by derived classes.  It is only used if a
    megawidget should conditionally define some options, perhaps
    depending on the value of other options.  Usually, megawidgets
    unconditionally define all their options in the call to
    /defineoptions()/ and do not need to use /addoptions()/.  This
    method may be called after the call to /defineoptions()/ and
    before the call to /initialiseoptions()/.

"""

text['methods']['destroy'] = """
    Destroy the *hull* component widget, if it exists, including all
    of its children.
    
"""

text['methods']['destroycomponent'] = """
    Remove the megawidget component called 'name'.  This method may be
    called by derived classes to destroy a megawidget component.  It
    destroys the component widget and then removes all record of the
    component from the megawidget.

"""

text['methods']['hulldestroyed'] = """
    Return true if the Tk widget corresponding to the *hull* component
    has been destroyed.

"""

text['methods']['initialiseoptions'] = """
    Check keyword arguments and call option callback functions.  This
    must be called at the end of a megawidget constructor with
    'myClass' set to the class being defined.
    
    It checks that all keyword arguments given to the constructor have
    been used.  If not, it raises an error indicating which arguments
    were unused.  A keyword is defined to be used if, during the
    construction of a megawidget, it is defined in a call to
    /defineoptions()/ or /addoptions()/ (by the megawidget or one of
    its base classes), or it references, by name, a component of the
    megawidget, or it references, by group, at least one component. 
    It also calls the configuration callback function for all
    configuration options.

    This method is only effective when called by the constructor of
    the 'leaf' class, that is, if 'myClass' is the same as the class
    of the object being constructed.  The method returns immediately
    when called by the constructors of base classes.

"""

text['methods']['interior'] = """
    Return the widget framing the interior space in which any children
    of this megawidget should be created.  By default, this returns
    the *hull* component widget, if one was created, or *None*
    otherwise.  A subclass should use the widget returned by
    /interior()/ as the parent of any components or sub-widgets it
    creates.  Megawidgets which can be further subclassed, such as
    ~Dialog~, should redefine this method to return the widget in
    which subclasses should create children.  The overall containing
    widget is always available as the *hull* component.
    
"""

text['methods']['isinitoption'] = """
    If 'option' is an initialisation option, return true.  Otherwise,
    return false (the option is a configuration option).  The 'option'
    argument must be an option of this megawidget, not an option of a
    component.  Otherwise an exception is raised.

"""

text['methods']['options'] = """
    Return a sorted list of this megawidget's options.  Each item in
    the list is a 3-element tuple, ('option', 'default', 'isinit'),
    where 'option' is the name of the option, 'default' is its default
    value and 'isinit' is true if the option is an initialisation
    option.

"""
