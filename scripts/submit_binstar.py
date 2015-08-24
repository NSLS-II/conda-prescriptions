

import os
from collections import defaultdict

packages_to_submit = [
    ('scikit-xray', ['dev']),
    ('metadatastore', ['v0.1.0']),
    ('filestore', ['v0.1.0']),
    ('dataportal', ['v0.1.0']),
]

if __name__ == "__main__":
    import subprocess
    recipes_path = os.path.abspath('../')
    for package, versions in packages_to_submit:
        for version in versions:
            recipe_path = os.path.join(recipes_path, 'recipes', package, version)
            # subprocess.check_output(['anaconda-build', 'submit', recipe_path],
            #                         shell=True)
            output = subprocess.check_output('anaconda-build submit %s' %
                                             recipe_path, shell=True)
            print(output)
