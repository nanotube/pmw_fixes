# This script creates a tar file of a Pmw distribution ready to be
# released.  The source for the distribution is in the directory
# Pmw/${SRC_DIR}.  The tar file is stored in
#     /tmp/Pmw.${VERSION}.tar.gz

echo Using Pmw/${SRC_DIR} to create Pmw.${VERSION}.

/bin/rm -rf /tmp/Pmw
tar cf - ./Pmw | (cd /tmp; tar xf -)
mv /tmp/Pmw/${SRC_DIR} /tmp/Pmw/TEMP
/bin/rm -rf /tmp/Pmw/Pmw_*
mv /tmp/Pmw/TEMP /tmp/Pmw/Pmw_${DIR}
cd /tmp/Pmw
find . -name CVS -exec /bin/rm -rf {} \;
find . -name Makeit.mk -exec /bin/rm -f {} \;
find . -name "*.pyc" -exec /bin/rm -f {} \;

# Fix this:
# ./detabAllPy `find . -name "*.py"`

/bin/rm ReleaseProcedure maketar.sh detabAllPy makelibs
echo Unexpected files:
/bin/ls | egrep -v "Alpha_99_9_example|__init__.py|README|Pmw_$DIR"
/bin/ls -lLR | egrep -v "\.(py|html|gif|bmp)$" | \
    egrep -v "^(total|d)" | egrep -v "^$" | egrep -v "(README|Pmw.def)"
cd Pmw_${DIR}

# Create documentation source:
tar cf Pmw.${VERSION}.docsrc.tar ./docsrc
gzip Pmw.${VERSION}.docsrc.tar
mv Pmw.${VERSION}.docsrc.tar.gz /tmp

/bin/rm -rf doc
cd docsrc
./createmanuals.py
cd ..

/bin/rm -rf docsrc
cd ..
find . -name "*.pyc" -exec /bin/rm -f {} \;
cd ..
/bin/rm -f Pmw.${VERSION}.tar.gz
tar cf Pmw.${VERSION}.tar ./Pmw
gzip Pmw.${VERSION}.tar

# Now that the tar file has been created, unpack and run the tests.
cd /tmp
/bin/rm -rf pmw.tmp
mkdir pmw.tmp
cd pmw.tmp
gzip -dc /tmp/Pmw.${VERSION}.tar.gz | tar xf -
echo "Now do this:"
echo "  cd /tmp/pmw.tmp/Pmw/Pmw_${DIR}/tests"
echo "  All.py"
echo "  cd /tmp/pmw.tmp/Pmw/Pmw_${DIR}/demos"
echo "  All.py"
echo "  netscape /tmp/pmw.tmp/Pmw/Pmw_${DIR}/doc/index.html
