#!/bin/bash

mkdir -p $PREFIX/etc
ETC=$PREFIX/etc


# set up
echo "# metadatastore configuration
# installed by nslsii_dev_configuration
# DO NOT EDIT
host: localhost
database: datastore_DEV
port: 27017
timezone: US/Eastern
" > $ETC/metadatastore.yml

echo "# filestore configuration
# installed by nslsii_dev_configuration
# DO NOT EDIT
host: localhost
database: filestore_DEV
port: 27017
" > $ETC/filestore.yml



# clean up after self
unset ETC
