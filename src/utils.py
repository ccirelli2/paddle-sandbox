"""
Utility functions
"""
import os
import logging
import yaml
import git

# Settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def load_config(directory: str = None, filename: str = 'config.yaml'):
    """
    Load configuration from a YAML file.
    """
    if not directory:
        directory = git.Repo('.', search_parent_directories=True).working_tree_dir
    assert os.path.isfile(os.path.join(directory, filename)), f'Not a file: {filename}'
    path = os.path.join(directory, filename)

    with open(path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    logger.info(f"Config file loaded successfully")
    return config



if __name__ == '__main__':
    load_config()
