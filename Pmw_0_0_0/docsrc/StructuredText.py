#!/bin/env python

import cgi
import regex
import regsub


# Characters that can come before and after a font change string.
before = '\([- \n(]\|^\)'
after = "\([-) \n,.:;'!?]\|$\)"

# Font types:

# 'italic'
reg_em = regex.compile(before + "'\([^ ']\([^\n']*[^ ]\)?\)'" + after)

# Let single quotes be escaped with a backslash: \'
reg_escape_em = regex.compile("\\\\'")

# *bold*
reg_strong = regex.compile(before + "\*\([^ *]\([^\n*]*[^ ]\)?\)\*" + after)

# /code/
reg_code = regex.compile(before + "/\([^ /]\([^\n/]*[^ ]\)?\)/" + after)

# ~~link~~text~~
reg_link = regex.compile(before + "~~\([^ ][^\n]*[^ ]\)~~\([^ ][^\n]*[^ ]\)~~" + after)

# ~link~
reg_pmw_link = regex.compile(before + "~\([^ ][^\n~]*[^ ]\)~" + after)


# Paragraph types:

# - bullet list
reg_bullet = regex.compile('[ \n]*[o*-][ \n]+\([^\0]*\)')

# 1.2.3 ordered list
reg_ol = regex.compile('[ \n]*\(\([0-9]+\|[a-zA-Z]+\)\.\)+[ \n]+\([^\0]*\|$\)')

# (99) ordered list
reg_olp = regex.compile('[ \n]*([0-9]+)[ \n]+\([^\0]*\|$\)')

# -- definition list
reg_dl = regex.compile('[ \n]*\([^\n]+\) +--[ \n]+\([^\0]*\)')

# # preformated code
reg_pre=regex.compile('[ \n]*#\([^\0]*\)')


# A single line paragraph ending in ':' is a heading
reg_nl=regex.compile('\n')

# To remove leading spaces and # on each line in preformated code:
reg_remove_hash=regex.compile('\n *#')


reg_indent_tab = regex.compile('\(\n\|^\)\( *\)\t')
reg_indent_space = regex.compile('\n\( *\)')
reg_paragraph_divider = regex.compile('\(\n *\)+\n')

reg_extra_dl = regex.compile("</dl>\n<dl>")
reg_extra_ul = regex.compile("</ul>\n<ul>")
reg_extra_ol = regex.compile("</ol>\n<ol>")

def gethtml(structuredString):
    '''\
    An HTML structured text formatter.
    Model text as structured collection of paragraphs.
    Structure is implied by the indentation level.

    Convert a string containing structured text into a structured
    text object.
      structuredString -- The string to be parsed.

    Return an HTML string representation of the structured text data.
    '''

    # Turn <, >, &, etc into html escape sequences and remove tabs.
    escapedText = cgi.escape(structuredString)
    noTabstext = untabify(escapedText)

    #########
    # Not yet finished
    # # Convert '.. [ref1] "Foo" by Bar', A to a named link.
    # print '==='
    # print noTabstext
    # print '==='
    # #Find out what \0 means inside []. Maybe convert to re module.
    # noTabstext = regsub.gsub(
    #     '\(^\|\n\) *\.\. \[\([0-9_a-zA-Z-]+\)\]',
    #     '\n  <a name="\\2">[\\2]</a>',
    #     noTabstext)
    #             
    # # Convert '[ref1]' to a link within the document.
    # noTabstext = regsub.gsub(
    #     '\([\0- ,]\)\[\([0-9_a-zA-Z-]+\)\]\([\0- ,.:]\)',
    #     '\\1<a href="#\\2">[\\2]</a>\\3',
    #     noTabstext)
    #             
    # # Convert '[foo.html]' to an external link.
    # noTabstext = regsub.gsub(
    #     '\([\0- ,]\)\[\([^]]+\)\.html\]\([\0- ,.:]\)',
    #     '\\1<a href="\\2.html">[\\2]</a>\\3',
    #     noTabstext)

    # Split the text into a list of paragraphs separted by a blank line.
    rawParagraphs = regsub.split(noTabstext, reg_paragraph_divider)

    # Create a list of (indent, para), where 'indent' is the number
    # of spaces on the first line and 'para' is the text'
    paragraphs = map(indent_level, rawParagraphs)

    # Create a list of (para, structure), where 'para' is the text of
    # a paragraph and 'structure' is a similar list of 'child'
    # paragraphs (ie, those indented further than 'para').
    structure=parse_structure(paragraphs)
    #print '<pre>'
    #print_structure(structure)
    #print '</pre>'

    s=structure_to_string(structure, 1)
    s=regsub.gsub(reg_extra_dl,'\n',s)
    s=regsub.gsub(reg_extra_ul,'\n',s)
    s=regsub.gsub(reg_extra_ol,'\n',s)
    return s

def print_structure(structure, indent = ''):
    import string
    print indent + str(len(structure))
    for p, s in structure:
	print indent + string.strip(p[:20])
	if len(s) > 0:
	    print_structure(s, indent = indent + '    ')

def changefonts(s):
    s=regsub.gsub(reg_em,'\\1<em>\\2</em>\\4',s)
    s=regsub.gsub(reg_escape_em,"'",s)
    s=regsub.gsub(reg_strong,'\\1<strong>\\2</strong>\\4',s)
    s=regsub.gsub(reg_code,'\\1<code>\\2</code>\\4',s)
    s=regsub.gsub(reg_link,'\\1<a href="\\2">\\3</a>\\4',s)
    s=regsub.gsub(reg_pmw_link,'\\1<a href="\\2.html">Pmw.\\2</a>\\3',s)
    return s

def untabify(aString):
    '''\
    Convert indentation tabs to spaces.
    '''
    result=''
    rest=aString
    while 1:
	start=reg_indent_tab.search(rest)
	if start >= 0:
	    lnl=len(reg_indent_tab.group(1))
	    indent=len(reg_indent_tab.group(2))
	    result=result+rest[:start]
	    rest="\n%s%s" % (' ' * ((indent/8+1)*8),
			     rest[start+indent+1+lnl:])
	else:
	    return result+rest

def indent_level(aString):
    '''\
    Find the minimum indentation for a string, not counting blank lines.
    '''
    start=0
    text='\n'+aString
    indent=l=len(text)
    while 1:
	start=reg_indent_space.search(text,start)
	if start >= 0:
	    i=len(reg_indent_space.group(1))
	    start=start+i+1
	    if start < l and text[start] != '\n':	# Skip blank lines
		if not i:
		    return (0,aString)
		if i < indent:
		    indent = i
	else:
	    return (indent,aString)

def paragraphs(list,start):
    l=len(list)
    level=list[start][0]
    i=start+1
    while i < l and list[i][0] > level:
	i=i+1
    return i-1-start

def parse_structure(list):
    if not list:
	return []
    i=0
    l=len(list)
    r=[]
    while i < l:
	sublen=paragraphs(list,i)
	i=i+1
	r.append((list[i-1][1],parse_structure(list[i:i+sublen])))
	i=i+sublen
    return r

def ul(p, after):
    p = changefonts(p)
    if p:
	p="<p>%s</p>" % p
    return '<ul><li>%s\n%s\n</ul>\n' % (p,after)

def ol(p, after):
    p = changefonts(p)
    if p:
	p="<p>%s</p>" % p
    return '<ol><li>%s\n%s\n</ol>\n' % (p,after)

def dl(t, d, after):
    t = changefonts(t)
    d = changefonts(d)
    return '<dl><dt>%s<dd>%s</p>\n%s\n</dl>\n' % (t,d,after)

def head(p, level, after):
    p = changefonts(p)
    if level > 0 and level < 6:
        return '<h%d>%s</h%d>\n%s\n' % (level, p, level, after)
    else:
        p = "<p><strong>%s</strong><p>" % p
        return '<dl><dt>%s\n<dd>%s\n</dl>\n' % (p, after)

# hash mark (#) at start of line indicates preformatted text
def pre(p, after):
    # Do not call changefonts for preformatted text.
    p = regsub.gsub(reg_remove_hash, '\n', p)
    return '<dl><dd><pre>%s</pre></dl>\n%s\n' % (p, after)

def normal(p,after):
    p = changefonts(p)
    return '<p>%s</p>\n%s\n' % (p,after)

def structure_to_string(structure, level):
    r = ''
    for text, sub_structure in structure:
	if reg_bullet.match(text) >= 0:
	    p=reg_bullet.group(1)
	    r = r + ul(p,structure_to_string(sub_structure, level))
	elif reg_ol.match(text) >= 0:
	    p=reg_ol.group(3)
	    r = r + ol(p,structure_to_string(sub_structure, level))
	elif reg_olp.match(text) >= 0:
	    p=reg_olp.group(1)
	    r = r + ol(p,structure_to_string(sub_structure, level))
	elif reg_dl.match(text) >= 0:
	    t,d=reg_dl.group(1,2)
	    r = r + dl(t,d,structure_to_string(sub_structure, level))
	elif reg_pre.match(text) >= 0:
	    p=reg_pre.group(1)
	    r = r + pre(p,structure_to_string(sub_structure, level))

        #########
        # Not yet finished
	# elif reg_nl.match(text) < 0 and sub_structure and text[-1:] != ':':
        #     r = r + head(text, level,
        #             structure_to_string(sub_structure, level and level + 1))

	else:
	    r = r + normal(text,structure_to_string(sub_structure, level))
    return r

if __name__ == '__main__':
    print gethtml(open('StructuredText.test').read())
