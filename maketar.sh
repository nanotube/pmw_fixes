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
for dir in `find . -name CVS -type d`
do
    /bin/rm -r $dir
done
for file in `find . -name "*.pyc" -type f`
do
    /bin/rm -r $file
done

/bin/rm ReleaseProcedure maketar.sh
echo Unexpected files:
echo ===== start =====
cat << EOF | sed "s/0_0_0/${DIR}/" > /tmp/Pmw.dirs1
.
./Alpha_99_9_example
./Alpha_99_9_example/lib
./Pmw_0_0_0
./Pmw_0_0_0/bin
./Pmw_0_0_0/contrib
./Pmw_0_0_0/demos
./Pmw_0_0_0/docsrc
./Pmw_0_0_0/docsrc/images
./Pmw_0_0_0/docsrc/text
./Pmw_0_0_0/lib
./Pmw_0_0_0/tests
EOF
find . -type d | sort > /tmp/Pmw.dirs2
diff /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
/bin/rm /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
cat << EOF | sed "s/0_0_0/${DIR}/" > /tmp/Pmw.dirs1
./Pmw_0_0_0/docsrc/Pmw.announce
EOF
find . -type f | egrep -v "\.(py|html|gif|bmp)$" | \
    egrep -v "(README|Pmw.def)" > /tmp/Pmw.dirs2
diff /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
echo ====== end ======
/bin/rm /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
cd /tmp/Pmw/Pmw_${DIR}

# Create documentation source:
tar cf Pmw.${VERSION}.docsrc.tar ./docsrc
gzip Pmw.${VERSION}.docsrc.tar
mv Pmw.${VERSION}.docsrc.tar.gz /tmp

/bin/rm -rf doc
cd /tmp/Pmw/Pmw_${DIR}/docsrc
./createmanuals.py
cd /tmp/Pmw/Pmw_${DIR}

/bin/rm -rf docsrc
cd /tmp/Pmw
for file in `find . -name "*.pyc" -type f`
do
    /bin/rm -r $file
done
cd /tmp
/bin/rm -f Pmw.${VERSION}.tar.gz
tar cf Pmw.${VERSION}.tar ./Pmw
gzip Pmw.${VERSION}.tar

# Now that the tar file has been created, unpack and run the tests.
/bin/rm -rf pmw.tmp
mkdir pmw.tmp
cd /tmp/pmw.tmp
gzip -dc /tmp/Pmw.${VERSION}.tar.gz | tar xf -
