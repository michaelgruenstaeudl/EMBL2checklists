#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Custom operations to generate ENA checklists
'''

#####################
# IMPORT OPERATIONS #
#####################
import Bio
import globalVariables as GlobVars
import MyExceptions as ME

###############
# AUTHOR INFO #
###############
__author__ = 'Michael Gruenstaeudl <m.gruenstaeudl@fu-berlin.de>,\
              Yannick Hartmaring <yanjo@zedat.fu-berlin.de>'
__copyright__ = 'Copyright (C) 2016-2018 Michael Gruenstaeudl'
__info__ = 'EMBL2checklists'
__version__ = '2018.09.17.2300'

#############
# DEBUGGING #
#############
import pdb
# pdb.set_trace()

###########
# CLASSES #
###########
class Checker:
    ''' This class contains functions to check the minimal requirements for a sequence record. '''

    def __init__(self):
        pass

    def checkMinimalFeaturePrerequisites(self, checklist_type, marker_abbrev):
        '''Various checks to see if the checklist type matches the marker abbreviations
        Args:
            checklist_type [string]: user input that contains checklist abbreviation
            marker_abbrev  [list]  : list of the abbreviations of the sequence record
        Returns:
            Boolean: True if it matched, False if not
        Raises:
            ME.MinimalPrerequisitesNotMet
        '''
        # VERY GENERAL CHECK: Check if at least one marker abbreviation matches any keyword across all implemented checklist types.
        if not any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_allChecklists):
            raise ME.MinimalPrerequisitesNotMet('WARNING: Not a single marker abbreviation matches any keyword across all implemented checklist types.')
            #return false

        # MORE SPECIFIC CHECK: Check if at least one marker abbreviation matches any keyword for the given checklist.
        try:
            if checklist_type == 'ETS' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_ETS):
                return True
            if checklist_type == 'ITS' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_ITS):
                return True
            if checklist_type == 'rRNA' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_rRNA):
                return True
            if checklist_type == 'trnK_matK' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_trnKmatK):
                return True
            if checklist_type == 'IGS' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_IGS):
                return True
            if checklist_type == 'gene_intron' and any(e in " ".join(marker_abbrev) for e in GlobVars.keywords_gene_intron):
                return True
        except:
            raise ME.MinimalPrerequisitesNotMet('WARNING: Not one marker abbreviation matches any keyword for the given checklist.')
            #return false
