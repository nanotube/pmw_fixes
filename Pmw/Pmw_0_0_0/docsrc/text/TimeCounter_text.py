complete = 1
reviewdate = "25 May 2002"

name = """
    counter for display and input of time
"""

description = """
    A time counter is similar to a regular ~Counter~ except that the
    user may increment and decrement the hours, minutes and seconds
    individually.

"""

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

text['options']['command'] = """
    This specifies a function to call whenever the *<Return>* key is
    pressed in one of the entry fields or /invoke()/ is called.

"""

text['options']['initwait'] = """
    Specifies the initial delay (in milliseconds) before a depressed
    arrow button automatically starts to repeat counting.

"""

text['options']['max'] = """
    Specifies the maximum acceptable time in the form "HH:MM:SS", or
    *None* if no maximum checking should be performed.

"""

text['options']['min'] = """
    Specifies the minimum acceptable time in the form "HH:MM:SS", or
    *None* if no minimum checking should be performed.

"""

text['options']['padx'] = """
    Specifies how much wider to make each column than the default
    width (where a column consists of two arrows and an entry field). 
    The entry fields expand to fill the extra space, but the arrow
    buttons are centered in the available space.

"""

text['options']['pady'] = """
    Specifies how much higher to make each row of arrow buttons than
    the default hight.  The arrow buttons are centered in the
    available space.

"""

text['options']['repeatrate'] = """
    Specifies the delay (in milliseconds) between automatic counts
    while an arrow button is held pressed down.

"""

text['options']['value'] = """
    Specifies the initial contents of the time counter, in the form
    "HH:MM:SS".  If this is *None*, the current time is used as the
    initial contents.

"""

text['components'] = {}

text['components']['downhourarrow'] = """
    The arrow button used for decrementing the hour field.

"""

text['components']['downminutearrow'] = """
    The arrow button used for decrementing the minute field.

"""

text['components']['downsecondarrow'] = """
    The arrow button used for decrementing the second field.

"""

text['components']['frame'] = """
    If the *label* component has been created (that is, the *labelpos*
    option is not *None*), the *frame* component is created to act as
    the container of the entry fields and arrow buttons.  If there is
    no *label* component, then no *frame* component is created and the
    *hull* component acts as the container.  In either case the border
    around the container of the entry fields and arrow buttons will be
    raised (but not around the label).

"""

text['components']['hourentryfield'] = """
    The entry field where the hours are entered and displayed.

"""

text['components']['minuteentryfield'] = """
    The entry field where the minutes are entered and displayed.

"""

text['components']['secondentryfield'] = """
    The entry field where the seconds are entered and displayed.

"""

text['components']['uphourarrow'] = """
    The arrow button used for incrementing the hour field.

"""

text['components']['upminutearrow'] = """
    The arrow button used for incrementing the minute field.

"""

text['components']['upsecondarrow'] = """
    The arrow button used for incrementing the second field.

"""

text['methods'] = {}

text['methods']['decrement'] = """
    Decrement the time by 'seconds' seconds.

"""

text['methods']['getint'] = """
    Return the currently displayed time as a number of seconds.

"""

text['methods']['getstring'] = """
    Same as /getvalue()/ method.

"""

text['methods']['getvalue'] = """
    Return the currently displayed time as a string in the form
    "HH:MM:SS".

"""

text['methods']['setvalue'] = """
    Set the contents of the time counter, where 'text' must be in the
    form "HH:MM:SS".
    
"""

text['methods']['increment'] = """
    Increment the time by 'seconds' seconds.

"""

text['methods']['invoke'] = """
    Invoke the command specified by the *command* option as if the
    *<Return>* key had been pressed.

"""
