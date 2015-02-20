#!/bin/bash
for f in *
do
    if [ -d $f ]
    then
        cd $f
        if [ -e ".binstar.yml" ]
        then
            binstar-build submit
        fi
        cd ..
    fi
done

exit 0
