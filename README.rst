conda-prescriptions
===================

Localized conda rescipies for use with Nikea and NSLS-II

A collection of conda-recipes for external depenancies and the 'stable' version of
locally developed libraries.


Building the binaries with the NSLS-II build server
---------------------------------------------------
#. Follow numbers 1 and 2 `here <https://github.com/NSLS-II/docs/blob/master/source/binstar.rst#submitting-builds-to-binstar>`_
#. Run the `recreate_binstar_yml.py` module from the command line with the extra
   arguments [binstar-account] [channel-name]. Though it is worth noting that `binstar-build submit`
   is not respecting the `channels` argument, so {CHANNEL_NAME} is rather optional, for now.
   This automatically configures all binstar.yml files in every directory with a ``meta.yaml``
   file. ::

      python recreate_binstar_yml.py {BINSTAR_ACCOUNT} {CHANNEL_NAME}

#. Submit individual builds by navigating to the ``releases/package/version/`` folder or the
   ``master/package/`` folder and running `bash binstar-build-submit.sh`

#. Submit master branch builds for all repositories in the ``master/`` folder ::

      cd master
      bash unix-build.sh


#. Note: You may get a number of errors in the previous step that look like
   the following:

    Using binstar api site https://conda.nsls2.bnl.gov/api
    [error] The package edill/pyepics does not exist.
    [error] Run:

        binstar package --create edill/pyepics

     to create this package
    [NotFound] Package edill/pyepics

   If you get these errors, simply follow the directions and create that package in the binstar
   account you are trying to upload to. You will need to do this once for each package for each
   binstar account ::

Build Order
-----------
If you are starting with a blank slate, this is the build order for the NSLS-II stack.
It must be respected!

#. Build order for **carchivetools**
    #. tzlocal
    #. pyasn1-modules
    #. characteristic
    #. service_identity
    #. protobuf
    #. carchivetools (PY2 only)
#. certifi
#. conda_etc
#. lmfit
#. Build order for **metadatastore**
    #. nslsii_dev_configuration
    #. mongoengine
    #. metadatastore cannot find the CONDA_ETC environmental variable apparently... what the hell??
#. Build order for **filestore**
    #. tifffile
    #. pims (PyQt4 syntax errors on py3 with unix-64)
    #. filestore cannot find the CONDA_ETC environmental variable apparently... what the hell??
#. Build order for **dataportal**
    #. channelarchiver (master?) (also, watch out for PyQt4 syntax errors on unix-64 with python3.4:
       `link<https://github.com/NSLS-II/conda-prescriptions/issues/35>`_
    #. metadatastore
    #. dataportal
#. ncurses (debian7 only)
#. readline (debian7 only)
#. python2 (debian7 only)
#. python3 (debian7 only)
#. Build order for **ophyd**
    #. requires metadatastore
#. Build order for **pcaspy**
    #. requires epics-base
#. Build order for **beamline metapackages**
#. pyspec : not py3 compatible
#. reindent (has syntax errors in py3) ::

    Writing /Users/ericdill/anaconda/envs/_build/lib/python3.4/site-packages/Reindent-0.1.1-py3.4.egg-info
      File "/Users/ericdill/anaconda/envs/_build/lib/python3.4/site-packages/reindent.py", line 71
        except getopt.error, msg:
                           ^
    SyntaxError: invalid syntax

    *** Error compiling '/Users/ericdill/anaconda/envs/_build/lib/python3.4/site-packages/reindent.py'...
      File "/Users/ericdill/anaconda/envs/_build/lib/python3.4/site-packages/reindent.py", line 71
        except getopt.error, msg:
                           ^
    SyntaxError: invalid syntax
#. sphinx-bootstrap-theme
#. sphinx-contrib-napoleon
#. vistrails

Not yet tested
#. xraylib

Help!
-----
Q: Binstar is uploading to the dev channel not the main channel. How do I fix this?
A1: ``binstar-build submit -p {ORG_NAME}/{PACKAGE_NAME} --channel main``
A2: I have no idea!  However, running this command will copy everything from the default
   "dev" channel to the "main" channel: ``binstar channel -o {USER_NAME} --copy dev main``
   where {USER_NAME} is whatever username/organization you are trying to move binaries
   from ``dev`` to ``main``
