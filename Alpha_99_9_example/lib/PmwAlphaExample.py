import string
import Pmw

_default_text = "AlphaExample example alpha Pmw megawidget.\nPmw version: " + \
    Pmw.version() + '\nPmw Alpha versions: ' + \
    string.join(Pmw.version(alpha = 1), ' ')
 
class AlphaExample(Pmw.MessageDialog):
    # Dummy widget for illustrating use of Pmw alpha version directory
 
    def __init__(self, parent = None, **kw):
 
	# Define the megawidget options.
	INITOPT = Pmw.INITOPT
	optiondefs = (
	    ('message_text', _default_text, None),
	)
	self.defineoptions(kw, optiondefs)
 
	# Initialise the base class (after defining the options).
	Pmw.MessageDialog.__init__(self, parent)
 
	# Check keywords and initialise options.
	self.initialiseoptions(AlphaExample)
