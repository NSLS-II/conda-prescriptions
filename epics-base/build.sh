#!/bin/bash
make -j$(getconf _NPROCESSORS_ONLN)
EPICS_BASE=$PREFIX/lib/epics

install -d $PREFIX/lib
cp -Prv lib/linux-x86_64/* $PREFIX/lib

install -d $PREFIX/bin
cp -Prv bin/linux-x86_64/caget $PREFIX/bin
cp -Prv bin/linux-x86_64/caput $PREFIX/bin
cp -Prv bin/linux-x86_64/camonitor $PREFIX/bin
cp -Prv bin/linux-x86_64/caRepeater $PREFIX/bin
cp -Prv bin/linux-x86_64/softIoc $PREFIX/bin

for X in bin configure db dbd include lib startup templates; do
  install -d $EPICS_BASE/$X
  cp -Prv $X/* $EPICS_BASE/$X
done
