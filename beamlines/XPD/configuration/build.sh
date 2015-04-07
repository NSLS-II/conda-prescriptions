#!/bin/bash

mkdir -p $PREFIX/etc
ETC=$PREFIX/etc


# set up
echo "# metadatastore configuration
# installed by xpd_configuration
# DO NOT EDIT
host: xf28id-ca1.cs.nsls2.local
database: datastore
port: 27017
timezone: US/Eastern
" > $ETC/metadatastore.yml

echo "# filestore configuration
# installed by xpd_configuration
# DO NOT EDIT
host: xf28id-ca1.cs.nsls2.local
database: filestore
port: 27017
" > $ETC/filestore.yml



# clean up after self
unset ETC
