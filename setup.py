from setuptools import setup,find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function will read the requiremnts.txt file and convert it into list of str
    '''
    Hypen_e_dot = '-e .'
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        [req.replace('\n','') for req in requirements]
    if Hypen_e_dot in requirements:
        requirements.remove(Hypen_e_dot)
    return requirements
setup(name='KS_1',version='0.0.1',author='Sasank',author_email='sasank19882000@gmail.com',packages=find_packages(),install_requires=get_requirements('requirements.txt'))