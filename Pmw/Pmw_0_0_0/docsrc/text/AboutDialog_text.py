complete = 1
reviewdate = "18 May 2002"

name = """
    window to display version and contact information
"""

description = """
    An about dialog is a dialog window which displays information
    about the application, such as name, version, copyright and
    contact details.

    The text of the message is constructed from the application name
    (given by the *applicationname* option) followed by the values
    supplied in the most recent calls to /Pmw.aboutversion()/,
    /Pmw.aboutcopyright()/ and /Pmw.aboutcontact()/ functions.

    The icon of the message defaults to *'info'*, but may be changed
    using the *icon_bitmap* component option.

"""

text = {}
text['options'] = {}

text['options']['applicationname'] = """
    The name of application, to be dispayed in the dialog body and in
    the window title if the *title* option is not given.

"""

text['components'] = {}

text['methods'] = {}
