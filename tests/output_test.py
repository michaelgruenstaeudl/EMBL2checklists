#!/usr/bin/env python
'''
Unit tests to compare actual and expected output
'''

#####################
# IMPORT OPERATIONS #
#####################
import unittest

# Add specific directory to sys.path in order to import its modules
# NOTE: THIS RELATIVE IMPORTING IS AMATEURISH.
# NOTE: COULD THE FOLLOWING IMPORT BE REPLACED WITH 'import EMBL2checklists'?
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'EMBL2checklists'))

import subprocess
import inspect

###############
# AUTHOR INFO #
###############
__author__ = 'Michael Gruenstaeudl <m.gruenstaeudl@fu-berlin.de>'
__copyright__ = 'Copyright (C) 2016-2018 Michael Gruenstaeudl'
__info__ = 'EMBL2checklists'
__version__ = '2018.09.25.1600'

#############
# DEBUGGING #
#############
import pdb
# pdb.set_trace()

####################
# GLOBAL VARIABLES #
####################

try:
    base_path = os.path.split(inspect.getfile(EMBL2checklists))[0] + '/'
except:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

script_rel_path = 'scripts/EMBL2checklists_CMD.py'
script_abs_path = os.path.join(base_path, script_rel_path)

e_mail = 'm.gruenstaeudl@fu-berlin.de'  # Please enter your email address here.

###########
# CLASSES #
###########

class OutputTestCases(unittest.TestCase):
    ''' Tests to evaluate miscellaneous operations'''


    def test_actual_vs_expected_output_ETS(self):
        ''' Assert that the actual and the expected output for checklist 
        `ETS` are identical. If they are not, show their difference. '''
        actual_inp = 'example_ETS.embl'
        expect_otp = 'example_ETS.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c ETS', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


    def test_actual_vs_expected_output_gene_intron(self):
        ''' Assert that the actual and the expected output for checklist 
        `gene_intron` are identical. If they are not, show their difference. '''
        actual_inp = 'example_gene_intron.embl'
        expect_otp = 'example_gene_intron.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c gene_intron', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


    def test_actual_vs_expected_output_IGS(self):
        ''' Assert that the actual and the expected output for checklist 
        `IGS` are identical. If they are not, show their difference. '''
        actual_inp = 'example_IGS.embl'
        expect_otp = 'example_IGS.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c IGS', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


    def test_actual_vs_expected_output_ITS(self):
        ''' Assert that the actual and the expected output for checklist 
        `ITS` are identical. If they are not, show their difference. '''
        actual_inp = 'example_ITS.embl'
        expect_otp = 'example_ITS.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c ITS', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


    def test_actual_vs_expected_output_rRNA(self):
        ''' Assert that the actual and the expected output for checklist 
        `rRNA` are identical. If they are not, show their difference. '''
        actual_inp = 'example_rRNA.embl'
        expect_otp = 'example_rRNA.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c rRNA', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


    def test_actual_vs_expected_output_trnK_matK(self):
        ''' Assert that the actual and the expected output for checklist 
        `trnK_matK` are identical. If they are not, show their difference. '''
        actual_inp = 'example_trnK_matK.embl'
        expect_otp = 'example_trnK_matK.tsv'
        actual_otp = sys._getframe().f_code.co_name  # Name of this function
        actual_inp_rel_path = os.path.join('example/input/', actual_inp)
        actual_inp_abs_path = os.path.join(base_path, actual_inp_rel_path)
        actual_otp_rel_path = os.path.join('example/temp/', actual_otp)
        actual_otp_abs_path = os.path.join(base_path, actual_otp_rel_path)
        expect_otp_rel_path = os.path.join('example/output/', expect_otp)
        expect_otp_abs_path = os.path.join(base_path, expect_otp_rel_path)
        cmd_list = ['python2', script_abs_path,
                    '-i', actual_inp_abs_path,
                    '-o', actual_otp_abs_path,
                    '-c trnK_matK', '-e no'
                   ]
        try:
            subprocess.check_output(' '.join(cmd_list), shell=True)
        except subprocess.CalledProcessError as e:
            print e.output
        expected_str = open(expect_otp_abs_path).read()
        if os.path.isfile(actual_otp_abs_path): # Check if actual output exists
            actual_str = open(actual_otp_abs_path).read()
            # Important: Remove actual output so that lines from 
            # subsequent tests are not appended, rendering actual and 
            # expected different.
            os.remove(actual_otp_abs_path)
        else:
            print 'EMBL2checklists TESTING ERROR: actual_str not found.'
        self.assertTrue(isinstance(expected_str, str),
                'Not a string: ' + expect_otp_abs_path)
        self.assertTrue(isinstance(actual_str, str),
                'Not a string: ' + actual_otp_abs_path)
        self.assertMultiLineEqual(expected_str, actual_str)


#############
# FUNCTIONS #
#############

########
# MAIN #
########

if __name__ == '__main__':
    unittest.main()
