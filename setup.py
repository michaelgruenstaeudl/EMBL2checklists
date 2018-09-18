import os
import glob
import unittest
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='*_test.py')
    return test_suite

setup(
    name='EMBL2checklists',
    version='0.0.5',
    description='Converts EMBL- or GenBank-formatted flatfiles to submission checklists (i.e., tab-separated spreadsheets) for submission to ENA via the interactive Webin submission system',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
        ],
    keywords='DNA sequence submission to ENA',
    url='https://github.com/michaelgruenstaeudl/EMBL2checklists',
    author='Michael Gruenstaeudl, PhD',
    author_email='m.gruenstaeudl@fu-berlin.de',
    license='GPLv3',
    packages=['EMBL2checklists'], # So that the subfolder 'EMBL2checklists' is read immediately.
    #packages = find_packages(),
    install_requires=['biopython', 'argparse'],
    scripts=glob.glob('scripts/*'),
    test_suite='setup.my_test_suite',
    include_package_data=True,
    zip_safe=False
)
