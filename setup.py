from setuptools import find_packages,setup

def get_requirements(file_path:str)->[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')


    return requirements


setup(
   name="Xray",
   version="0.0.1",
   author="Trevor Serem",
   author_email="trevorserem53@gmail.com",
   install_requires=get_requirements("./requirements_dev.txt"),
   packages=find_packages(),




)