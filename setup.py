from setuptools import setup, find_packages

setup(
    name='archetype',
    version='1.0',
    author='Everton Gago',
    packages=find_packages(include=['src.*', 'tests.*']),
    namespace_packages=['src'],
    install_requires=open('requirements.txt').readlines(),
    tests_require=['pytest'],
    zip_safe=False
)
