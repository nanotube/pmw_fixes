complete = 1
reviewdate = "22 May 1998"

name = """
    entry widget with validation
"""

description = """
    This class consists of an entry widget with optional validation of
    various kinds.  Built-in validation may be used, such as
    *integer*, *real*, *time* or *date*, or an external validation
    function may be supplied.  If valid text is entered, it will be
    displayed with the normal background.  If invalid text is entered,
    it is not displayed and the previously displayed text is restored. 
    If partially valid text is entered, it will be displayed with a
    background color to indicate it is in error.  An example of
    partially valid *real* text is *'-.'*, which may be the first two
    charactes of the valid string *'-.5'*.  Some validators, such as
    *date*, have a relaxed interpretation of partial validity, which
    allows the user flexibility in how they enter the text.

    Validation is performed 'early', at each keystroke or other event
    which modifies the text.  However, if partially valid text is
    permitted, the validity of the entered text can be checked just
    before it is to be used, which is a form of 'late' validation.
    
    Minimum and maximum values may be specified.  Some validators also
    accept other specifications, such as date and time formats and
    separators.

"""

sections = (
    ('Validation function return values', 1, 'Description',
	"""
	Validation is performed by a function which takes as its first
	argument the entered text and returns one of three standard
	values, indicating whether the text is valid:

	*Pmw.OK* -- The text is valid.

	*Pmw.ERROR* -- The text is invalid and is not acceptable for
	    display.  In this case the entry will be restored to its
	    previous value.
	    
	*Pmw.PARTIAL* -- The text is partially valid and is acceptable
	    for display.  In this case the text will be displayed
	    using the *errorbackground* color.

	"""
    ),
)

no_auto_default = ('invalidcommand', 'validate')

text = {}
text['options'] = {}

text['options']['command'] = """
    This specifies a function to call whenever the *<Return>* key is
    pressed or /invoke()/ is called.

"""

text['options']['errorbackground'] = """
    Specifies the background color to use when displaying invalid or
    partially valid text.

"""

text['options']['invalidcommand'] = """
    This is executed when invalid text is entered and the text is
    restored to its previous value (that is, when the *validate*
    function returns *Pmw.ERROR*).  It is also called if an attempt is
    made to set invalid text in a call to /setentry()/.  The default
    is *self.bell*.

"""

text['options']['modifiedcommand'] = """
    This is called whenever the contents of the entry has been changed
    due to user action or by a call to /setentry()/.

"""

text['options']['validate'] = """
    Specifies what kind of validation should be performed on the entry
    input text.

    The most general way to specify the *validate* option is as a
    dictionary.  The kind of validation is specified by the
    *'validator'* dictionary field, which may be the name of one of
    the standard validators described below, the name of a validator
    supplied by the *extravalidators* option, a function or *None*. 
    The default is *None*.
    
    Any other dictionary fields specify other restrictions on the
    entered values.  For all validators, the following fields may be
    specified:

    *'min'* -- Specifies the minimum acceptable value, or *None* if no
	minimum checking should be performed.  The default is *None*.
    
    *'max'* -- Specifies the maximum acceptable value, or *None* if no
	maximum checking should be performed.  The default is *None*.
    
    *'minstrict'* -- If true, then minimum checking is strictly enforced. 
	Otherwise, the entry input may be less than *min*, but will be
	displayed using the *errorbackground* color.  The default is true.
    
    *'maxstrict'* -- If true, then maximum checking is strictly enforced. 
	Otherwise, the entry input may be more than *max*, but will be
	displayed using the *errorbackground* color.  The default is true.

    If the dictionary contains a *'stringtovalue'* field, it overrides
    the normal 'stringtovalue' function for the validator.  The
    'stringtovalue' function is described below.

    Other fields in the dictionary (apart from the core fields
    mentioned above) are passed on to the 'validator' and
    'stringtovalue' functions as keyword arguments.
    
    If *validate* is not a dictionary, then it is equivalent to
    specifying it as a dictionary with a single *'validator'* field. 
    For example, /validate = 'real'/ is equivalent to /validate =
    {'validator' : 'real'}/ and specifies real numbers without any
    minimum or maximum limits and using *'.'* as the decimal point
    character.

    The standard validators accepted in the *'validator'* field are:

    *'numeric'* -- An integer greater than or equal to 0.  Digits
	only. No sign.

    *'integer'* -- Any integer (negative, 0 or positive) as accepted
	by /string.atol()/.

    *'hexadecimal'* -- Hex number (with optional leading *'0x'*), as accepted
	by /string.atol(text, 16)/.

    *'real'* -- A number, with or without a decimal point and optional
	exponent (e or E), as accepted by /string.atof()/.  This
	validator accepts a *'separator'* argument, which specifies
	the charactor used to represent the decimal point.  The
	default *'separator'* is *'.'*.

    *'alphabetic'* -- Consisting of the letters *'a-z'* and *'A-Z'*.
	In this case, *'min'* and *'max'* specify limits on the length
	of the text.

    *'alphanumeric'* -- Consisting of the letters *'a-z'*, *'A-Z'* and *'0-9'*.
	In this case, *'min'* and *'max'* specify limits on the length
	of the text.

    *'time'* -- Hours, minutes and seconds, in the format
	*'HH:MM:SS'*, as accepted by /Pmw.timestringtoseconds()/. 
	This validator accepts a *'separator'* argument, which
	specifies the charactor used to separate the three fields. 
	The default separator is *':'*.  The time may be negative.

    *'date'* -- Day, month and year, as accepted by
	/Pmw.datestringtojdn()/.  This validator accepts a
	*'separator'* argument, which specifies the charactor used to
	separate the three fields.  The default is *':'*.  This
	validator also accepts a *'format'* argument, which is passed to
	/Pmw.datestringtojdn()/ to specify the desired ordering of the
	fields.  The default is *'ymd'*.

    If *'validator'* is a function, then it will be called whenever
    the contents of the entry may have changed due to user action or
    by a call to /setentry()/.  The function is called with at least
    one argument, the first one being the new text as modified by the
    user or /setentry()/.  The other arguments are keyword arguments
    made up of the non-core fields of the *validate* dictionary.
    
    The 'validator' function should return *Pmw.OK*, *Pmw.ERROR* or
    *Pmw.PARTIAL* as described above.  It should not perform minimum
    and maximum checking.  This is done after the call, if it returns
    *Pmw.OK*.

    The *'stringtovalue'* field in the dictionary may be specified as
    the name of one of the standard validators, the name of a
    validator supplied by the *extravalidators* option, a function or
    *None*.

    The 'stringtovalue' function is used to convert the entry input
    into a value which can then be compared with any minimum or
    maximum values specified for the validator.  If the *'min'* or
    *'max'* fields are specified as strings, they are converted using
    the 'stringtovalue' function.  The 'stringtovalue* function is
    called with the same arguments as the 'validator' function.  The
    'stringtovalue' function for the standard number validators
    convert the string to a number.  Those for the standard alpha
    validators return the length of the string.  Those for the
    standard *'time'* and *'date'* validators return the number of
    seconds and the Julian Day Number, respectively.  See
    /Pmw.stringtoreal()/, /Pmw.timestringtoseconds()/ and
    /Pmw.datestringtojdn()/.

    If the validator has been specified as a function and no
    *'stringtovalue'* field is given, then it defaults to the standard
    python /len()/ function.
    
    If *'validator'* is *None*, no validation is performed.  However,
    minimum and maximum checking may be performed, according to the
    'stringtovalue' function.  For example, to limit the entry text to
    a maximum of five characters:

    # Pmw.EntryField(validate = {'max' : 5})

    The validator functions for each of the standard validators can
    be accessed as:

      # Pmw.numericvalidator
      # Pmw.integervalidator
      # Pmw.hexadecimalvalidator
      # Pmw.realvalidator
      # Pmw.alphabeticvalidator
      # Pmw.alphanumericvalidator
      # Pmw.timevalidator
      # Pmw.datevalidator

    Whenever the *validate* option is configured, the text currently
    displayed in the entry widget is revalidated.  If it is not valid,
    the *errorbackground* color is set and the *invalidcommand*
    function is called.  However, the displayed text is not modified.

    The default for *validate* is *None*.

"""

text['options']['extravalidators'] = """
    This is a dictionary of extra validators.  The keys are the names
    of validators which may be used in a future call to the
    *validate* option.  Each value in the dictionary is a tuple of
    ('validate_function', 'stringtovalue_function').

    The 'validate_function' is used to implement the validation and
    the 'stringtovalue_function' is used to convert the entry input
    into a value which can be compared with the minimum and maximum
    limits.  These functions are as described for the *validate*
    option.

    If either of these is not given as a function, it is assumed to be
    the name of one of the other extra validators or one of the
    standard validators.  The alias search is performed when the
    *validate* option is configured, not when the *extravalidators*
    option is configured or when the *validate* function is called.

    If the name of one of the extra validators is the same as one of
    the standard validators, the extra validator takes precedence.

"""

text['options']['value'] = """
    Specifies the initial contents of the entry.
    If this text is invalid, it will be displayed with the
    *errorbackground* color and the *invalidcommand* function will be called. 
    If both *value* and *entry_textvariable* options are specified in
    the constructor, *value* will take precedence.

"""

text['components'] = {}

text['components']['entry'] = """
    The widget where the user may enter text.  Long text may be
    scrolled horizontally by dragging with the middle mouse button.

"""

text['methods'] = {}

text['methods']['checkentry'] = """
    Check the validity of the current contents of the entry widget
    and return the result.
    If the text is not valid, set the background to *errorbackground* and
    call the *invalidcommand* function.  If there is a variable
    specified by the *entry_textvariable* option, this method should be
    called after the /set()/ method of the variable is called.  If this
    is not done in this case, the entry widget background will not be
    set correctly.
    
"""

text['methods']['clear'] = """
    Remove all text from the entry widget.  Equivalent to /setentry('')/.
    
"""

text['methods']['invoke'] = """
    Invoke the command specified by the *command* option as if the
    *<Return>* key had been pressed and return the result.
    
"""

text['methods']['setentry'] = """
    Set the contents of the entry widget to 'text' and carry out
    validation as if the text had been entered by the user.  If the
    text is invalid, the entry widget will not be changed and the
    *invalidcommand* function will be called.  Return the validity
    of 'text'.
    
"""

text['methods']['valid'] = """
    Return true if the contents of the entry widget are valid.
    
"""
