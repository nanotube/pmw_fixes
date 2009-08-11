reviewdate = "25 May 2002"

name = """
    interface to some BLT widgets and commands
    
"""

description = """
    This module contains function interfaces to the BLT /busy/ command
    as well as the classes *Pmw.Blt.Vector*, *Pmw.Blt.Graph*,
    *Pmw.Blt.Stripchart* and *Pmw.Blt.Tabset*, which are interfaces to
    the vector, graph, stripchart and tabset commands of version 2.4
    of the *BLT* extension to Tk.  The interfaces are complete except
    for *Pmw.Blt.Vector* where several creation options, methods and
    operations have not been implemented.

    The blt graph and barchart widgets are essentially the same and so
    only the graph widget has been ported.  The /element_create()/
    method is not implememted for *Pmw.Blt.Graph*, so instead:

        - to create a 'line' element, use the /line_create()/ method and

        - to create a 'bar' element, use the /bar_create()/ method.

    To operate on elements, use the /element_*()/ methods, such as
    /element_bind()/, /element_activate()/, etc.

    *Note:* Full documentation of Pmw.Blt.Graph is available in
    ~~http://www.ifi.uio.no/~hpl/Pmw.Blt/doc/~~A User's Guide to Pmw.Blt~~
    written by Bjorn Ove Thue and Hans Petter Langtangen.
    You can also download 
    ~~http://www.ifi.uio.no/~hpl/Pmw.Blt/Pmw.Blt.doc.tar.gz~~the full HTML document~~
    of the guide for local viewing.
    
"""

text = {}

text['functions'] = {}

text['functions']['busy_hold'] = """
    Interface to the BLT /busy hold/ command.

"""

text['functions']['busy_release'] = """
    Interface to the BLT /busy release/ command.

"""

text['functions']['busy_forget'] = """
    Interface to the BLT /busy forget/ command.

"""

text['functions']['haveblt'] = """
    Return true if any commands in the BLT extension are available.

"""

text['functions']['havebltbusy'] = """
    Return true if the BLT *busy* command is available.

"""

text['functions']['vector_expr'] = """
    Interface to the BLT /vector expr/ command.

"""

text['functions']['vector_names'] = """
    Interface to the BLT /vector names/ command.

"""
