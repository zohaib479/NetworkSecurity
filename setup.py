from setuptools import find_packages,setup
from typing import List
hyphen_e='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this  function returns the list of requirements
    '''
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[reqq.replace('\n',"") for reqq in req]
        req = [r for r in req if r.strip() != hyphen_e]
    return req
setup(
    name='Network-Security-Project',
    version='0.0.1',
    author='Zohaib_Rajput',
    author_email='zohaibrajput215@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)