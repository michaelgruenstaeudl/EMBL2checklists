#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Class for custom exceptions
'''

###############
# AUTHOR INFO #
###############
__author__ = 'Michael Gruenstaeudl <m.gruenstaeudl@fu-berlin.de>,\
              Yannick Hartmaring <yanjo@zedat.fu-berlin.de>'
__copyright__ = 'Copyright (C) 2016-2018 Michael Gruenstaeudl'
__info__ = 'EMBL2checklists'
__version__ = '2018.09.17.2300'

#################################
# implemented exception by now: #
#################################
# MyException                    : default error spec; currently unused
# FileParsingError               : raise when the input file was not successfully parsed
# IncorrectInputFileformat       : raise when the inputfile is not in the correct fileformat
# DataParsingError               : raise when the input data was not successfully parsed
# ChecklistTypeUnknown           : raise when the seleceted Checklist type is not known yet
# MinimalPrerequisitesNotMet     : raise when the minimal prerequisites not met with the known minimal prerequisites for specific checklist type
# UnspecifiedError               : raise when none of the existing error specs fit

###########
# CLASSES #
###########
class MainException():
    def __str__(self):
        return(self.value)

    def getErrorNumber(self):
        return str(self.number)

    def getErrorName(self):
        return self.name

class MyException(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 1
        self.name = "MyException"
       
class FileParsingError(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 2
        self.name = "FileParsingError"

class IncorrectInputFileformat(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 3
        self.name = "IncorrectInputFileformat"

class DataParsingError(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 4
        self.name = "DataParsingError"

class ChecklistTypeUnknown(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 5
        self.name = "ChecklistTypeUnknown"

class MinimalPrerequisitesNotMet(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 6
        self.name = "MinimalPrerequisitesNotMet"

class UnspecifiedError(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 404
        self.name = "UnspecifiedError"
