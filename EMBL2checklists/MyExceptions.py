#!/usr/bin/env python
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
__version__ = '2018.09.07.1900'

#################################
# implemented exception by now: #
#################################
# MyException                   : should be removed in future
# FileNotExist                  : raise when the Inputfile not exists
# WrongInputFile                : raise when the inputfile is not in the correct format
# WrongOutputFile               : should be removed in future cause the program forms his own outputfile
# ParserError                   : raise when something went wrong while parsing the inputfile
# CheckListTypeNotKnownError    : raise when the seleceted Checklist type is not known yet
# MinimalPrerequisitesNotMet    : raise when the minimal prerequisites not met with the known minimal prerequisites for specific checklist type
# FeaturePrerequisutesNotMet    : raise when the feature prerequisites not met with the known feature prerequisites for specific checklist type
# ErrorNotFound                 : raise when non of the existing errors raise so the new error can be implemented to the code

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

class FileNotExist(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 2
        self.name = "FileNotExist"

class WrongInputFile(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 3
        self.name = "WrongInputFile"

class WrongOutputFile(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 4
        self.name = "WrongOutputFile"

class ParserError(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 5
        self.name = "ParserError"

class CheckListTypeNotKnownError(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 6
        self.name = "CheckListTypeNotKnownError"

class MinimalPrerequisitesNotMet(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 7
        self.name = "MinimalPrerequisitesNotMet"

class FeaturePrerequisutesNotMet(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 8
        self.name = "FeaturePrerequisutesNotMet"

class ErrorNotFound(Exception, MainException):
    def __init__(self, value):
        self.value = value
        self.number = 404
        self.name = "ErrorNotFound"
