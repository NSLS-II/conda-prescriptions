#!/bin/bash
for f in *
do
    if [ -d $f ]
    then
        cd $f
        for f in *
        do
            if [ -d $f ]
            then
                cd $f
                if [ -e "meta.yaml" ]
                then
                    conda build .
                fi
                cd ..
            fi
        done
        cd ..
    fi
done

exit 0
