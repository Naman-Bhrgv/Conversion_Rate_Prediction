from setuptools import find_packages,setup

def get_req(file_path):

    req_list=[]

    with open(file_path) as file:

        requirements=file.readlines()
        
        requirements=[i.replace("\n","") for i in requirements]

        if '-e .' in requirements:

            requirements.remove('-e .')

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Naman',    
    author_email='nambhprac@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)

