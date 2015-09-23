Note that this is an attempt to simplify our deployment strategy by explaining
it, not propose a new deployment strategy or make things more complicated then
they already are.

Proposed deployment strategy for NSLS-II
----------------------------------------
Our beamline scientists complain that we do not have a stable software
deployment that they can roll back to when things go sideways. As things will
invariably go sideways, their complaints are well taken.  To provide a stable
software deployment we should provide a stable metapackage for each beam cycle
with exact software versions pinned.  Bugfixes should

#. result in an update to this metapackage
#. the build number should be incremented by one
#. the metapackage should be rebuilt and uploaded to conda.nsls2.bnl.gov/latest
#. all beamlines should be updated to this latest stable metapackage on beam
   shutdown days

NSLS-II has `three cycles per year <https://www.bnl.gov/ps/proposal-cycles.php>`_:

#. Spring
#. Summer
#. Fall

We should provide a stable metapackage for each of those cycles that are
versioned as '{{ year }}-{{ cycle_number }}'.

For this next cycle (Fall 2015), consider this as an example of a proposed
stable metapackage ::

    package:
      name: collection
      version: '2015-3'

    build:
      number: 1


    requirements:
      run:
        - python ==3.4
        - openpyxl
        - matplotlib >=1.5.0rc1
        # sort of our deps
        - pyolog ==v4.0.0.post5+g1a24409
        - channelarchiver ==v0.0.5.post6
        - pyepics ==v3.2.4.post19+g763d30
        - lmfit ==0.9.0rc1.post0
        # our data collection/retrieval deps
        - bluesky ==0.2.0
        - ophyd ==0.1
        - dataportal ==0.2.2
        - metadatastore ==0.2.0
        - filestore ==0.2.0
        # our data exploration/analysis/visualization deps
        - album >=v0.0.1
        - scikit-xray >=v0.0.5
        - xray-vision >=v0.0.3


Once a cycle begins, this stable metapackage will **only** be updated for
bugfixes.

**Example 1.** Consider a bugfix to metadatastore. The stable
metadatastore version according to the above metapackage is v0.2.0.  If there
have been no new features added to metadatastore, then it will still be minor
version 2.  Once the bugfix lands in master, metadatastore should be tagged at
v0.2.1, built and uploaded to conda.nsls2.bnl.gov/latest and the above
metapackage should have its build number bumped to 2 and the metadatastore
version changed to v0.2.1. The new metapackage should be deployed to each of
the beamlines during our 'software update day'

**Example 2.** Consider a bugfix to dataportal.  We are currently undergoing
some API reconsiderations for dataportal and so are expecting **new** features
to land during this next cycle (Fall 2015).  As soon as new features start
landing in dataportal, all of those features should be considered to be in
minor version 3 of dataportal and should not be considered part of the stable
metapackage for the Fall 2015 cycle at NSLS-II.  Lets, for the sake of
argument, assert that a bug has been discovered in existing code in dataportal.
This bugfix should be backported to dataportal v0.2.2 and dataportal should be
retagged at v0.2.3, built and uploaded to conda.nsls2.bnl.gov/latest. The
2015-3 collection metapackage should have its build number bumped to 3 and the
dataportal version changed to ==v0.2.3 and then be rebuild and uploaded to
conda.nsls2.bnl.gov/latest. The new metapackage should be deployed to each of
the beamlines during our 'software update day'

**Example 3.** Consider any library in the "sort of our deps" category of
requirements above. Any bugfixes to these libraries probably will reside on our
fork of that library in the NSLS-II github organization.  Bugfixes should
result in that library being rebuilt and uploaded to conda.nsls2.bnl.gov/latest.
The metapackage build number should be incremented by 1, the library which just
got a bugfix should have its version correctly set, the metapackage should be
rebuilt and uploaded to conda.nsls2.bnl.gov/latest. The new metapackage should
be deployed to each of the beamlines during our 'software update day'

**Example 4.** Consider any library in the "data exploration/analysis/visualization"
category of requirements above.  These are likely non-critical libraries for
data collection and so should not be strictly pinned to a version, but expect
at least a base version.
