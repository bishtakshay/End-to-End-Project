from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # return non-empty, non-comment requirement lines
    requirements = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
    return requirements

setup(
    name="endtoend",   # no spaces
    version="0.0.1",
    author="Akshay",
    author_email="akshaybisht07@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
