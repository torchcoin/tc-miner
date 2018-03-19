from setuptools import setup

setup(
    name='tcminer',
    version='0.1',
    py_modules=['tcminer'],
    include_package_data=True,
    install_requires=[
        'click',
        'emoji',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        tcminer=tcminer:cli
    ''',
)
