import os.path
# Always prefer setuptools over distutils
from setuptools import setup, find_packages


def read_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


here = os.path.dirname(__file__)
# Get the long description from the README file
long_description = read_text(os.path.join(here, 'README.md'))


def read_version_string(version_file):
    for line in read_text(version_file).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


version = read_version_string("utils/version.py")

requirements = read_text(os.path.join(here, 'requirements.txt')).splitlines()

setup(
    name='utils',
    version=version,
    description='Utils',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # The project's main homepage.
    url='https://github.com/aljeshishe/utils',
    author='Alexey Grachev',
    author_email='ax66@bk.ru',
    license='Apache License 2.0',
    classifiers=[
    ],
    keywords='utils',
    packages=['utils'],
    install_requires=requirements,
    # extras_require={
    #     's3': [
    #         'boto3>=1.9',
    #     ],
    #     'azure': [
    #         'azure-storage-blob>=2.0.1,<=2.1',
    #     ],
    #     'gs': [
    #         'google-cloud-storage>=1.13.2',
    #     ],
    # },
    # package_data={
    #     'clearml': ['config/default/*.conf', 'backend_api/config/default/*.conf']
    # },
    include_package_data=True,
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'clearml-init = clearml.cli.config.__main__:main',
    #         'clearml-data = clearml.cli.data.__main__:main',
    #         'clearml-task = clearml.cli.task.__main__:main',
    #     ],
    # },
)
