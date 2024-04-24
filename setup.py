from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith('-e'):
                requirements.append(line)
    return requirements


setup(
   name="Xray",
   version="0.0.1",
   author="Trevor Serem",
   author_email="trevorserem53@gmail.com",
   install_requires=get_requirements("C:\\Users\hp\Desktop\\deeplearningproject\\requirements_dev.txt"),
   packages=find_packages(),




)