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

