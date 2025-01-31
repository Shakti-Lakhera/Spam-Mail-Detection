from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path)->List[str]:
    '''
       This function returns the list of all requirements
    '''
    requiremenst = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")] for req in requirements ]

    return requirements

setup = (
    name = 'Spam_Mail_Detection',
    version = '0.0.1',
    author = 'Shakti',
    author_email = 'imshaktilakhera@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt'),


)