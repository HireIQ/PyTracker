from setuptools import setup, find_packages


setup(
    name='pytracker',
    version='0.2.1',
    description='Python APIs for Pivotal Tracker',
    url='http://code.google.com/p/pytracker/',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    license="Apache"
)

