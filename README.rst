conda-prescriptions
===================

Localized conda rescipies for use with Nikea and NSLS-II

A collection of conda-recipes for external depenancies and the 'stable' version of
locally developed libraries.


Building the binaries with the NSLS-II build server
---------------------------------------------------
#. Follow numbers 1 and 2 `here <https://github.com/NSLS-II/docs/blob/master/source/binstar.rst#submitting-builds-to-binstar>`_
#. Run the `recreate_binstar_yml.py` module from the command line with the extra
   arguments [binstar-account] [channel-name]. This automatically configures all
   binstar.yml files in every directory with a ``meta.yaml`` file. ::

      python recreate_binstar_yml.py edill main

#. Submit master branch builds for all repositories in the ``master/`` folder ::

      cd master
      bash unix-build.sh

#. Note: You may get a number of errors in the previous step that look like
   the following monospace. If you get these errors, simply follow the
   directions and create that package in your binstar account. You will need
   to do this once for each package for each binstar account ::

    Using binstar api site https://conda.nsls2.bnl.gov/api
    [error] The package edill/pyepics does not exist.
    [error] Run:

        binstar package --create edill/pyepics

     to create this package
    [NotFound] Package edill/pyepics

Build Order
-----------
If you are starting with a blank slate, this is the build order for the NSLS-II stack.
It must be respected!

# Build order for carchivetools
    # tzlocal
    # pyasn1-modules
    # characteristic
    # service_identity
    # protobuf
    # carchivetools (NOT PY3 COMPATIBLE!)
# certifi
# conda_etc
# Build order for dataportal
    # channelarchiver (master?) (also, watch out for PyQt4 syntax errors on unix-64 with python3.4:
       `link<https://github.com/NSLS-II/conda-prescriptions/issues/35>_
    # <<Note: This build order is incomplete as I need to figure out channelarchiver issues on py3>>
    # dataportal
# lmfit
# Build order for metadatastore
    # nslsii_dev_configuration
    # mongoengine
    # metadatastore cannot find the CONDA_ETC environmental variable apparently... what the hell??

# Build order for beamline metapackages

Help!
-----
Q: Binstar is uploading to the dev channel not the main channel. How do I fix this?
A: I have no idea!  However, running this command will copy everything from the default
   "dev" channel to the "main" channel: ``binstar channel -o {USER_NAME} --copy dev main``
   where {USER_NAME} is whatever username/organization you are trying to move binaries
   from ``dev`` to ``main``

