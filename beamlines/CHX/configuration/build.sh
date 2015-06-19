#!/bin/bash

mkdir -p $PREFIX/etc
ETC=$PREFIX/etc


# set up
echo "# metadatastore configuration
# installed by chx_configuration
# DO NOT EDIT
host: xf11idb-ioc1
database: datastore
port: 27017
timezone: US/Eastern
" > $ETC/metadatastore.yml

echo "# filestore configuration
# installed by chx_configuration
# DO NOT EDIT
host: xf11idb-ioc1
database: filestore
port: 27017
" > $ETC/filestore.yml

echo "# archiver configuration
# installed by chx_configuration
url: http://xf11id-ca.cs.nsls2.local/cgi-bin/ArchiveDataServer.cgi
pv_dict:
   DCM_TBragg: XF:11ID1-OP{Mono:DCM-Ax:Bragg}T-I
" > $ETC/filestore.yml



# clean up after self
unset ETC
