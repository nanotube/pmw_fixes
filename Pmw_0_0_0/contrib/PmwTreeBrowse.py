import Pmw
import Tkinter

class DoubleSelects:
    def __init__(self, hull):
	self.level = len(hull.treeLevel) #hasn't been added to list yet!
	self._hull = hull
	self.name = "Pane 0"
	hull.browser.add(self.name, min= .1,size=150 )
	num = len(hull.browser.panes())
	rel = 1.0/num
	print "REL", rel
	hull.browser.configure(hull_width=num*150)
	for i in range(num):
	    hull.browser.configurepane(i,size=rel)

	self.innerPane = Pmw.PanedWidget(hull.browser.pane(self.name))

	self.topName = 'Pane ' + str(num) + "t"
	self.innerPane.add(self.topName, size = .5,)

	self.topBox = Pmw.ScrolledListBox(self.innerPane.pane(self.topName),
	    listbox_selectmode='single',
	    vscrollmode = 'dynamic',
	    selectioncommand=self.selectionNodeCommand,
	    dblclickcommand=self.defNodeCmd)
        self.topBox.pack(fill= 'both', expand = 'yes', padx=0, pady=0)
        self.topBox.component('listbox').configure(exportselection=0)
	self.bottomName = 'Pane ' + str(num) + "b"
	self.innerPane.add(self.bottomName, size=.5 ,)
	self.bottomBox = Pmw.ScrolledListBox(
	    self.innerPane.pane(self.bottomName),
	    listbox_selectmode='single',
	    vscrollmode = 'dynamic',
	    selectioncommand=self.selectionLeafCommand,
	    dblclickcommand=self.defLeafCmd)
        self.bottomBox.pack(fill = 'both', expand='yes', padx = 0, pady = 0)
        self.bottomBox.component('listbox').configure(exportselection=0)
	self.innerPane.pack(expand = 1, fill='both')

    def selectionNodeCommand(self):
	sels = self.topBox.getcurselection()
	if len(sels) == 0:
	    print 'No selection'
	else:
	    print "bbb", self._hull.tree
	    nodes, leaves = self._hull.tree._selected(sels[0],self.level)
	    apply(self.topbox.insert,('end',)+tuple(nodes))
#	    print  self._hull.current
#	    print 'Selection:', sels[0]
#	    self._hull.selectedNode(self.level,sels)
#	    self.list = self.tree.getRootNodeNames()
#	    print "LIST", list
#	    apply(self.topbox.insert,('end',)+tuple(self.list))
	    

    def defNodeCmd(self):
	sels = self.topBox.getcurselection()
	if len(sels) == 0:
	    print 'No selection for double click'
	else:
	    print 'Double click:', sels[0]

    def selectionLeafCommand(self):
	sels = self.bottomBox.getcurselection()
	if len(sels) == 0:
	    print 'No selection'
	else:
	    print 'Selection:', sels[0]

	#  display the contents of the selected file in a dialog box which
	#  is appended to self.tmpwindict in order to facilitate easy
	#  deletion
	import string   # for string.join
	import os       # for os.sep
	# construct the file name given the selected directory list.
	# NOTE:  if a file is selected under the root directory, then
	#        there will be a double-slash prepended to its name.
	#        this is legal under unix, not sure if it is so under DOS.
	#        also, the slash character must be replaced with a p
#	fn = os.sep + string.join(self._hull.current + sels[0], os.sep) + os.sep + sels[0]
#        self._hull.selectedNode(self.level, self.topBox.getcurselection())
        s = self._hull.current[:self.level+1]
	s.append(sels[0])
        fn = os.sep + string.join(s, os.sep)
	print '*** file selected is \'', fn, '\'.'
	print '*** file directory is ', s
	print '*** app trees: ', self._hull.trees
	print '*** app treeLevel: ', self._hull.treeLevel
	self._hull.tmpwindict[sels[0]]= Pmw.TextDialog()
	self._hull.tmpwindict[sels[0]].component('scrolledtext').importfile(fn)
	    
    def defLeafCmd(self):
	sels = self.bottomBox.getcurselection()
	if len(sels) == 0:
	    print 'No selection for double click'
	else:
	    print 'Double click:', sels[0]    
	

class  TreeBrowser(Pmw.MegaWidget):
    def __init__(self, parent=None, tree=None, **kw):
	self.tree = tree
	self.tmpwindict = {}  #  temporary window list implemented as a dict
	                      #  format:  { 'name', <object> }
	self.trees= []
	self.treeLevel = []
	self.current = []
	optiondefs = ()
	self.defineoptions(kw, optiondefs)
	def pane_conf(sizes):
	    print "pane_conf", sizes

	# Initialise the base class (after defining the options).
        Pmw.MegaWidget.__init__(self, parent)
	oldInterior = Pmw.MegaWidget.interior(self)
	print "OLDINTER", oldInterior

	self.browser =self.createcomponent('browserPane',(),None,
		Pmw.PanedWidget, (oldInterior,),
		hull_width=200, hull_height=300,
			        orient='horizontal',
				command=pane_conf,
#		hull_relief = 'raised',
#		hull_borderwidth = 1,
		)
	self.browser.pack(anchor="nw")# fill = 'x', expand = 'yes' )

	self.initialiseoptions(TreeBrowser)
	self.addPane()
	if tree:
	    self.addRoot(tree)

    def addRoot(self, tree):

#	try:	    
	    rootName = tree.getRootKey()
	    print "ROOTNAME",rootName, self.treeLevel
	    apply(self.treeLevel[0].topBox.insert,('end',)+tuple(rootName))
	    self.trees.append(tree)
#	except:
	    print "Won't work, need data"



    def addPane(self):
	self.treeLevel.append(DoubleSelects(self))

    def clearPanes(self,thislevel):
	for i in range(thislevel,len(self.treeLevel)):
	    print "clear attributes from level ",i, self.treeLevel
	    self.treeLevel[i].bottomBox.delete(0, 'end')
	for i in range(thislevel+1,len(self.treeLevel)):
	    print "clear nodes from level ",i, self.treeLevel
	    self.treeLevel[i].topBox.delete(0, 'end')
    def selectedNode(self, level,sels):
	thislevel = level
	nextlevel = level+1
	self.current = self.current[:thislevel]
	print "CURRENT", self.current, sels
	self.current.append(sels[0])
	print "selectedNode", level,sels, len(self.treeLevel)#, self.current
	nodes = self.trees[0].getNodeNames(tuple(self.current))
#	nnodes = []
#	for i in nodes:
#	    nnodes.append(i[-1])
#	nodes = nnodes
#	print "NODES", nodes
	if len(self.treeLevel) <= nextlevel and len(nodes) > 0:
	    self.addPane()
	self.clearPanes(thislevel)
	attributes = self.trees[0].getLeafKeys(tuple(self.current))
	bottombox = self.treeLevel[thislevel].bottomBox
	print "ATTRIBUTES", attributes, bottombox
	apply(bottombox.insert, ('end',)+tuple(attributes))

	if len(nodes) > 0:
	    topbox = self.treeLevel[nextlevel].topBox
	    apply(topbox.insert, ('end',)+tuple(nodes))
    def interior(self):
	return self.__dialogChildSite


def test():
    import os
    class Tree:
	def __init__(self, root):
	    self.root = root
	    self.current = []

	def _selected(self, word,level):
	    if len(self.current) > level:
		self.current[level-1] = word
		self.current = self.current[:level-1]
	    if len(self.current) == level:
		self.current.append(word)
	    names = os.listdir(string.joinfields(self.current,"/"))
	    print names
	    node = []
	    leaves = []
	    for name in names:
		if os.path.isdir(os.path.join(dirname,name)):
 		    nodes.append(name)
 		else:
 		    leaves.append(name)
	    return nodes, leaves
# 	def mkdict(self,arg,dirname,names):
# 	    pieces = tuple(string.splitfields(dirname,"/")[1:])
# 	    nodes = self.dict[pieces,"nodes"] = []
# 	    leaves = self.dict[pieces,"leaves"] = []
# 	    for name in names:
# 		if os.path.isdir(os.path.join(dirname,name)):
# 		    nodes.append(name)
# 		else:
# 		    leaves.append(name)

# 	    depth = len(string.splitfields(dirname,"/"))-1

	def getRootKey(self):
	    return ((self.root,))

	def getRootName(self):
	    return self.root

# 	def getRootNodeNames(self):
# 	    ret = []
# 	    nodelist = self.getNodeKeys(self.getRootKey())
# 	    print "NODES", nodelist
# 	    for node in nodelist:
# 		ret.append(node[1])
# 	    return ret
	def getNodeNames(self, key):
	    return self.dict[key,"nodes"]

	def getLeafNames(self, key):
	    return self.dict[key,"nodes"]

	def getNodeKeys(self, key):
	    ret = []
	    for name in self.dict[key,"nodes"]:
		ret.append(tuple(list(key)+[name]))
	    return ret

	def getLeafKeys(self, key):
	    ret = []
	    for name in self.dict[key,"leaves"]:
		ret.append(name)
	    return ret
    
    return Tree("etc")	

if __name__ == '__main__':

    root = Pmw.initialise()
    root.resizable(width=0, height=0)
    tree = test()
    widget = TreeBrowser(root, tree)
    widget.pack(anchor="nw", expand='yes')

