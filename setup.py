# this will make your entire ml application to be used as an package
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    #this function retunr the list of requirements
    requirements = []
    HYPEN_E_DOT = '-e.'
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name = 'mlproject',
version = '0.0.1',
author= 'Harsh',
author_email= 'harsh.vardhan7695@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)