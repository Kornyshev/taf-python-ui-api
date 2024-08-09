import os

import pytest
from jproperties import Properties


def load_properties(file_path):
    config = Properties()
    with open(file_path, 'rb') as config_file:
        config.load(config_file)
    properties = {}
    for key, value in config.items():
        properties[key] = value.data
    return properties


@pytest.fixture(scope='session', autouse=True)
def load_env_variables():
    general_properties = load_properties('C:\\Projects\\taf-python-ui-api\\properties\\general.properties')
    standard_user_properties = load_properties('C:\\Projects\\taf-python-ui-api\\properties\\user.properties')

    for key, value in general_properties.items():
        os.environ[key] = value

    for key, value in standard_user_properties.items():
        os.environ[key] = value
