from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = "-e ."

def get_requirements(filepath: str) -> List[str]:
    '''
    This function returns the requirements needed,
    in the form of a list.
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
        
    return requirements 
        
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Pawel Siurek',
    author_email='pawel.siurek77@gmail.com',
    packages=find_packages(),
    requires=get_requirements("requirements.txt")
)