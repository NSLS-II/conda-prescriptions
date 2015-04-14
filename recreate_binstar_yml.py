
import os
import sys
import re
import yaml

DEFAULT_CHANNEL = 'dev'

def safe_yaml_read(fpath, replace_str=''):
    """
    Reads a yaml file stripping all of the jinja templating markup

    Parameters
    ----------
    fpath : str
        Path to yaml file to sanitize

    replace_str : str
        String to replace the template markup with, defaults to ''.

    Returns
    -------
    yaml_dict : dict
        The dictionary with all of the jinja2 templating fields
        replaced with ``replace_str``.
    """
    with open(fpath, 'r') as f:
        lns = []
        for ln in f:
            # handle the jinja2 templating correctly
            if ln.split(':')[0] in ['version', 'string']:
                print('ln.split(":")[0]: {}'.format(ln.split(':')[0]))
                ln = re.sub(r'{[{%].*?[%}]}', '', ln)
            lns.append(ln)

    meta_dict = yaml.load(''.join(lns))
    return meta_dict

def get_package_name(fpath):
    with open(fpath, 'r') as f:
        lns = []
        for ln in f:
            split = ln.split()
            print('split: {}'.format(split))
            # handle the jinja2 templating correctly
            if len(split) >= 2 and split[0][:4] == 'name':
                return split[1]
    raise

def make_template(package_name, upload_acct, channel_name=None):
    if channel_name is None:
        channel_name = DEFAULT_CHANNEL
    binstar_yml_template = """package: {}
user: {}
platform:
 - linux-64
 - osx-64
engine:
 - python=2.7
script:
  - conda build . --python 2.7
build_targets:
 files: conda
 channels: main
---
platform:
 - linux-64
 - osx-64
engine:
 - python=3.4
script:
  - conda build . --python 3.4
build_targets:
 files: conda
 channels: main
 """.format(package_name, upload_acct, channel_name)
    return binstar_yml_template


def write_yml(build_folder, upload_acct, channel_name):
    package_name = get_package_name(os.path.join(build_folder, 'meta.yaml'))
    with open(os.path.join(build_folder, '.binstar.yml'), 'w') as f:
        f.write(make_template(package_name, upload_acct, channel_name))


def make_ymls(root_folder, upload_acct, channel_name):
    if 'meta.yaml' in os.listdir(root_folder):
        write_yml(root_folder, upload_acct, channel_name)
    else:
        for subfolder in os.listdir(root_folder):
            subfolder = os.path.join(root_folder, subfolder)
            if os.path.isdir(subfolder):
                make_ymls(subfolder, upload_acct, channel_name)


if __name__ == "__main__":
    try:
        upload_acct = sys.argv[1]
    except IndexError:
        print("you supplied no command line arguments. I have no idea where to"
              "upload your packages to. Please specify a user_account as the"
              "first command line argument after 'recreate_binstar_yml.py'")
        print("Usage: python recreate_binstar_yml.py user_account channel_name")
        print("Example: python recreate_binstar_yml.py edill main")
        sys.exit(1)

    try:
        channel_name = sys.argv[2]
    except IndexError:
        # use the default channel
        channel_name = None
    # make the yaml files
    make_ymls(os.getcwd(), upload_acct, channel_name)
