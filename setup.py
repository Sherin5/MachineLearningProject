from setuptools import setup
from typing import List

PROJECTNAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Sherin Thomas"
DESCRIPTION="This is a housing price prediction app"
REQUIREMENTS_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """
    This function will return the list of packages mentioned in requirements.txt

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
    name =PROJECTNAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=['housing'],
    install_requires=get_requirements_list()

)

