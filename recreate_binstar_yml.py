
import os
import sys
import yaml

UPLOAD_ACCOUNT = None
CHANNEL = 'dev'

def make_template(package_name):
    binstar_yml_template = """

## The package attribure specifies a binstar package namespace to build the package to.
## This can be specified here or on the command line
package: {}

## You can also specify the account to upload to,
## you must be an admin of that account, this
## defaults to your user account
user: {}

#===============================================================================
# Build Matrix Options
# Thes options may be a single item, a list or empty
# The resulting number of builds is [platform * engine * env]
#===============================================================================

## The platforms to build on.
## platform defaults to linux-64
platform:
 - linux-64
 - osx-64
#  - linux-32
## The engine are the inital conda packages you want to run with
engine:
 - python=2
 - python=3
## The env param is an environment variable list
# engine:
#  - MY_ENV=A CC=gcc
#  - MY_ENV=B

#===============================================================================
# Scrip options
# Thes options may be broken out into the before_script, script and after_script
# or not, that is up to you
#===============================================================================

## Run before the script
# before_script:
#   - echo "before_script!"
## Put your main computations here!
script:
  - conda build .
## This will run after the script regardless of the result of script
## BINSTAR_BUILD_RESULT=[succcess|failure]
# after_script:
#   - echo "The build was a $BINSTAR_BUILD_RESULT" | tee artifact1.txt
## This will be run only after a successfull build
# after_success:
#   - echo "after_success!"
## This will be run only after a build failure
# after_failure:
#   - echo "after_failure!"

#===============================================================================
# Build Results
# Build results are split into two categories: artifacts and targets
# You may omit either key and stiff have a successfull build
# They may be a string, list and contain any bash glob
#===============================================================================

## Build Artifacts: upload anything you want!
## Your build artifacts will be put into the website
## http://artifacts.build.binstar.info/USERNAME/PACKGE_NAME/BUILD_NO
## You can store all logs or any derived data here
## Remember, the site http://artifacts.build.binstar.info is NOT secure and does not
## require a user to log in to view
# build_artifacts:
#   - *.log

## Build Targets: Upload these files to your binstar package
## build targets may be a list of files (globs allows) to upload
## The special build targets 'conda' and 'pypi' may be used to
## upload conda builds
## e.g. conda is an alias for /opt/anaconda/conda-bld/<os-arch>/*.tar.bz2
build_targets:
 files: conda
 channels: {}
    """.format(package_name, UPLOAD_ACCOUNT, CHANNEL)
    return binstar_yml_template

def write_yml(build_folder, package_name):
    # with open(os.path.join(build_folder, 'meta.yaml')) as f:
    #     yaml_file = yaml.load(f)
    #     package_name = yaml_file['package']['name']
    print('package_name: {}'.format(package_name))
    with open(os.path.join(build_folder, '.binstar.yml'), 'w') as f:
        f.write(make_template(package_name))
    pass


def make_version_ymls(root_folder):
    releases_folder = os.path.join(root_folder, 'releases')
    for package_name in os.listdir(releases_folder):
        package_folder = os.path.join(releases_folder, package_name)
        for version_name in os.listdir(package_folder):
            version_folder = os.path.join(package_folder, version_name)
            if 'meta.yaml' in os.listdir(version_folder):
                write_yml(version_folder, package_name)


def make_master_ymls(root_folder):
    root_folder = os.path.join(root_folder, 'master')
    for member in os.listdir(root_folder):
        if os.path.isdir(os.path.join(root_folder, member)):
            write_yml(os.path.join(root_folder, member), member)


def main(root_folder):
    make_master_ymls(root_folder)
    make_version_ymls(root_folder)
    # find_build_folder(root_folder)


if __name__ == "__main__":
    UPLOAD_ACCOUNT = sys.argv[1]
    try:
        CHANNEL = sys.argv[2]
    except IndexError:
        # use the default channel
        pass
    main(os.getcwd())
