text = """
    There are two aspects of Pmw, unrelated to megawidgets, that
    require special attention.  Firstly, Pmw is made up of many
    sub-modules, potentially making access to its various classes and
    functions cumbersome for the user.  Secondly, Pmw is regularly
    being modified and added to, thus requiring the release of new
    versions.  Therefore, techniques for making access to the
    sub-modules easy and efficient and for dealing with the different
    versions have been developed.  These techniques are incorporated
    into the dynamic loader which Pmw creates when it is first
    imported.

    The first purpose of the loader is to give access to all Pmw classes
    and functions through a single entry point, the *Pmw.* prefix.  For
    example, to access the ComboBox class (which resides in one of the
    sub-modules of Pmw), you just have to use /Pmw.ComboBox/.  Without
    the loader, this would be a more complicated reference, such as,
    hypothetically, /Pmw.PmwComboBox.ComboBox/.

    The second purpose of the loader is to delay the importing of the
    sub-modules until they are needed.  This improves the startup time
    of applications which only use a few Pmw megawidgets.  It also
    allows more megawidgets to be added to the library without slowing
    down applications which do not use them.

    The third purpose of the loader is to allow a script using Pmw to
    specify which version of Pmw it requires.  This allows an
    application to continue working correctly even after newer releases
    of Pmw have been made which are not compatible with the version
    expected by the application.  Several versions of Pmw can be
    installed at once, with the actual version used being specified by
    each application.  In addition, the loader can be configured to
    search in one or more alpha versions of Pmw.  These versions may
    contain new megawidgets, or new versions of existing megawidgets,
    that are currently not in the base releases.

    Several functions are available to set and query the version of
    Pmw being used.  These are /Pmw.setversion()/ and
    /Pmw.setalphaversions()/ which specify the version and alpha
    versions (if any) to use for this session; /Pmw.version()/ which
    returns the version(s) being used by this session; and
    /Pmw.installedversions()/ which returns the version(s) of Pmw
    currently installed.  These are described in the
    ~~PmwFunctions.html~~Pmw functions reference manual~~.

    When Pmw is first imported, an instance of PmwLoader is created
    and placed into /sys.modules['Pmw']/.  From that point on, any
    reference to attributes of the Pmw \\'module\\' is handled by the
    loader.  The real Pmw package is stored in /sys.modules['_Pmw']/.

    The loader searches the Pmw package base directory for
    sub-directories with the prefixes /Pmw_/ and /Alpha_/, which
    contain Pmw base releases and alpha releases.  The version numbers
    are given by the part of the directory name following the prefix. 
    These versions are available for use and are those returned by the
    /Pmw.installedversions/ function.  The initial version is set to
    the base release with the greatest version number.  When the first
    reference to a Pmw class or function is made, the loader reads the
    files named *Pmw.def* in the current base version directory and
    also in the alpha directories (if any).  These files list all the
    classes and functions supported by the version.  Pmw attributes
    are first searched for in the alpha directories and then in the
    base version directory.  The first directory which supports the
    reference is used.  In this way, alpha versions override base
    versions.

    The directory /Alpha_99_9_example/ contains a simple example of
    how to structure an alpha version.  The following code can be used
    to request that the alpha version be used and then creates an
    instance of a new megawidget defined in the alpha version.

    # import Pmw
    # Pmw.setalphaversions('99.9.example')
    #
    # # Create a standard message dialog using the base Pmw version.
    # ordinary = Pmw.MessageDialog(
    #     message_text = 'Ordinary\\nPmw Dialog')
    #
    # # Create an example dialog using the alpha Pmw version.
    # alpha = Pmw.AlphaExample()

    *Freezing Pmw*

    Since the dynamic loader requires that Pmw be installed at run
    time, it can not be used when 'freezing' Pmw.  In this case, a
    single module containing all Pmw code is required, which can then
    be frozen with the rest of the application's modules.  The
    /bundlepmw.py/ script in the Pmw /bin/ directory can be used to
    create such a file.  This script concatenates (almost) all Pmw
    megawidget files into a single file, /Pmw.py/, which it writes to
    the current directory.  The script is called like this:

    # bundlepmw.py [-noblt] [-nocolor] /path/to/Pmw/Pmw_X_X_X/lib

    The last argument should be the path to the /lib/ directory of the
    required version of Pmw.  By default, the /Pmw.py/ file imports
    the /PmwBlt/ and /PmwColor/ modules and so, to freeze an
    application using Pmw, you will need to copy the files /PmwBlt.py/
    and /PmwColor.py/ to the application directory before freezing.

    If you are sure that your application does not use any of the
    /Pmw.Blt/ or /Pmw.Color/ functions, you can use the /-noblt/ or
    /-nocolor/ options.  In this case /Pmw.py/ will be modified so
    that it does not import these module(s) and so will not need to be
    included when freezing the application.

    If your application only uses a few Pmw megawidgets, you can
    remove the references to the usused ones in the /files/ list in
    the /bundlepmw.py/ code.  To make the change, take a copy of the
    script and modify it.  This will make the /Pmw.py/ file smaller. 
    However, be sure that you do not delete megawidgets that are
    components or base classes of megawidgets that you use.

"""
