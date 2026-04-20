from setuptools import setup, find_packages
from typing import List

file_path = "requirements.txt"

def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            
            for line in lines:
                requirement = line.strip()
                
                # Skip editable install
                if requirement == "-e .":
                    continue
                
                if requirement:
                    requirements.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirements


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Amey Yarnalkar",
    packages=find_packages(),
    install_requires=get_requirements(file_path)
)