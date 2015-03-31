#!/bin/bash

mkdir -p $PREFIX/etc
ETC=$PREFIX/etc


# set up
echo "# mds configuration
host: xf10id-ca1
database: datastore
port: 27017
timezone: US/Eastern
" > $ETC/mds.yml

echo "# filestore configuration
host: xf10id-ca1
database: filestore
port: 27017
" > $ETC/filestore.yml



# clean up after self
unset ETC
