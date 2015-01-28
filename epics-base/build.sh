#!/bin/bash
make -j$(getconf _NPROCESSORS_ONLN)
EPICS_BASE=$PREFIX/lib/epics
EPICS_HOST_ARCH=$(startup/EpicsHostArch)

cd $PREFIX

install -d $PREFIX/bin
install -d $PREFIX/lib
LIBDIR=$PREFIX/lib/epics/lib/$EPICS_HOST_ARCH
BINDIR=$PREFIX/lib/epics/bin/$EPICS_HOST_ARCH
LIBS=`find $LIBDIR/* -type f`
BINS="caget caput camonitor softIoc"

for file in $LIBS ; do
	f=${file##$LIBDIR}
	ln -s ../lib/epics/lib/$EPICS_HOST_ARCH/$f lib/$f
done
for file in $BINS ; do
	f=${file##$BINDIR}
	ln -s ../lib/epics/bin/$EPICS_HOST_ARCH/$f bin/$f
done
