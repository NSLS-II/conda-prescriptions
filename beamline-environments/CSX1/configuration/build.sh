
mkdir -p $PREFIX/etc
ETC=$PREFIX/etc

echo "# archiver configuration
# installed by csx1_configuration
# DO NOT EDIT
db: "$ETC"/pv_mapping.sql
url: https://xf23id-ca.cs.nsls2.local:8888/cgi-bin/ArchiveDataServer.cgi
" >$ETC/archiver.yml

echo "# filestore configuration
# installed by csx1_configuration
# DO NOT EDIT
database: filestore
host: xf23id-broker
port: 27017
" >$ETC/filestore.yml

echo "# metadatastore configuration
# installed by csx1_configuration
# DO NOT EDIT
database: datastore2
host: xf23id-broker
port: 27017
timezone: US/Eastern
" >$ETC/metadatastore.yml



# clean up after self
unset ETC
