complete = 1

name = """
    information line for displaying short messages
"""

description = """
    This class creates a single-line message display area.  Messages
    of several different types may displayed.  Messages are cleared
    after a period defined for each message type.  Each message type
    has a priority so that if the application attempts to display more
    than one message at a time, the message with the highest priority
    will be displayed.  Messages may be accompanied by a number of
    audible bells.

"""

no_auto_default = ('messagetypes',)

text = {}
text['options'] = {}

text['options']['messagetypes'] = """
    This defines what message types are supported by the message bar
    and the characteristics of those message types.  It is a
    dictionary where the key is a string specifying a message type and
    the value is a tuple of four integers, ('priority', 'showtime',
    'bells', 'logmessage'), where 'priority' is the rank of the
    message type, 'showtime' is the number of seconds to display
    messages of this message type, 'bells' is the number of audible
    bells to ring and 'logmessage' is a boolean
    specifying whether this message should be logged for retrieval
    later.  Messages with a higher priority are displayed in
    preference to those with lower priority.  If a high priority
    message times out (because it has been displayed for 'showtime'
    seconds), then a lower priority message may be displayed.  A
    'showtime' of *0* means that the message will never time out and
    is useful for displaying messages describing the current state of
    the application as opposed to messages describing events.  Logging
    is not currently implemented.  The default is

	# {
	#     'systemerror'  : (5, 10, 2, 1),
	#     'usererror'    : (4, 5, 1, 0),
	#     'busy'         : (3, 0, 0, 0),
	#     'systemevent'  : (2, 5, 0, 0),
	#     'userevent'    : (2, 5, 0, 0),
	#     'help'         : (1, 5, 0, 0),
	#     'state'        : (0, 0, 0, 0),
	# }

"""

text['options']['silent'] = """
    If true, no audible bells will sound, regardless of the value for
    'bells' defined in the *messagetypes* option.

"""

text['components'] = {}

text['components']['entry'] = """
    The widget where the messages are displayed.  Long messages may be
    scrolled horizontally by dragging with the middle mouse button.

"""

text['methods'] = {}

text['methods']['helpmessage'] = """
    A convenience method to display 'text' in the message bar
    according to the characteristics defined by the *help* message type.
    Equivalent to /message(\\'help\\', text)/.
    
"""

text['methods']['resetmessages'] = """
    Clear the 'type' message and all message types with a lower
    priority, except permanent messages, such as *state*.  This is
    useful to clear the *busy* message and any outstanding event and
    help messages.
    
"""

text['methods']['message'] = """
    Display 'text' in the message bar according to the characteristics
    defined by the 'type' message type, as discussed under
    *messagetypes*.
    
"""
