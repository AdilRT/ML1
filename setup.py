# setup.py- responsible in creating my ML app as a package and you can instll this package in another project and also deploy in pypi
# building our app as a package
# run setup.py to build a package

# - **`setuptools`** is a powerful Python library that simplifies the packaging of Python projects.
# - **`setup()`** is the main function used to define your package details.
# - **`find_packages()`** automatically discovers all packages (folders with `__init__.py`) in your project directory.

# - This tells setuptools to automatically find all packages and sub-packages to include in the distribution.
# - For example, if you have: mlproject/init.py, data/init.py, models/init.py

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Aadil',
    author_email='adiltuladhar77@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']
    install_requires=get_requirements('requirement.txt')

)
