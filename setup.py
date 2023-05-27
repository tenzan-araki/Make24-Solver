import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()


version_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__),'VERSION.txt'))
with open(version_path, 'r') as fd:
    version = fd.read().rstrip()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')
with open(README_PATH) as readme_file:
    README = readme_file.read()

setup(
    name="make24",
    version=version,
    description="A repository for the code used to solve Make 24",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/tenzan-araki/Make24-Solver.git",
    author="Tenzan Araki",
    author_email="taraki@ethz.ch",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    keywords="24",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.7"
)
