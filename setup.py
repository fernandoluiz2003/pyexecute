from setuptools import setup, find_packages

setup(
    name='pyexecute',
    version='0.5.5',
    packages=find_packages(where='lib'),
    package_dir={'' : 'lib'},
    include_package_data=True,
    license='unlincense',
    description='Easy way to create a main.exe',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fernandoluiz2003/pyexecute',
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com',
    entry_points={
        'console_scripts': [
            'pyexecute=pyexecute.cli:main',
        ],
    },
)