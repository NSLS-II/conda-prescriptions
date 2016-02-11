import os

BUILD_TEMPLATE = """
mkdir -p $PREFIX/etc
ETC=$PREFIX/etc

{resources}

# clean up after self
unset ETC
"""


RESOURCE_TEMPLATE = """echo "# {app_name} configuration
# installed by {beamline_id}_configuration
# DO NOT EDIT
{fields}" >$ETC/{app_name}.yml

"""

information = {
    'csx1': {
        'metadatastore': {
            'host': 'xf23id-broker',
            'database': 'datastore2',
            'port': 27017,
            'timezone': 'US/Eastern',
        },
        'filestore': {
            'host': 'xf23id-broker',
            'database': 'filestore',
            'port': 27017,
        },
        'archiver': {
            'url': 'https://xf23id-ca.cs.nsls2.local:8888/cgi-bin/ArchiveDataServer.cgi',
            'db': '"$ETC"/pv_mapping.sql',
        }
    }
}

for beamline_name, beamline_resources in information.items():
    resources = ""
    for lib_name, lib_info in sorted(beamline_resources.items()):
        resource_info = {'app_name': lib_name, 'beamline_id': beamline_name}
        fields = ''
        for lib_key, lib_value in sorted(lib_info.items()):
            fields += """%s: %s
""" % (lib_key, lib_value)
        resource_info['fields'] = fields
        resources += RESOURCE_TEMPLATE.format(**resource_info)
    build_path = os.path.join(os.getcwd(), beamline_name.upper(), 'configuration', 'build.sh')
    print(BUILD_TEMPLATE.format(resources=resources))
    with open(build_path, 'w') as f:
        f.write(BUILD_TEMPLATE.format(resources=resources))
