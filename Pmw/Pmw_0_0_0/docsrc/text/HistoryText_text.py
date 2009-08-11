complete = 1
reviewdate = "20 May 2002"

name = """
    text widget with a course-grained form of history
"""

description = """
    A history text is a scrolled text widget with added functionality
    to maintain a history of each screen and allow editing of prior
    screens.  Here, 'screen' refers to the entire contents of the text
    widget.  This widget does not support a fine-grained history of
    every change made to the text.

    Together with a few buttons and a scrolled text to display the
    results, a history text can be used as the query-entry part of a
    simple interactive text-based database query system.  When the
    user enters and executes a query, the query (the entire contents
    of the text widget) is added to the history list.  The user may
    view previous queries and either execute them again or modify them
    and execute the new query.  If a previously executed query is
    modified, the user may undo or redo all changes made to the query
    'before the query is executed'.
    
"""

text = {}
text['options'] = {}

text['options']['compressany'] = """
    See /addhistory()/.

"""

text['options']['compresstail'] = """
    See /addhistory()/.

"""

text['options']['historycommand'] = """
    This is a callback to indicate whether the currently displayed
    entry in the history list has a previous or next entry.  The
    callback is given two arguments, 'prevstate' and 'nextstate'.  If
    the currently displayed entry is first in the history list, then
    'prevstate' is *'disabled'*, otherwise it is *'normal'*.  If the
    currently displayed entry is last in the history list, then
    'nextstate' is *'disabled'*, otherwise it is *'normal'*.  These
    values can be used, for example, to modify the state of *Next* and
    *Previous* buttons that call the /next()/ and /prev()/ methods.

"""

text['components'] = {}

text['methods'] = {}

text['methods']['addhistory'] = """
    Append the currently displayed text to the history list.

    If *compressany* is true, a new entry will be added to the history
    list only if the currently displayed entry has changed.

    If *compresstail* is true, a new entry will be added to the
    history list only if the currently displayed entry has changed
    'or' if it is not the last entry in the history list.
    
"""

text['methods']['next'] = """
    Display the next screen in the history list.
    
"""

text['methods']['prev'] = """
    Display the previous screen in the history list.

"""

text['methods']['undo'] = """
    Undo all changes made since this entry was added to the history
    list.
    
"""

text['methods']['redo'] = """
    Reverse the effect of /undo()/.
    
"""

text['methods']['gethistory'] = """
    Return the history list.  Each entry in the list is a 3-tuple. 
    The first item in a history entry is the original text as added by
    /addhistory()/.  The second item is the edited text (if the user
    has modified the entry but /addhistory()/ has not yet been called
    on the text).  The third item specifies whether the entry should
    currently display the original or modified text.
    
"""
