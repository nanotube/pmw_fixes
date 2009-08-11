# HTMLgen.py
# COPYRIGHT (C) 1996, 1997  ROBIN FRIEDRICH
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.
# THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
# RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""A class library for the generation of HTML documents.

Each HTML tag type has a supporting class which is responsible for
emitting itself as valid HTML formatted text. An attempt is made to
provide classes for newer HTML 3.0 and proposed tag elements.  An
excellant reference for HTML tag elements can be found at
[Sandia National Labs].  I'll try to keep up with this list. 

The Document class is a container object which acts as a focal point
to populate all the contents of a particular web page. It also can
enforce consistent document formating according to the guidelines from
the [Yale Web Style Manual].

Features include customization of document template graphics / colors
through use of resource files, minimizing the need for modifying or
subclassing from the module source code. Support for tables, frames,
forms (persistant and otherwise) and client-side imagemaps are included.

A newer implementation for the Table support is now included,
TableLite().  In support of this there are new tag classes TD, TH, TR
and Caption.  These class instances can be assembled in any way to
populate the TableLite container object. 

.. [Sandia National Labs] http://www.sandia.gov/sci_compute/elements.html
.. [Yale Web Style Manual] http://info.med.yale.edu/caim/StyleManual_Top.HTML
"""

import string, regex, regsub, time, os
import UserList, copy

__author__ = 'Robin Friedrich   friedric@phoenix.net'
__version__ = '1.2.0'

StringType = type('s')
IntType    = type(3)
ListType   = type([1])
TupleType  = type((1,2))
InstanceType = type(UserList.UserList())
DOCTYPE = '<!DOCTYPE HTML PUBLIC "-//Netscape_Microsoft//DTD HTML 3.0//EN">\n<HTML>\n'
PRINTECHO = 0
###### UTILITIES USED INTERNALLY ########
def escape(text):
    """Converts the special characters '<', '>', and '&'.
    
    RFC 1866 specifies that these characters be represented
    in HTML as &lt; &gt; and &amp; respectively.
    """
    # using this join/split technique is faster than regsub
    # for strings with few occurances. Otherwise it's a wash.
    split = string.split
    join  = string.join
    text = join(split(text, '&'), '&amp;') # must be done 1st
    text = join(split(text, '<'), '&lt;')
    text = join(split(text, '>'), '&gt;')
    return text


def getgifsize(path, data=None):
    """ getgifsize reads the first ten bytes of the
    file specified by path, checks whether it's a GIF file,
    returns the width and height of the GIF file if it is one,
    else TypeError is raised.
    """
    # Author: just@knoware.nl (Just van Rossum)
    # Modified by: johnm@magnet.com (John Mitchell)
    # -- added predefined-data argument, fixed endian problem
    #    by using ord() instead of struct
    if not data:
	gifFile = open(path, "rb")
	data = gifFile.read(10)
	gifFile.close()

    if data[:4] <> "GIF8":
	raise TypeError, "Not a GIF file."

    return (ord(data[7])*256 + ord(data[6]),
	    ord(data[9])*256 + ord(data[8]))


class URL:
    """Represent a Universal Resource Locator.
    
    Assumed to be of the form: **http://www.node.edu/directory/file.html**
    with *http* being an example protocol, *www.node.edu* being an example
    network node, *directory* being the directory path on that node, and
    *file.html* being the target filename. The argument string is parsed
    into attributes .proto , .node , .dir , .file respectively and may
    be altered individually after instantiation. The __repr__ method
    simply reassembles the components into a full URL string.
    """
    pattern = regex.compile('^\([a-z]+\)://\([^/ ]*\)\([^ ]*\)$',regex.casefold)
    def __init__(self, url=''):
        self.proto = ''
        self.node = ''
        self.dir = ''
        self.file = ''
        if not url: return
        if self.pattern.search(url) > -1:
            self.proto, self.node, path = self.pattern.group(1,2,3)
            self.dir, self.file = self.split(path)
        else:
            print 'Invalid URL: '+ url

    def split(self, p):
        """Same as posixpath.split()

        Copied here for availability on the Mac.
        """
        i = string.rfind(p, '/') + 1
        head, tail = p[:i], p[i:]
        if head and head != '/'*len(head):
                while head[-1] == '/':
                        head = head[:-1]
        return head, tail

    def __repr__(self):
        return '%s://%s%s/%s' % (self.proto, self.node, self.dir, self.file)

    def copy(self):
        """No argument. Return a copy of this object.
        """
        return copy.deepcopy(self)

def mpath(path):
    """Converts a POSIX path to an equivalent Macintosh path.

    Works for ./x ../x /x and bare pathnames.
    Won't work for '../../style/paths'. I'm not sure the Mac
    has such a concept.

    Also will expand environment variables and Cshell tilde
    notation if running on a POSIX platform.
    """
    import os
    if os.name == 'mac' : #I'm on a Mac
        if path[:3] == '../': #parent
            mp = '::'
            path = path[3:]
        elif path[:2] == './': #relative
            mp = ':'
            path = path[2:]
        elif path[0] == '/': #absolute
            mp = ''
            path = path[1:]
        else: # bare relative
            mp = ':'
        pl = string.split(path, '/')
        mp = mp + string.join(pl, ':')
        return mp
    elif os.name == 'posix': # Expand Unix variables
        if path[0] == '~' :
            path = os.path.expanduser( path )
        if '$' in path:
            path = os.path.expandvars( path )
        return path
    else: # needs to take care of dos & nt someday
        return path

#_realopen = open  #If I do a lot of mpath I can overload 'open'
#def open(filename, mode = 'r', bufsize = -1):
#    return _realopen( mpath(filename), mode, bufsize )

def relpath(path1, path2):
    """Return the relative path from directory 'path1' to directory 'path2'

    Both arguments are assumed to be directory names as there is no
    way to really distinguish a file from a directory by names
    alone. To loosen this restriction one can either assume that both
    arguments represent files or directories currently extant so that
    they can be tested, or add extra arguments to flag the path types
    (file or directory).

    I chose to impose this restriction because I will use this function
    in places where the pathnames are for files yet to be created.
    """
    common = os.path.commonprefix([path1, path2])
    sliceoff = len(common)
    path1 = path1[sliceoff:]
    path2 = path2[sliceoff:]

    dirs1 = string.split(path1, os.sep) # list of directory components below
                                        # the common path
    dirs1 = filter(lambda x: x, dirs1)  # filter out empty elements
    rel = (os.pardir+os.sep)*len(dirs1) # construct the relative path to the
                                        # common point
    return rel+path2


#################
# CLASS LIBRARY #
#################
class Document:
    """Primary container class for an HTML document.

    Single optional string argument for the path to a resource file
    used to specify document parameters. This helps minimize the need
    for subclassing from this class. Keyword parameters may be used
    for any of the following class attributes. See *HTMLtest.py* for
    example usage.

    Class instance attributes and keyword arguments
    
        base -- object of the Base class
        meta -- object of the Meta class
        cgi  -- if non zero will issue a mime type of text/html
        logo -- ('filename', width, height)  All images are specified
                 with a tuple of string, int, int. If the size of the
                 graphic is unknown, use 0, 0.  This one is the little
                 graphic on the footer of each page.
        banner -- ('filename', width, height) Banner graphic at
                 the top of page. Can also be set to a string filename
                 or an Image object. Can be autosized if it's a GIF.
        title --  string to be used as the document title.
        subtitle -- string to be used as the document subtitle.
                 If non-nil, this string will be used for the doc title
                 instead of title.
        author -- String used in the copyright notice
        email -- Email address for feedback mailto: tag
        zone -- string used to label the time zone if datetime
                 is used. By default not used.
        bgcolor -- Color string (can use variables from
                 HTMLcolors.py)
        background -- string filename of a graphic used as the
                 doc background.
        textcolor -- Color string used for text.  (can use
                 variables from HTMLcolors.py)
        linkcolor -- Color string used for hyperlinked text. 
        vlinkcolor -- Color string used for visited hypertext.
        alinkcolor -- Color string used for active hypertext.
        place_nav_buttons -- Flag to enable/disable the use of
                 navigation buttons.
                 Default is on. Set to 0 to disable.
        blank -- Image tuple for the transparent spacer gif
        prev -- Image tuple for the Previous Page button
        next -- Image tuple for the Next Page button
        top -- Image tuple for the Top of Manual button
        home -- Image tuple for the site Home Page button
        goprev -- URL string for the prev button
        gonext -- URL string for the next button
        gotop  -- URL string for the top button
        gohome -- URL string for the home button
        scripts -- a single or list of Script objects to be included in the <HEAD>
        onLoad -- Script, which is executed when the document is loaded
        onUnload -- Script, which is executed when the document is unloaded
    """
    
    def __init__(self, resource='', **kw):
        self.contents = []
        self.base = None
        self.meta = None
        self.cgi = None
        self.printecho = None
        self.logo = ('/image/logo.gif', 36, 35)
        self.banner = ('/image/banner.gif', 472, 30)
        self.title = ''
        self.subtitle = ''
        self.author = 'Micky Mouse'
        self.email = 'micky@disney.com'
        self.zone = ' Central US'
        self.datetime = time.ctime(time.time()) + self.zone
        self.date = regsub.sub('[0-9]+:[0-9]+:[0-9]+ ', '',
                               time.ctime(time.time()))
        self.bgcolor = ''
        self.background = ''
        self.textcolor = ''
        self.linkcolor = ''
        self.vlinkcolor = ''
        self.alinkcolor = ''
        self.place_nav_buttons = 'yes'
        self.blank = ('../image/blank.gif', 71, 19)
        self.prev = ('../image/BTN_PrevPage.gif', 71, 19)
        self.next = ('../image/BTN_NextPage.gif', 71, 19)
        self.top = ('../image/BTN_ManualTop.gif', 74, 19)
        self.home = ('../image/BTN_HomePage.gif', 74, 19)
        self.goprev = '' # URLs for above navigation buttons
        self.gonext = ''
        self.gotop  = ''
        self.gohome = ''
        self.script = []
        self.onLoad = ''
        self.onUnload = ''
        self.server = ''
        self.server_root = ''
        self.myurl = ''
        # Read stuff from resource file into instance namespace
        if resource: execfile(mpath(resource), self.__dict__)
        # Overlay keyword parameter values
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError,\
                      `item`+' not a valid parameter of the Document class.'

    def __repr__(self):
        if self.cgi:
            mime = 'Content-Type: text/html\n\n'
            s = mime + DOCTYPE
        else:
            s = DOCTYPE
        s = s + str(Comment('This file generated using Python HTMLgen module.'))
        # build the HEAD and BODY tags
        s = s + self.htmlhead()
        # HEADER SECTION
        s = s + self.header()
        # DOCUMENT CONTENT SECTION and FOOTER added on
        bodystring = '%s\n' * len(self.contents)
        s = s + (bodystring % tuple(self.contents)) + self.footer()
        return s

    def htmlhead(self):
        """Generate the HEAD TITLE and BODY tags.
        """
        if self.subtitle: titlebar = self.subtitle
        else: titlebar = self.title
        s = '<HEAD>\n  <META NAME="GENERATOR" CONTENT="HTMLgen 1.1">\n\
        <TITLE>%s</TITLE>\n' % titlebar
        if self.meta: s = s + str(self.meta)
        if self.base: s = s + str(self.base)
        if self.script: # for javascripts
            if type(self.script) in (TupleType, ListType):
                for script in self.script:
                    s = s + str(script)
            else:
                s = s + str(self.script)
        s = s + '</HEAD>\n'
        s = s + '<BODY'
        if self.bgcolor:    s = s + ' BGCOLOR="%s"' % self.bgcolor
        if self.background: s = s + ' BACKGROUND="%s"' % self.background
        if self.textcolor:  s = s + ' TEXT="%s"' % self.textcolor
        if self.linkcolor:  s = s + ' LINK="%s"' % self.linkcolor
        if self.vlinkcolor: s = s + ' VLINK="%s"' % self.vlinkcolor
        if self.alinkcolor: s = s + ' ALINK="%s"' % self.alinkcolor
        if self.onLoad:     s = s + ' onLoad="%s"' % self.onLoad
        if self.onUnload:   s = s + ' onUnload="%s"' % self.onUnload
        s = s + '>\n'
        return s
        
    def header(self):
        """Generate the standard header markups.
        """
        # HEADER SECTION - overload this if you don't like mine.
        s = ''
        if self.banner:
            bannertype = type(self.banner)
            if bannertype in (TupleType, StringType):
                s = str(Image(self.banner, border=0)) + '<BR>\n'
            elif bannertype == InstanceType:
                s = str(self.banner) + '<BR>\n'
            else:
                raise TypeError, 'banner must be either a tuple, instance, or string.'
        if self.place_nav_buttons:
            s = s + self.nav_buttons()
        s = s + str(Heading(3,self.title))
        if self.subtitle:
            s = s + '<H2>%s</H2>\n' % self.subtitle
        s = s + '<HR>\n\n'
        return s

    def footer(self):
        """Generate the standard footer markups.
        """
        # FOOTER SECTION - overload this if you don't like mine.
        s =  '\n<P><HR>\n'
        if self.place_nav_buttons:
            s = s + self.nav_buttons()
        s = s + '<BR>' + str(Image(self.logo, align='bottom'))
        s = s + '\n<FONT SIZE="-1"><P>Copyright &#169 %s<BR>All Rights Reserved<BR>\n' \
            % self.author
        s = s + '\nComments to author: ' + `MailTo(self.email)` 
        s = s + '<br>\nGenerated: %s <BR>' % self.date # can use self.datetime here instead
        s = s + '<hr>' + self.myurl
        s = s + '\n</FONT> </BODY> </HTML>'
        return s

    def nav_buttons(self):
        """Generate hyperlinked navigation buttons.

        If a self.go* attribute is null that corresponding button is
        replaced with a transparent gif to properly space the remaining
        buttons.
        """
        s = ''
        if self.goprev: # place an image button for previous page
            btn = Image(self.prev, border=0, alt='Previous')
            link = Href(self.goprev, str(btn))
            s = s + str(link) + ' \n'
        else: # place a blank gif as spacer
            btn = Image(self.blank)
            s = s + str(btn) + ' \n'
        if self.gonext: # place an image button for next page
            btn = Image(self.next, border=0, alt='Next')
            link = Href(self.gonext, str(btn))
            s = s + str(link) + ' \n'
        else: # place a blank gif as spacer
            btn = Image(self.blank)
            s = s + str(btn) + ' \n'
        if self.gotop: # place an image button for top of manual page
            btn = Image(self.top, border=0, alt='Top of Manual')
            link = Href(self.gotop, str(btn))
            s = s + str(link) + ' \n'
        else: # place a blank gif as spacer
            btn = Image(self.blank)
            s = s + str(btn) + ' \n'
        if self.gohome: # place an image button for site home page
            btn = Image(self.home, border=0, alt='Home Page')
            link = Href(self.gohome, str(btn))
            s = s + str(link) + ' \n'
        else: # place a blank gif as spacer
            btn = Image(self.blank)
            s = s + str(btn) + ' \n'
        return s

    def append(self, *items):
        """Add content to the Document object.
        
        Arg *items* can be plain text or objects; multiple arguments supported.
        """
        for item in items:
            self.contents.append(item)

    def prepend(self, *items):
        """Add content to the beginning of the Document object.
        
        Arg *items* can be plain text or objects; multiple arguments supported.
        """
        for item in items:
            self.contents.insert(0, item)

    def copy(self):
        """Return a complete copy of the current Document object.
        """
        return copy.deepcopy(self)

    def write(self, filename = None):
        """Emit the Document html into file.
        
        In Unix you can use environment variables in filenames.
        Will print to stdout if no argument.
        """
        if filename:
            f = open(mpath(filename), 'w')
        else:
            import sys
            f = sys.stdout
        f.write(str(self))
        f.close()
        if PRINTECHO and filename: print 'wrote: "'+filename+'"'


class MinimalDocument(Document):
    """A Document without all the header and footer stuff.
    
    Can be given a resource file as in Document.
    Uses the following attributes in the same way as Document:
    title, subtitle, meta, base, bgcolor, background, textcolor,
    linkcolor, vlinkcolor, cgi.   *All others ignored.*
    """
    def __repr__(self):
        if self.cgi:
            s = 'Content-Type: text/html\n\n' + DOCTYPE
        else:
            s = DOCTYPE
        s = s + str(Comment('This file generated using the Python HTMLgen module.'))
        s = s + self.htmlhead()
        # DOCUMENT CONTENT SECTION
        for object in self.contents:
            s = s + str(object)
        s = s + '\n </BODY> </HTML>'
        return s

class FramesetDocument(Document):
    """A minimal document suitable for entering Framesets.

    Arguments are for contents **NOT** a document resource file.

    Keyword Parameters
    
        title -- string to be used as the document title.
        base  -- object of the Base class
        meta  -- object of the Meta class
        cgi   -- if non zero will issue a mime type of text/html
        scripts -- a single or list of Script objects to be included in the <HEAD>
    
    No <body> markup. Instead add Frameset(s) with the constructor or
    append method.  Useful methods are *append*, *prepend*, *write*,
    and *copy*. **Others inherited from Document class are unused.**
    """
    def __init__(self, *contents, **kw):
        self.contents = map(None, contents)
        self.meta = None
        self.base = None
        self.title = ''
        self.cgi = 0
        self.script = []
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError,\
                      `item`+' not a valid parameter of the Document class.'

    def __repr__(self):
        if self.cgi:
            mime = 'Content-Type: text/html\n\n'
            s = mime + DOCTYPE
        else:
            s = DOCTYPE
        s = s + `Comment('This file generated with Python HTMLgen module.')`
        s = s + '<HEAD>\n<TITLE>%s</TITLE>\n' % self.title
        if self.meta: s = s + str(self.meta)
        if self.base: s = s + str(self.base)
        if self.script: # for javascripts
            if type(self.script) in (TupleType, ListType):
                for script in self.script:
                    s = s + str(script)
            else:
                s = s + str(self.script)
        s = s + '</HEAD>\n'
        for item in self.contents:
            s = s + str(item)
        s = s + '</HTML>'
        return s
        
        
class Meta:
    """Set document Meta-information.

    The META element is used within the HEAD element to embed
    document meta-information not defined by other HTML elements.
    
    Keywords supported
 
        name  -- NAME element attribute (default: 'keywords')
        equiv  -- will map to the HTTP-EQUIV attribute
        content -- mandatory attribute (default: 'python,HTMLgen')
        url -- URL naturally
    
    Example:

        Meta( name='keywords', content='eggs,spam,beans' )
    """
    def __init__(self, **kw):
        self.equiv = 'keywords'
        self.name  = ''
        self.content = 'python,HTMLgen'
        self.url = ''
        for item in kw.keys():
            self.__dict__[item] = kw[item]

    def __repr__(self):
        s = '<META'
        if self.equiv: s = s + ' HTTP-EQUIV="%s"' % self.equiv
        if self.name:  s = s + ' NAME="%s"' % self.name
        if self.content: s = s + ' CONTENT="%s"' % self.content
        if self.url: s = s + ' URL="%s"' % self.url
        s = s + '>\n'
        return s

class Base:
    """Set the the absolute URL base to be used for relative URL links.

    One string argument required. It must be a complete file name, and
    is usually the original URL of this document.  If this file is
    moved, having the BASE set to the original URL eliminates the need
    to also move all the documents which are identified by relative
    URL links in this document.
    """
    def __init__(self, url=''):
        self.url = url

    def __repr__(self):
        return '<BASE HREF="%s">\n' % self.url


##### Client-side Imagemap Support #####

class Map:
    """Used to name and describe a client-side image map.

    The *areas* argument is a list of Area objects.
    Keyword arg is supported for *name*, which defines the map name
    to be used with the usemap attribute of an Image class instance.
    """
    def __init__(self, areas = None, **kw):
        self.areas = areas or []
        self.name = ''
        for item in kw.keys():
            self.__dict__[item] = kw[item]

    def __repr__(self):
        s = '\n<MAP NAME="%s">\n' % self.name
        for area in self.areas:
            s = s + str(area)
        s = s + '</MAP>\n'
        return s

class Area:
    """Specify a click-sensitive area of an image.

    The area is linked to a HREF specified by the *href* attribute.
    The *coords* attribute is required and describes the position of
    an area (in pixels) of the image in comma-separated x,y
    coordinates where the upper-left corner is "0,0". For shape='rect'
    (the default), it is "left,top,right,bottom". For shape='circle',
    it is "center_x,center_y,radius". For shape='polygon', it is
    successive x,y vertices of the polygon. If the first and last
    coordinates are not the same, then a segment is inferred to close
    the polygon. If no *href* keyword is given a *NOHREF* will be
    generated indicating that this region should generate no links.
    
    Keyword Arguments
    
        href --  Typically a reference to an image
        coords --  string holding a list of coordinates defining
        shape  -- 'rect'|'circle'|'polygon'
    """
    
    def __init__(self, **kw):
        self.shape = 'RECT'
        self.coords = ''
        self.href = ''
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Area class.'

    def __repr__(self):
        if not self.coords:
            raise AttributeError, 'Area object requires coords attribute.'
        s = '<AREA SHAPE="%s" COORDS="%s"' % (self.shape, self.coords)
        if self.href: s = s + ' HREF="%s"' % self.href
        else: s = s + ' NOHREF'
        s = s + '>\n'
        return s

###### FRAME SUPPORT ######

class Frameset:
    """Define a FRAMESET.

    Framesets can contain either Frames or other Framesets.

    Keywords/Attributes
    
        rows -- is a string like "20%,*,20%" stating the number and widths of
            rows defined for the frames. Widths for each row can be expressed in
            integer (absolute pixels), percentage (of overall browser window or
            containing frame), or asterisk(*) to indicate an auto-resized remainder
            width.
        cols -- is a string of the same format as above except applied to column
            widths. There should not be both a rows and cols attribute in the same
            Frameset tag.
        frame_warning -- optional flag is available to indicate if a <NOFRAMES>
            statement should be included with the Frameset to alert browsers without
            frame support. Default is 1 (yes).
        onLoad -- is a string of script code, which is executed when the frameset
            is loaded
        onUnload -- is a string of script code, which is executed when the frameset
            is unloaded
    """
    def __init__(self, *contents, **kw):
        """contents is a series of Frame objects, key word arguments supported.
        """
        self.rows = ''
        self.cols = ''
        self.contents = []
        self.frame_warning = 1
        self.onLoad = ''
        self.onUnload = ''
        if contents: apply(self.append, contents)
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Frameset class.'
        if self.rows and self.cols:
            raise AttributeError, "Can't use both rows and cols in a Frameset."

    def append(self, *items):
        """Add Frames to the Frameset.

        *items* can be one or more Frame object.
        """
        for item in items:
            self.contents.append(item)

    def __repr__(self):
        s = '\n<FRAMESET'
        if self.rows: s = s + ' ROWS="%s"' % self.rows
        if self.cols: s = s + ' COLS="%s"' % self.cols
        if self.onLoad: s = s + ' onLoad="%s"' % self.onLoad
        if self.onUnload: s = s + ' onUnload="%s"' % self.onUnload
        s = s + '>\n'
        if self.frame_warning:
            s = s + """<NOFRAMES>
            <H2 align=center>Frame ALERT!</h2>
            <p>
            This document is designed to be viewed using <b>Netscape</b>'s
            Frame features. If you are seeing this message, you are using
            a frame challenged browser.
            </p>
            <p>
            A <b>Frame-capable</b> browser can be gotten from
            <a href="http://home.netscape.com/">Netscape Communications</a>.
            </p>
            </NOFRAMES>
            """
            # I'll add microsoft.com when IE supports Frames RSN.
        for item in self.contents:
            s = s + str(item)
        s = s + '\n</FRAMESET>\n'
        return s

class Frame:
    """Define the characteristics of an individual frame.

    Keywords Arguments

        src  -- is a HREF which points to the initial contents of the frame.
        name -- is the window name used by others to direct content into this frame.
        marginwidth -- is the number of pixels used to pad the left and right
               sides of the frame.
        marginheight -- is the number of pixels used to pad the top and bottom
               sides of the frame.
        scrolling -- is used to indicate scrolling policy set to 'yes'|'no'|'auto'
        noresize -- is a flag which instructs the browser to disallow frame resizing. 
               set to non zero lock size ( noresize=1 ).
    """
    def __init__(self, **kw):
        """keyword arguments are supported.
        """
        self.src = ''
        self.name = ''
        self.marginwidth = 0
        self.marginheight = 0
        self.scrolling = None
        self.noresize = None
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Frameset class.'

    def __repr__(self):
        s = '   <FRAME'
        if self.src: s = s + ' SRC="%s"' % self.src
        if self.name: s = s + ' NAME="%s"' % self.name
        if self.marginwidth: s = s + ' MARGINWIDTH=%s' % self.marginwidth
        if self.marginheight: s = s + ' MARGINHEIGHT=%s' % self.marginheight
        if self.scrolling: s = s + ' SCROLLING="%s"' % self.scrolling
        if self.noresize: s = s + ' NORESIZE'
        s = s + '>\n'
        return s


class Href:
    """Generate a hyperlink.

    Argument 1 is the URL and argument 2 is the hyperlink text.

    Keyword arguments

        target -- is an optional target symbol 
        onClick --  is the script-code which is executed when link is clicked.
        onMouseOver -- is the script-code which is executed when the mouse
                       moves of the link.
    """
    def __init__(self, url='', text='', **kw):
        self.target = None
        self.onClick = None
        self.onMouseOver = None
        self.url = url
        self.text = text
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter for this class.'

    def __repr__(self):
        s = '<A HREF="%s"' % self.url
        if self.target: s = s + ' TARGET="%s"' % self.target
        if self.onClick: s = s + ' onClick="%s"' % self.onClick
        if self.onMouseOver: s = s + ' onMouseOver="%s"' % self.onMouseOver
        s = s + '>%s</A>' % self.text
        return s

    def append(self, content):
        self.text = self.text + str(content)
        

A = HREF = Href # alias

class Name(Href):
    """Generate a named anchor.

    Arg *url* is a string or URL object,
    Arg *text* is optional string or object to be highlighted as the anchor.
    """
    def __repr__(self):
        s = '<A NAME="%s">%s</A>' % (self.url, self.text)
        return s

NAME = Name # alias

class MailTo:
    """A Mailto href

    First argument is an email address, optional second argument is
    the text shown as the underlined hyperlink. Default is the email
    address.
    """
    def __init__(self, address='', text=None):
        self.address = address
        self.text = text or address

    def __repr__(self):
        return '<A HREF="mailto:%s">%s</A>' % (self.address, self.text)

MAILTO = Mailto = MailTo

# Inline Images
class Image:
    """Inlined Image

    The *filename* argument is a filename, or URL of a graphic image,
    or a triple of ( filename, width, height ) where dimensions are in
    pixels. Where the filename is found to be a valid pathname to an
    existing GIF file that file will be read to determine its width and
    height properties. 
    
    Keyword Arguments
    
        width  -- (int) Width in pixels
        height -- (int) Height in pixels
        border -- (int) Border width in pixels
        align  -- (string) 'top'|'middle'|'bottom'|'right'|'left'
        alt    -- (string) Text to substitute for the image in nonGUI browsers
        usemap -- Imagemap name or Map object
        ismap  -- Flag indicating if a server side imagemap is available.
        absolute -- Absolute path to the directory containing the image
        prefix -- Relative path or URL to directory containing the image
    """
    def __init__(self, filename='', **kw):
        self.prefix = None
        self.absolute = None
        self.filename = filename
        self.width = None
        self.height = None
        self.border = None
        self.align = None
        self.alt = None
        self.ismap = None
        self.usemap = None
        for item in kw.keys():
            self.__dict__[item] = kw[item]
        # unpack the tuple if needed
        if type(self.filename) == TupleType:
            self.width = self.filename[1]
            self.height = self.filename[2]
            self.filename = self.filename[0]
        # if the file is there test it to get size of GIF
        if self.filename and not self.width:
            try:
                self.width, self.height = getgifsize(filename)
            except (IOError, TypeError):
                pass

    def calc_rel_path(self, from_dir=None):
        """Calculate the relative path from 'from_dir' to the
        absolute location of the image file.

        Sets self.prefix.
        """
        if not from_dir:
            from_dir = os.getcwd()
        if self.absolute:
            self.prefix = relpath(from_dir, self.absolute)
        
    def __repr__(self):
        if self.prefix:
            fullname = os.path.join(self.prefix, self.filename)
        else:
            fullname = self.filename
        s = '<IMG SRC="%s"' % fullname
        if self.width:  s = s + ' WIDTH=%s' % self.width
        if self.height: s = s + ' HEIGHT=%s' % self.height
        if type(self.border)==IntType: s = s + ' BORDER=%s' % self.border
        if self.align: s = s + ' ALIGN=%s' % self.align
        if self.alt:
            s = s + ' ALT="%s"' % self.alt
        else:
            s = s + ' ALT="%s"' % os.path.basename(self.filename)
        if self.usemap:
            if type(self.usemap) == StringType:
                # Normally it's a string with a leading # sign
                s = s + ' USEMAP="%s"' % self.usemap
            elif type(self.usemap) == InstanceType:
                # can use a Map instance for this
                try:
                    s = s + ' USEMAP="#%s"' % self.usemap.name
                except:
                    pass
        if self.ismap: s = s + ' ISMAP'
        s = s + '>'
        return s

IMG = Image # alias

# Headings
class Heading:
    """Heading markups for H1 - H6

    The *level* arg is an integer for the level of the heading.
    Valid levels are 1-6.
    The *text* arg is a string (or any object) for the text of the heading.
    """
    def __init__(self, level=1, text=''):
        if level not in (1,2,3,4,5,6):
            raise ValueError, `level`+' is not a valid heading level'
        self.level = level
        if type(text) == StringType: text = escape(text)
        self.text = str(text)

    def __repr__(self):
        s = '<H%s>%s</H%s>\n' % (self.level, self.text, self.level)
        return s

    def append(self, text):
        """Add text onto the end of the Heading object.
        """
        if type(text) == StringType: text = escape(text)
        self.text = self.text + str(text)

H = Head = Header = Heading # Aliases

# Paragraph blocks
class Paragraph:
    """Define a Paragraph.

    Takes a single string/object argument and the optional
    keyword argument 'align' which may be one of (left, right,
    center).  **Not to be confused with class P**. That is
    just for inserting a para break.

    Example:
    
        Paragraph('Some text to center', align='center')
    """
    def __init__(self, text='', **kw):
        self.align = ''
        self.contents = []
        if type(text) == StringType: text = escape(text)
        self.contents.append(text)
        if kw.has_key('align'): self.align = kw['align']

    def append(self, text):
        """Adds text (or any object) onto the end of object."""
        if type(text) == StringType: text = escape(text)
        self.contents.append(text)

    def __repr__(self):
        s = '\n<P'
        if self.align: s = s + ' ALIGN=%s' % self.align
        s = s + '>'
        for item in self.contents:
            s = s + str(item)
        s = s + '</P>\n'
        return s

    def markup(self, rex= None, classobj=None, kw=None):
        """Markup the text with a given regex with a given tag class.

        Arguments

            rex -- a regular expression object or string which will be used
                to match all text patterns in the Paragraph body.
            classobj -- a class object to which the found text will be sent for
                wrapping.
            kw -- Optional dictionary of keyword parameter mappings sent
                along to the class to tailor the instance.
        
        **[EXPERIMENTAL]**
        """
        #the pattern used to find parenthetical text
        self.text = ''
        for item in self.contents:
            self.text = self.text + str(item)
        if not rex: rex = regex.compile('([^)]*)')
        if not classobj: classobj = Emphasis
        if not kw: kw = {}
        if type(rex) == StringType:
            rex = regex.compile(rex)
        endpoints = [(0,0)]  #start off the list of slices with 0
        output = []
        i = 0
        while 1:
            # build up a list of tuples each containing the
            # endpoints of the found parenthetic text
            if rex.search(self.text, i) > -1:
                endpoints.append(rex.regs[0])
                i = rex.regs[0][1]
            else:
                break
        if len(endpoints) == 1: return 0# didn't find any matches
        # tack on a ending slice
        endpoints.append( ( len(self.text)-1 , len(self.text)-1 ) )
        length = len(endpoints)
        for i in range(1, length-1):
            # first take the text before the paren starts
            # and send it unchanged to the output list
            a , b = endpoints[i-1][1] , endpoints[i][0]
            output.append(self.text[a:b])
            # next take the paren slice itself and wrap
            # it in the markup class
            a , b = endpoints[i][0] , endpoints[i][1]
            output.append( str(apply(classobj,(self.text[a:b],),kw)) )
        # the loop didn't get the last stretch of plain text
        # so this finishes up
        a , b = endpoints[i][1], endpoints[i+1][0] + 1
        output.append(self.text[a:b])
        # rejoin the list and set it to the internal text
        self.text = string.join(output, '')
        self.contents = [self.text]
        return length - 2 #return the number of items found

Para = Paragraph # Alias

class P:
    """Just echo a <P> tag"""
    
    def __repr__(self):
        return '\n<P>\n'

# List constructs

class List(UserList.UserList):
    """Will generate a bulleted list given a list arg.

    Supports nested lists, i.e. lists of lists. Each
    time a list is encountered in a list it will indent
    those contents w.r.t. the prior list entry. This
    can continue indefinitely through nested lists
    although there are only three different bullets
    provided by the browser (typically).
    
    Optional keyword *indent* can be used to indicate
    whether you want the list to start left justified or
    indented. *indent=0* will make it left justified. The
    default is to indent however.

    Optional keyword *type* can be set to either disk, circle, or
    square to specify what kind of symbol is used for each list item's
    bullet. (Netscape extension)
    
    Since we inherit from the UserList class any normal
    list operations work on instances of this class.
    Any list contents will do. Each of the items will be
    emitted in html if they are themselves objects from
    this module.  Aliases: UL, BulletList
    """
    I_am_a_list = 1
    tagname = 'UL'
    attrs = ('type','align')
    flags = ('compact')
    pad = '    '
    indent = 1
    def __init__(self, list = None, **kw):
        self.data = []
        self.lvl = 0
        if list:
            if type(list) == type(self.data):
                self.data[:] = list
            else:
                self.data[:] = list.data[:]
        for item in kw.keys():
            self.__dict__[string.lower(item)] = kw[item]

    def __repr__(self):
        self.firstitem = 1
        self.s = ''

        if self.indent:
            self.s = self.pad*self.lvl + self.start_element()
        for item in self.data: #start processing main list
            itemtype = type(item)
            if itemtype == InstanceType: 
                try: # in case it's a nested list object
                    if item.I_am_a_list:
                        itemtype = ListType
                except AttributeError:
                    pass
            if itemtype == ListType: #process the sub list
                self.sub_list(item)
            else:
                self.s = self.s + self.render_list_item(item)

        if self.indent: #close out this level of list
            self.s = self.s + self.pad*self.lvl + self.end_element()
        self.lvl = 0
        return self.s

    def sub_list(self, list):
        """Recursive method for generating a subordinate list
        """
        self.lvl = self.lvl + 1
        if type(list) == InstanceType:
            try:
                if list.I_am_a_list: #render the List object
                    list.lvl = self.lvl
                    self.s = self.s + str(list)
            except AttributeError:
                pass
        else:
            self.s = self.s + self.pad*self.lvl + self.start_element()
            for item in list:
                itemtype = type(item)
                if itemtype == InstanceType:
                    try: #could be another nested List child object
                        if item.I_am_a_list:
                            itemtype = ListType
                    except AttributeError:
                        pass
                if itemtype == ListType:
                    self.sub_list(item) #recurse for sub lists
                else: # or just render it
                    self.s = self.s + self.render_list_item(item)
            # close out this list level
            self.s = self.s + self.pad*self.lvl + self.end_element()
        self.lvl = self.lvl - 1 #decrement indentation level

    def render_list_item(self, item):
        """Renders the individual list items

        Overloaded by child classes to represent other list styles.
        """
        return '%s<LI>%s\n' % (self.pad*self.lvl, item)

    def start_element(self):
        """Generic creator for the HTML element opening tag.

        Reads tagname, attrs and flags to return appropriate tag.
        """
        s = '<' + self.tagname
        for attr in self.attrs:
            try:
                s = s + ' %s="%s"' % (attr, getattr(self, attr))
            except AttributeError:
                pass
        for flag in self.flags:
            try:
                x = getattr(self, flag)
                s = s + ' %s' % flag
            except AttributeError:
                pass
        return s + '>\n'

    def end_element(self):
        """Closes the HTML element
        """
        return '</%s>\n' % self.tagname

    def append(self, *items):
        """Append entries to the end of the list
        """
        for item in items:
            self.data.append(item)
    
UL = BulletList = List  #Aliases

class OrderedList(List):
    """Will generate a numbered list given a list arg.

    Optional keyword *type* can be used to specify whether you want
    the list items marked with: capital letters (type='A'), small
    letters (type='a'), large Roman numerals (type='I'), small Roman
    numerals (type='i'). The default is arabic numbers. The other
    types are HTML3.2 only and may not be supported by browsers yet.
    Any list contents will do. Each of the items will be emitted
    in HTML if they are themselves objects.
    """
    tagname = 'OL'
    attrs = ('type',)

OL = NumberedList = OrderedList

class DefinitionList(List):
    """Show a series of items and item definitions.

    Arg is a list of tuple pairs:
    [(string/object,string/object),(,)...]  1st item in each pair is
    the word to be defined. It will be rendered in bold. 2nd is the
    string which will be indented to it's next-line-right. If the
    *compact* flag is set to non-empty, the definition side will be
    placed on the same line.  Example

        DefinitionList([( 4 , 'Number after 3') , ( 1 , 'Unity')] ) will emit:
        4
            Number after 3
        1
            Unity
    """
    tagname = 'DL'
    attrs = ()
    flags = ('compact',)
    def render_list_item(self, item):
        """Overload method to perform DT/DD markup.
        """
        return '%s<DT><B>%s</B><DD>%s\n' % (self.pad*self.lvl, item[0], item[1])

DL = DefinitionList

class ImageBulletList(List):
    """Show a list of images with adjoining text(or object).

    Arg is a list of tuple pairs: [(Image_obj, string/object),(,)...]
    Generates an inlined image then the text followed by a <BR>
    for each element.
    """
    tagname = 'UL'
    attrs = ()
    flags = ()
    def render_list_item(self, item):
        """Overload method to take first item from an item tuple and
        setting it next to the second item, using BR to separate list items.
        """
        return '%s%s %s<BR>\n' % (self.pad*self.lvl, item[0], item[1])

class NonBulletList(List):
    """Generate a raw indented list without bullet symbols.

    Arg is a list of python objects:
    """
    tagname = 'UL'
    attrs = ()
    flags = ()
    def render_list_item(self, item):
        """Overload method to take first item from an item tuple and
        setting it next to the second item, using BR to separate list items.
        """
        return '%s%s<BR>\n' % (self.pad*self.lvl, item)


####### FORM TAGS ########

class Form:
    """Define a user filled form. Uses POST method.
   
    *cgi* is the URL to the CGI processing program.  Input objects
    (any others as well) are appended to this container widget.
    
    Keywords
    
        name -- name of the form
        submit -- flag indicating if a Submit button should automatically
                  be appended to the form.
        reset  -- flag indicating if a Reset button should automatically
                  be appended to the form.
        target -- set a TARGET attribute
        enctype -- specify an Encoding type.
        onSubmit -- script, which is executed, when the form is submitted
    """
    def __init__(self, cgi = None, **kw):
        self.contents = []
        self.cgi = cgi
        self.submit = None
        self.reset = None
        self.target = None
        self.enctype = None
        self.name = None
        self.onSubmit = ''
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Form class.'

    def append(self, *items):
        """Append any number of items to the form container.
        """
        for item in items:
            self.contents.append(item)

    def __repr__(self):
        if not self.submit:
            self.contents.append(Input(type='submit', name='SubmitButton',value='Send'))
        else:
            self.contents.append(self.submit)
        if self.reset:
            self.contents.append(self.reset)

        s = '\n<FORM METHOD="POST"'
        if self.cgi: s = s + ' ACTION="%s"' % self.cgi
        if self.enctype: s = s + ' ENCTYPE="%s"' % self.enctype
        if self.target: s = s + ' TARGET="%s"' % self.target
        if self.name: s = s + ' NAME="%s"' % self.name
        if self.onSubmit: s = s + ' onSubmit="%s"' % self.onSubmit
        s = s + '>\n'
        for item in self.contents:
            s = s + str(item)
        s = s + '\n</FORM>\n'
        return s

class Input:
    """General Form Input tags.

    Keyword Arguments

        type -- 'TEXT' (default) Supported types include password, checkbox,
                      radio, file, submit, reset, hidden.
        name -- provides the datum name
        value -- the initial value of the input item
        checked --  flag indicating if the item is checked initially
        size -- size of the widget (e.g. size=10 for a text widget is it's width)
        maxlength -- maximum number of characters accepted by the textfield.
        llabel  --  an optional string set to the left of the widget
        rlabel  --  an optional string set to the right of the widget
        onBlur -- script, which is executed, when the field loses focus,
                  useful for the text-type 
        onChange -- script, which is executed, when the field value changed,
                    useful for the text-type
        onClick -- script, which is executed, when the field in clicked,
                   useful for the button, checkbox, radio, submit, reset type
        onFocus -- script, which is executed, when the field receives focus,
                   useful for the text-type
        onSelect -- script, which is executed, when part of the field 
                    is selected, useful for the text-type
    """
    re_type = regex.compile('text\|password\|checkbox\|radio\|file\|submit\|reset\|hidden',
                            regex.casefold)
    def __init__(self, **kw):
        self.type = 'TEXT'
        self.name = 'Default_Name'
        self.value= ''
        self.checked = ''
        self.size = 0
        self.maxlength = 0
        self.llabel = ''
        self.rlabel = ''
        self.onBlur = ''
        self.onChange = ''
        self.onClick = ''
        self.onFocus = ''
        self.onSelect = ''
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Input class.'
        if Input.re_type.search(self.type) < 0:
            raise KeyError, `self.type`+' not a valid type of Input class.'

    def __repr__(self):
        s = ''
        if self.llabel: s = str(self.llabel)
        s = s + '<INPUT '
        if self.type: s = s + 'TYPE="%s" ' % self.type
        if self.name: s = s + 'NAME="%s" ' % self.name
        if self.value: s = s + 'VALUE="%s" ' % self.value
        if self.checked: s = s + 'CHECKED '
        if self.size: s = s + 'SIZE=%s ' % self.size
        if self.maxlength: s = s + 'MAXLENGTH=%s ' % self.maxlength
        if self.onBlur: s = s + 'onBlur="%s" ' %self.onBlur
        if self.onChange: s = s + 'onChange="%s" ' %self.onChange
        if self.onClick: s = s + 'onClick="%s" ' %self.onClick
        if self.onFocus: s = s + 'onFocus="%s" ' %self.onFocus
        if self.onSelect: s = s + 'onSelect="%s" ' %self.onSelect
        s = s + '>\n'
        if self.rlabel: s = s + str(self.rlabel)
        return s


class Select(UserList.UserList):
    """Used to define a list widget or option widget.
    
    Pass a list of strings to show a list with those values. Alternatively
    can pass a list of tuple pairs. Each pair contains the displayed string
    and it's associatated value mapping. If no value mapping is needed just
    use something that evaluates to None.

    Keyword Arguments:
    
        name -- provides the datum name
        size -- the visual size. 1 means use an option popup widget. 
                               >=2 means use a list widget with that many lines.
        multiple -- flag to indicate whether multiple selections are supported.
        onBlur -- script, which is executed, when the field loses focus
        onChange -- script, which is executed, when the field value changed
        onFocus -- script, which is executed, when the field receives focus
    """
    def __init__(self, data=None, **kw):
        UserList.UserList.__init__(self, data)
        self.name = ''
        self.size = 1
        self.multiple = None
        self.selected = []
        self.onBlur = ''
        self.onChange = ''
        self.onFocus = ''
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Select class.'

    def __repr__(self):
        s = '<SELECT NAME="%s"' % self.name
        if self.size: s = s + ' SIZE=%s' % self.size
        if self.multiple: s = s + ' MULTIPLE'
        if self.onBlur: s = s + ' onBlur="%s"' % self.onBlur
        if self.onChange: s = s + ' onChange="%s"' % self.onChange
        if self.onFocus: s = s + ' onFocus="%s"' % self.onFocus
        s = s + '>\n'
        if type(self.data[0]) == TupleType:
            for item, value in self.data:
                s = s + '<OPTION'
                if value:
                    s = s + ' Value="%s"' % value
 		    if value in self.selected:
 		       s = s + ' SELECTED'
 		else:
 		    if item in self.selected:
 		       s = s + ' SELECTED'
                s = s + '>%s\n' % item
        else:
            for item in self.data:
                if item not in self.selected:
                    s = s + '<OPTION>%s\n' % item
                else:
                    s = s + '<OPTION SELECTED>%s\n' % item
        s = s + '</SELECT>\n'
        return s


class Textarea:
    """Used for an entry widget to type multi-line text (for forms).

    Keyword Arguments:

        rows -- sets the number of text rows. (default=4)
        cols -- sets the number of text columns. (default=40)
        onBlur -- script, which is executed, when the field loses focus
        onChange -- script, which is executed, when the field value changed
        onFocus -- script, which is executed, when the field receives focus
        onSelect -- script, which is executed, when part of the field 
                    is selected
    """
    def __init__(self, text='', **kw):
        self.text = text
        self.name = 'text_area'
        self.rows = 4
        self.cols = 40
        self.onBlur = ''
        self.onChange = ''
        self.onFocus = ''
        self.onSelect = ''
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Textarea class.'

    def __repr__(self):
        s = '<TEXTAREA NAME="%s" ROWS=%s COLS=%s' % (self.name, self.rows, self.cols)
        if self.onBlur: s = s + ' onBlur="%s"' % self.onBlur
        if self.onChange: s = s + ' onChange="%s"' % self.onChange
        if self.onFocus: s = s + ' onFocus="%s"' % self.onFocus
        if self.onSelect: s = s + ' onSelect="%s"' % self.onSelect
        s = s + '>'
        s = s + str(self.text)
        s = s + '</TEXTAREA>'
        return s

class Script:
    """Construct a Script

    Keyword Arguments

        Defaults in (parenthesis).  Keyword parameters may be set as attributes of 
        the instantiated script object as well.

        language -- specifies the language ('JavaScript')
        src -- specifies the location
        code -- script code, which is printed in comments, to hide it from non
                java-script browsers
    """
    def __init__(self, **kw):
        # Specify the default values
        self.language = 'JavaScript'
        self.src = ''
        self.code = ''
        # Now overlay the keyword arguments from caller
        for k in kw.keys():
            if self.__dict__.has_key(k):
                self.__dict__[k] = kw[k]
            else:
                print `k`, "isn't a valid parameter for this class."

    def __repr__(self):
        s = '<SCRIPT LANGUAGE="%s" ' % self.language
        if self.src: s = s + 'SRC="%s" ' % self.src
        s = s + '>'
        if self.code: s = s + '<!--\n%s\n//-->\n' % self.code
        s = s + '</SCRIPT>'
        return s


class Table:
    """Construct a Table with Python lists.

    Instantiate with a string argument for the table's name (caption).
    Set object.heading to a list of strings representing the column headings.
    Set object.body to a list of lists representing rows. **WARNING:** the body
    attribute will be edited to conform to html. If you don't want your
    data changed make a copy of this list and use that with the table object.

    Keyword Parameters

        Defaults in (parenthesis).  Keyword parameters may be set as attributes of the
        instantiated table object as well.

        caption_align -- 'top'|'bottom'  specifies the location of the table title ('top')
        border -- the width in pixels of the bevel effect around the table (2)
        cell_padding -- the distance between cell text and the cell boundary (4)
        cell_spacing -- the width of the cell borders themselves (1)
        width -- the width of the entire table wrt the current window width ('100%')
        colspan -- a list specifying the number of columns spanned by that heading
               index. e.g. t.colspan = [2,2] will place 2 headings spanning
               2 columns each (assuming the body has 4 columns).
        heading --  list of strings, the length of which determine the number of
                   columns.  ( ['&nbsp']*3 )
        heading_align -- 'center'|'left'|'right'
                        horizontally align text in the header row ('center')
        heading_valign --  'middle' |'top'|'bottom'
                        vertically align text in the header row ('middle')
        body -- a list of lists in row major order containing strings or objects
               to populate the body of the table. ( [['&nbsp']*3] )
        column1_align -- 'left'|'right'|'center'  text alignment of the first column
        cell_align --    'left'|'right'|'center'  text alignment for all other cells
        cell_line_breaks -- 1|0  flag to determine if newline char in body text will be
                  converted to <br> symbols; 1 they will, 0 they won't. (1)
        
    """
    def __init__(self, tabletitle='', **kw):
        """Arg1 is a string title for the table caption, optional keyword
        arguments follow.
        """
        # Specify the default values
        self.tabletitle = tabletitle
        self.caption_align = 'top'
        self.border = 2
        self.cell_padding = 4
        self.cell_spacing = 1
        self.width = '100%'
        self.heading = ['&nbsp']*3
        self.heading_align = 'center'
        self.heading_valign = 'middle'
        self.body = [['&nbsp']*3]
        self.column1_align = 'left'
        self.cell_align = 'left'
        self.cell_line_breaks = 1
        self.colspan = None
        # Now overlay the keyword arguments from caller
        for k in kw.keys():
            if self.__dict__.has_key(k):
                self.__dict__[k] = kw[k]
            else:
                print `k`, "isn't a valid parameter for this class."

    def __repr__(self):
        """Generates the html for the entire table.
        """
        if self.tabletitle:
           s = `Name(self.tabletitle)` + '\n<P>'
        else:
           s = ''

        s = s + '<TABLE border=%s cellpadding=%s cellspacing=%s width="%s">\n' % \
                (self.border, self.cell_padding, self.cell_spacing, self.width)
        if self.tabletitle:
            s = s + '<CAPTION align=%s><STRONG>%s</STRONG></CAPTION>\n' % \
                    (self.caption_align, self.tabletitle)
        #convert all body data to string
        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                if type(self.body[i][j]) == StringType:
                    self.body[i][j] = escape(self.body[i][j])
                    #process cell contents to insert breaks for \n char.
                    if self.cell_line_breaks:
                        self.body[i][j] = regsub.gsub('\n','<br>',string.strip(self.body[i][j]))
                else: #could be a markup object so just repr it
                    self.body[i][j] = str(self.body[i][j])
        # Initialize colspan property to 1 for each
        #  heading column if user doesn't provide it.
        if self.heading:
            if not self.colspan:
                if type(self.heading[0]) == ListType:
                    self.colspan = [1]*len(self.heading[0])
                else:
                    self.colspan = [1]*len(self.heading)
        # Construct heading spec
        #  can handle multi-row headings. colspan is a list specifying how many
        #  columns the i-th element should span. Spanning only applies to the first
        #  or only heading line.
        if self.heading:
            prefix = '<TR Align=' + self.heading_align + '> '
            postfix = '</TR>\n'
            middle = ''
            if type(self.heading[0]) == ListType:
                for i in range(len(self.heading[0])):
                    middle = middle + '<TH ColSpan=%s>' % self.colspan[i] + str(self.heading[0][i]) +'</TH>'
                s = s + prefix + middle + postfix
                for i in range(len(self.heading[1])):
                    middle = middle + '<TH>' + str(self.heading[i]) +'</TH>'
                for heading_row in self.heading[1:]:
                    for i in range(len(self.heading[1])):
                        middle = middle + '<TH>' + heading_row[i] +'</TH>'
                    s = s + prefix + middle + postfix
            else:
                for i in range(len(self.heading)):
                    middle = middle + '<TH ColSpan=%s>' % self.colspan[i] + str(self.heading[i]) +'</TH>'
                s = s + prefix + middle + postfix
        # construct the rows themselves
        for row in self.body:
            prefix = '<TR> <TD Align='+ self.column1_align + '>'
            postfix = '</TD> </TR>\n'
            infix = '</TD> <TD Align='+self.cell_align+'>'
            s = s + prefix + string.join(row, infix) + postfix
        #close table
        s = s + '</TABLE><P>\n'
        return s


class Tbase:
    "Abstract base class for the table tag markup classes."
    tagname = '' # to be provided by derived classes
    attrs = ()   # to be provided by derived classes
    flags = ()   # to be provided by derived classes

    def __init__(self, arg=None, **kw):
        self.arg = arg
        for item in kw.keys():
            self.__dict__[string.lower(item)] = kw[item]

    def start_tag(self):
        "Return start tag for this tag type including all attributes"
        s = '<' + self.tagname
        for attr in self.attrs:
            try:
                s = s + ' %s="%s"' % (attr, getattr(self, attr))
            except AttributeError:
                pass
        for flag in self.flags:
            try:
                x = getattr(self, flag)
                s = s + ' %s' % flag
            except AttributeError:
                pass
        return s + '>'

    def end_tag(self):
        "Return end tag for this tag type"
        return '</%s>' % self.tagname

    def __repr__(self):
        "default string for this markup"
        return self.start_tag() + str(self.arg) + self.end_tag()

class Container:
    """Generic base class providing methods associated with managing
    an object with a content list. Used by the TableLite class and friends.
    """
    def __init__(self, *args, **kw):
        self.contents = []
        for arg in args:
            self.contents.append(arg)
        for item in kw.keys():
            self.__dict__[string.lower(item)] = kw[item]

    def append(self, *items):
        """Append one or more items to the end of the container.
        """
        for item in items:
            self.contents.append(item)

    def prepend(self, *items):
        """Prepend one or more items to the top of the container.
        """
        for item in items:
            self.contents.insert(0, item)

    def empty(self):
        """Empty the contents of the container.
        """
        self.contents = []

    def length(self):
        """Return the integer length of the container list.
        """
        return len(self.contents)

    def last(self):
        """Return the last item in the container.
        """
        return self.contents[-1]

    def copy(self):
        """Return a full copy of the object.
        """
        return copy.deepcopy(self)

    def __add__(self, other):
        """Support self + list
        """
        if type(other)==type([]):
            self.contents = self.contents + other
            return self
        else:
            raise TypeError, 'can only add lists to this object'

    def __repr__(self):
        s = '\n' + self.start_tag()
        for item in self.contents:
            s = s + str(item)
        s = s + self.end_tag()
        return s

class Caption(Tbase):
    """Caption used to annotate the entire Table.

    Keywords Available

        align -- set to either top|bottom|left|right
    """
    tagname = 'CAPTION'
    attrs = ('align',)

class TH(Tbase):
    """Column Heading cell.

    Keywords Available

        align -- set to either top|bottom|left|right
        valign -- set to either top|middle|bottom|baseline
        rowspan -- integer number of rows this heading cell should span
        colspan -- integer number of columns this heading cell should span
        nowrap -- flag to indicate that no text wrapping be done on this cell
        width -- integer or percent to force cell width
    """
    tagname = 'TH'
    attrs = ('align','valign','rowspan','colspan','bgcolor')
    flags = ('nowrap',)
    
class TD(Container, Tbase):
    """Data cell.

    Keywords Available

        align -- set to either left|right|center|justify|char|decimal
        valign -- set to either top|middle|bottom|baseline
        rowspan -- integer number of rows this cell should span
        colspan -- integer number of columns this cell should span
        nowrap -- flag to indicate that no text wrapping be done on this cell
        width -- integer or percent to force cell width
        bgcolor -- color string used for the background of the table data
    """
    tagname = 'TD'
    attrs = ('align','valign','rowspan','colspan','width','bgcolor')
    flags = ('nowrap',)

class TR(Container, Tbase):
    """Table Row.  Contains a series of TH or TD cells.

    Keywords Available

        align -- set to either left|right|center|justify|char|decimal
        valign -- set ot either top|middle|bottom|baseline for vertical alignment
        bgcolor -- color string used for the background of the table row
    """
    tagname = 'TR'
    attrs = ('align','valign', 'bgcolor')

class TableLite(Container, Tbase):
    """Container for HTML tables.

    This is an implementation for Peter Gerhard who wanted a
    completely flexible Table class. Well, I also used it as
    an exercise in multiple inheritance. Gosh it's easy!

    Keywords Available

        align -- set to either left|right|center|justify|bleedleft|bleedright
        border -- outside frame width in pixels. set to 0 for no border
        frame -- set to void|above|below|hsides|lhs|rhs|vsides|box|border
        cellpadding -- integer spacing between cell content and cell border
        cellspacing -- integer spacing between cells (defines cell border thickness)
        width -- integer or percentage width of entire table. percentages are the
                 fraction of the window while a literal integer forces a pixel width.
    """
    tagname = 'TABLE'
    attrs = ('align','border','frame','cellpadding','cellspacing','width','bgcolor')

class Multicol(Container):
    """Declare a multi-column section of the page.

    Instantiate the Multicol class and use the append method to add contents
    to the section. Mutlicol sections can be nested but it's not recommended
    for appearance reasons.

    Keyword Arguments

        cols -- number of column. If not provided it defaults to 2.
        gutter -- width in pixels of the gap between the columns. Default is 10.
        width -- width in pixels of the columns. All columns are the same width.
                 Overall width of the multicol section is
                 (cols * width) + ((cols - 1) * gutter)

    The method *total_width* is provided for the lazy folks who don't want
    to calculate the above equation.
    """
    cols = 2
    gutter = 0
    width = 0
    def start_tag(self):
        "Return start tag for this tag type including all attributes"
        s = '<MULTICOL'
        s = s + ' COLS=%s' % self.cols
        if self.gutter: s = s + ' GUTTER=%s' % self.gutter
        if self.width:  s = s + ' WIDTH=%s' % self.width
        return s + '>'

    def end_tag(self):
        "Return end tag for this tag type"
        return '</MULTICOL>\n'

    def total_width(self):
        """Calculates the total width in pixels of the multi-column section
        given the current object properties.
        """
        if self.width > 0:
            gutter = self.gutter or 10
            cols = self.cols
            width = self.width
            return `(cols * width) + ((cols - 1) * gutter)` + ' pixels'
        else:
            return 'Need a specific column width first.'

    def set_total_width(self, total):
        """Calculates and sets the column width needed to make this section
        the given the total width in pixels desired. 
        """
        gutter = self.gutter or 10
        cols = self.cols
        self.width = (total - ((cols - 1) * gutter)) / cols
        
MULTICOL = Multicol

class Spacer:
    """Spacing object to force spcific spacing between other objects.

    The *type* attribute has three possible values: 'horizontal',
    'vertical', and 'block'.  The default value is horizontal.

        - The horizontal spacer inserts horizontal space between
        words. The width of the space is controlled by the *size*
        attribute.

        - The vertical spacer inserts vertical space between
        lines. Implicit in this spacer is a line break to end the
        current line, then the vertical space is added before the
        beginning of the next line. The height of the space is
        controlled by the *size* attribute.

        - The block spacer behaves almost exactly like an invisible
        image. When using this type of spacer the *size* attribute is
        ignored, and instead the *width*, *height*, and *align*
        attributes are applied just as they would be for the <IMG>
        tag.

    The *size* attribute only applies when the spacer has a type of
    horizontal or vertical. Then this attribute controls the absolute
    width or height in pixels of the spacing added.

    The *width* attribute only applies when the spacer is of type
    block. Then this attribute controls the absolute width in pixels
    of the spacing rectangle added.

    The *height* attribute only applies when the spacer is of type
    block. Then this attribute controls the absolute height in pixels
    of the spacing rectangle added.

    The *align* attribute only applies when the spacer is of type
    block. Then this attribute controls the alignment of the spacing
    rectangle in exactly the same way it would control the alignment
    of an <IMG> tag.  """

    def __init__(self, **kw):
        self.type = 'horizontal'
        self.size = None
        self.width = None
        self.height = None
        self.align = None
        for item in kw.keys():
            if self.__dict__.has_key(item):
                self.__dict__[item] = kw[item]
            else:
                raise KeyError, `item`+' not a valid parameter of the Spacer class.'
    def __repr__(self):
        s = '<SPACER TYPE="%s"' % self.type
        if self.size:   s = s + ' SIZE=%s' % self.size
        if self.width:  s = s + ' WIDTH=%s' % self.width
        if self.height: s = s + ' HEIGHT=%s' % self.height
        if self.align:  s = s + ' ALIGN="%s"' % self.align
        return s + '>'
        
  

# Text Formatting Classes
class InitialCaps:
    """Utility class to process text into Initial Upper Case style
    using Font specifications. All text is converted to upper case
    and the initial characters are altered by the size given by
    the optional second argument. The rest of the characters are
    altered by the size given in the optional third argument.

    For example:
    
       InitialCaps('We the people', '+3', '+1')
    """
    def __init__(self, text='', upsize = '+2', downsize = '+1'):
        list = string.split(text)
        self.wordlist = []
        for word in list:
            word = `Font(string.upper(word[0]), size=upsize)` +\
                   `Font(string.upper(word[1:]), size=downsize)`
            self.wordlist.append(word)

    def __repr__(self):
        return string.join(self.wordlist)

class Text:
    """Base class for text.

    Escape the special characters for html.
    """
    def __init__(self, text='', **kw):
        if type(text) == StringType: text = escape(text)
        self.text = str(text)
        self.size = None
        self.color = None
        self.face = None
        for item in kw.keys():
            self.__dict__[item] = kw[item]

    def append(self, text=''):
        """Concatenate text characters onto the end.
        
        Will escape special characters.
        """
        if type(text) == StringType: text = escape(text)
        self.text = self.text + ' ' + str(text)

    def __repr__(self):
        return self.text

class RawText(Text):
    """Base class for raw text.

    Does **NOT** escape the special characters."""
    def __init__(self, text=''):
        self.text = text
        
    def append(self, text=''):
        self.text = self.text + ' ' + str(text)

class Pre(RawText):
    """Preformatted text. Will not escape any special characters.
    """
    def __repr__(self):
        return '<PRE>\n%s\n</PRE>\n' % self.text

class Backquote(Text):
    """Use the <BLOCKQUOTE> tag

    Typically used to include lengthy quotations in
    a separate block on the screen.
    """
    def __repr__(self):
        return '<BACKQUOTE>\n%s\n</BACKQUOTE>\n' % self.text

class Font(Text):
    """Lets you change the attributes of text.

    Argument is a text string or object with a string representation.
    Keyword arguments control the rendered apperance of this text.

    size  -- Browsers typically represent font size as an index from 1 to 7.
             Normal body text is declared a 3 on this scale (not in point size).
             Relative font changes can be declared by using a '+/-N' notation
             where N is the number of size steps relative to the surrounding
             text.
    color -- Set the color of the text using the hex triple notation.
    face  -- A string listing (comma separated) the preferred font family names.
             e.g., face="Times,Times New Roman" or face="Helvetica,Arial,Geneva".
             This allows more direct usage of font capabilities on browsing
             machines.

    Arguments must be strings. e.g. Font('Blazing',color='#cc0000',size='+2')
    will present the word *Blazing* in the color red and a font two sizes
    larger than the surrounding text.
    """
    def __repr__(self):
        # every time we add an attribute to test on be sure to
        # add it to the __init__ constructor in the base class (Text).
        s = '<FONT'
        if self.size: s = s + ' SIZE="%s"' % self.size
        if self.color: s = s + ' COLOR="%s"' % self.color
        if self.face: s = s + ' FACE="%s"' % self.face
        s = s + '>'
        s = s + str(self.text) + '</FONT>'
        return s

class Address(Text):
    """Used to specify the author of a document, etc.
    
    Has nothing to do with Postal addressing. That should be PREformatted.
    """
    def __repr__(self):
        return '<ADDRESS>%s</ADDRESS>\n' % self.text

class Emphasis(Text):
    """Use for emphasis.

    Typically displayed in italics.
    """
    def __repr__(self):
        return '<EM>%s</EM>' % self.text

class Cite(Text):
    """Use for titles of books, films, etc.
    
    Typically displayed in italics.
    """
    def __repr__(self):
        return '<CITE>%s</CITE>' % self.text

class KBD(RawText):
    """Use for user keyboard entry.
    
    Typically displayed in plain fixed-width font.
    """
    def __repr__(self):
        return '<KBD>%s</KBD>' % self.text

class Sample(RawText):
    """Use for a sequence of literal characters.
    
    Displayed in a fixed-width font.
    """
    def __repr__(self):
        return '<SAMP>%s</SAMP>' % self.text

class Strong(Text):
    """Use for strong emphasis.
    
    Typically displayed in bold.
    """
    def __repr__(self):
        return '<STRONG>%s</STRONG>' % self.text

class Code(RawText):
    """Use for computer code.

    Displayed in a fixed-width font.
    """
    def __repr__(self):
        return '\n<CODE>%s\n</CODE>\n' % self.text

class Define(Text):
    """Use for a word being defined.

    Typically displayed in italics.
    """
    def __repr__(self):
        return '<DFN>%s</DFN>' % self.text

class Var(Text):
    """Use for a variable.

    Used where you will replace the variable with specific information.
    Typically displayed in italics.
    """
    def __repr__(self):
        return '<VAR>%s</VAR>' % self.text

PRE = Pre
Bold = STRONG = Strong
Italic = EM = Emphasis
Typewriter = Sample

# Misc items
class HR:
    """Horizontal Rule.
    
    thickness -- The pixel thickness of the line

    Keyword Arguments

        width -- either int number of pixels or string percentage of window
        align -- string either 'left'|'right'|'center'
        noshade -- set to non-null value to force no bevel shading effect
    """
    def __init__(self, thickness=None, **kw):
        self.size = thickness
        self.width = None
        self.align = None
        self.noshade = None
        for item in kw.keys():
            self.__dict__[item] = kw[item]

    def __repr__(self):
        s = '\n<HR'
        if self.size: s = s + ' SIZE=%s' % self.size
        if self.width: s = s + ' WIDTH=%s' % self.width
        if self.align: s = s + ' ALIGN=%s' % self.align
        if self.noshade: s = s + ' NOSHADE'
        s = s + '>\n'
        return s

class BR:
    """Force Line break. Integer argument causes repeated breaks.
    """
    def __init__(self, multi = 1):
        self.multi = multi
    def __repr__(self):
        return '\n' + '<BR>'*self.multi + '\n'

class NOBR:
    """No Break.

    All the text between the start and end of the NOBR elements cannot
    have line breaks inserted between them by the browser's wrapping
    mechanism.  """

    def __init__(self, text=''):
        self.text = text
    def __repr__(self):
        return '<NOBR>%s</NOBR>' % self.text

class Center:
    """A general form to center arbitrary content.
    
    Netscape folks say this is prefered over <P align=center>.
    """
    def __init__(self, text=''):
        self.text = text
    def __repr__(self):
        return '<CENTER>%s</CENTER>' % self.text

class Indent(Text):
    """Indent text using the UL tag.
    """
    def __init__(self, text=''):
        self.text = text
    def __repr__(self):
        return '<UL>\n%s</UL>' % self.text

class Comment:
    """Place a comment internal to the html doc.

    Will not be visible from the browser.
    """
    def __init__(self, text=''):
        self.text = text
    def __repr__(self):
        return '\n<!-- %s -->\n' % self.text

