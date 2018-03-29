*embl2enachecklist*
===================

Converts EMBL flat files to ENA checklists (i.e., tab-separated spreadsheets) for submission to [ENA](http://www.ebi.ac.uk/ena) via [Webin](https://www.ebi.ac.uk/ena/submit/sra/#home).


FILE REQUIREMENTS
-----------------
All that is needed is a valid EMBL-formatted file.


GENERAL USAGE
-------------

###### Checklist 'genomic_CDS'
```
python2 scripts/embl2enachecklists_CMD.py 
-e examples/input/TestData_1.embl 
-o examples/output/TestData_1__checklist_genomicCDS.tsv 
-c genomic_CDS
```

###### Checklist 'rRNA'
```
python2 scripts/embl2enachecklists_CMD.py 
-e examples/input/TestData_1.embl 
-o examples/output/TestData_1__checklist_rRNA.tsv 
-c rRNA
```


TO DO
-----

###### 1. Have the CLMODE automatically add the colum names for the final checklists

###### 2. Have the CLMODE automatically add non-mandatory qualifiers as separate column
i.e., ensure that all features that are not mandatory are added as separate columns into the checklist output (and not dropped, as they are now)

###### 3. Write a GUI interface for input
* The GUI should consist of just one Window, where all functions are immediately visible; the GUI should not have any dropdown-menus. In general, the simpler the interface, the better.


CHANGELOG
---------
###### Version 0.0.1 (2018.03.29)
* foo
* bar
* baz
