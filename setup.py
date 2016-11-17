from setuptools import setup
import os

top_dir, _ = os.path.split(os.path.abspath(__file__))

with open(os.path.join(top_dir, 'VERSION')) as f:
    version = f.readline().strip()

setup(
    name = 'lfsr',
    version = version,
    description = 'Linear Feedback Shift Register toolkit.',
    author = 'Grzegorz Krason',
    author_email = 'grzegorz@krason.biz',
    url = 'https://github.com/gergelyk/pylfsr',
    download_url = 'https://github.com/gergelyk/pylfsr/tarball/' + version,
    license = 'MIT',
    packages = ['lfsr'],
    package_data = {'': ['../VERSION']},
    keywords = 'lfsr prng random generator'.split(),
    classifiers = [],
)

