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

###### 1. foo

###### 2. baz

###### 3. baz
* foo bar baz
* foo bar baz
* foo bar baz


CHANGELOG
---------
###### Version 0.0.1 (2018.03.29)
* foo
* bar
* baz
