import setuptools

setuptools.setup(
    name='otcbtc_client',
    version='0.1.0',
    author='Gimo',
    author_email='self@gimo.me',
    description='OTCBTC SDK for Python',
    url='https://github.com/masakichi/otcbtc-client',
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    install_requires=[
    'requests >=2.11, <3.0a0',
    ]
)