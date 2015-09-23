.condarc should look like this ::

    channels:
      - beamline
      - latest
      - anaconda

    create_default_packages:
      - pip

    envs_dirs:
      # if you put ~/mc/envs first then the user at the beamline can create environments
      # with conda create -n env_name
      # unanswered questions: if there is an environment in /opt/conda_envs
      # called "analysis", what happens if you 'conda create -n analysis'?
      # Does it create a new environment in ~/mc/envs? Or does conda recognize
      # that there is already one in /opt/conda_envs and blow up?
      - ~/mc/envs
      - /opt/conda_envs
