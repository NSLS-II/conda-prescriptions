#!/bin/bash
for f in *
do
    if [ -d $f ]
    then
        cd $f
        if [ -e ".binstar.yml" ]
        then
            if [[ $f == *"master"* ]]
            then
                binstar-build submit
            fi
        fi
        cd ..
    fi
done

exit 0
