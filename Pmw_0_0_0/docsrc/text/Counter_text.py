complete = 1
reviewdate = "24 May 1998"

name = """
    entry field with up and down arrow buttons
"""

description = """
    This class consists of an entry field with arrow buttons to
    increment and decrement the value in the entry field.  Standard
    counting types include numbers, times and dates.  A user defined
    counting function may also be supplied for specialised counting. 
    Counting can be used in combination with the entry field's
    validation.  The components may be laid out horizontally or
    vertically.

    Each time an arrow button is pressed the value displayed in the
    entry field is incremented or decremented by the value of the
    *increment* option.  If the new value is invalid (according to the
    entry field's *validate* option, perhaps due to exceeding minimum
    or maximum limits), the old value is restored.

    When an arrow button is pressed and the value displayed is not an
    exact multiple of the *increment*, it is "truncated" up or down to
    the nearest increment.

"""

no_auto_default = ('datatype',)

text = {}
text['options'] = {}

text['options']['autorepeat'] = """
    If true, the counter will continue to count up or down while an
    arrow button is held pressed down.

"""

text['options']['buttonaspect'] = """
    Specifies the width of the arrow buttons as a proportion of their
    height.  Values less than *1.0* will produce thin arrow buttons. 
    Values greater than *1.0* will produce fat arrow buttons.

"""

text['options']['datatype'] = """

    Specifies how the counter should count up and down.

    The most general way to specify the *datatype* option is as a
    dictionary.  The kind of counting is specified by the *'counter'*
    dictionary field, which may be either a function or the name of
    one of the standard counters described below.  The default is
    *'numeric'*.
    
    Any other fields in the dictionary are passed on to the 'counter'
    function as keyword arguments.
    
    If *datatype* is not a dictionary, then it is equivalent to
    specifying it as a dictionary with a single *'counter'* field. 
    For example, /datatype = 'real'/ is equivalent to
    /datatype = {'counter' : 'real'}/.

    The standard counters are:

    *'numeric'* -- An integer number, as accepted by /string.atol()/.

    *'integer'* -- Same as *'numeric'*.

    *'real'* -- A real number, as accepted by /string.atof()/.  This
	counter accepts a *'separator'* argument, which specifies
	the charactor used to represent the decimal point.  The
	default *'separator'* is *'.'*.

    *'time'* -- A time specification, as accepted by
	/Pmw.timestringtoseconds()/.  This counter accepts a
	*'separator'* argument, which specifies the charactor used to
	separate the time fields.  The default separator is *':'*.

    *'date'* -- A date specification, as accepted by
	/Pmw.datestringtojdn()/.  This counter accepts a *'separator'*
	argument, which specifies the charactor used to separate the
	three date fields.  The default is *'/'*.  This counter also
	accepts a *'format'* argument, which is passed to
	/Pmw.datestringtojdn()/ to specify the desired ordering of the
	fields.  The default is *'ymd'*.

    If *'counter'* is a function, then it will be called whenever the
    counter is incremented or decremented.  The function is called
    with at least three arguments, the first three being ('text',
    'factor', 'increment'), where 'text' is the current contents of
    the entry field, 'factor' is *1* when incrementing or *-1* when
    decrementing, and 'increment' is the value of the *increment*
    megawidget option.

    The other arguments are keyword arguments made up of the fields of
    the *datatype* dictionary (excluding the *'counter'* field).

    The 'counter' function should return a string representing the
    incremented or decremented value.  It should raise a a
    *ValueError* exception if the 'text' is invalid.  In this case the
    bell is rung and the entry text is is not changed.

    The default for *datatype* is *numeric*.

"""

text['options']['increment'] = """
    Specifies how many units should be added or subtracted when the
    counter is incremented or decremented.  If the currently displayed
    value is not a multiple of *increment*, the value is changed to
    the next multiple greater or less than the current value.

    For the number datatypes, the value of *increment* is a number. 
    For the *'time'* datatype, the value is in seconds.  For the
    *'date'* datatype, the value is in days.

"""

text['options']['initwait'] = """
    Specifies the initial delay (in milliseconds) before a depressed
    arrow button automatically starts to repeat counting.

"""

text['options']['orient'] = """
    Specifies whether the arrow buttons should appear to the left and
    right of the entry field (*'horizontal'*) or above and below
    (*'vertical'*).

"""

text['options']['padx'] = """
    Specifies a padding distance to leave around the arrow buttons in
    the x direction.

"""

text['options']['pady'] = """
    Specifies a padding distance to leave around the arrow buttons in
    the y direction.

"""

text['options']['repeatrate'] = """
    Specifies the delay (in milliseconds) between automatic counts
    while an arrow button is held pressed down.

"""

text['components'] = {}

text['components']['downarrow'] = """
    The arrow button used for decrementing the counter.  Depending on
    the value of *orient*, it will appear on the left or below the
    entry field.

"""

text['components']['entryfield'] = """
    The entry field widget where the text is entered, displayed and
    validated.

"""

text['components']['frame'] = """
    If the *label* component has been created (that is, the *labelpos*
    option is not *None*), the *frame* component is created to act as
    the container of the entry field and arrow buttons.  If there is
    no *label* component, then no *frame* component is created and the
    *hull* component acts as the container.  In either case the border
    around the container of the entry field and arrow buttons will be
    raised (but not around the label).

"""

text['components']['uparrow'] = """
    The arrow button used for incrementing the counter.  Depending on
    the value of *orient*, it will appear on the right or above the
    entry field.

"""

text['methods'] = {}

text['methods']['decrement'] = """
    Decrement the counter once, as if the down arrow had been pressed.

"""

text['methods']['increment'] = """
    Increment the counter once, as if the up arrow had been pressed.

"""
