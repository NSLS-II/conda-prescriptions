#!/bin/bash
make
echo $PREFIX
mkdir $PREFIX/lib
cp -av lib/linux-x86_64/* $PREFIX/lib
mkdir $PREFIX/bin
cp -av bin/linux-x86_64/caget $PREFIX/bin


