#!/bin/bash
make -j$(getconf _NPROCESSORS_ONLN)
EPICS_BASE=$PREFIX/lib/epics
EPICS_HOST_ARCH=$(startup/EpicsHostArch)


install -d $PREFIX/bin
install -d $PREFIX/lib
BINS="caget caput camonitor softIoc"

cd $PREFIX/lib
ln -s epics/lib/$EPICS_HOST_ARCH/lib* .

cd $PREFIX/bin
for file in $BINS ; do
	ln -s ../lib/epics/bin/$EPICS_HOST_ARCH/$file .
done
