*embl2enachecklist*
===================
Converts EMBL flatfiles to submission checklists (i.e., tab-separated spreadsheets) for submission to [ENA](http://www.ebi.ac.uk/ena) via [Webin](https://www.ebi.ac.uk/ena/submit/sra/#home).


INPUT
-----
* EMBL flatfile


GENERAL USAGE
-------------

###### Checklist 'trnK_matK'
```
python2 scripts/embl2enachecklists_CMD.py 
-e examples/input/matK.embl
-o examples/output/matK_SubmissionChecklist.tsv 
-c trnK_matK
```

###### Checklist 'IGS'
```
python2 scripts/embl2enachecklists_CMD.py 
-e examples/input/rpl32_trnL.embl
-o examples/output/rpl32_trnL_SubmissionChecklist.tsv
-c IGS
```


TO DO
-----

###### 1. Have the CLMODE automatically add the colum names for the final checklists

###### 2. An error in processing a sequence should break only the iteration of the loop, not the entire code execution.

###### 3. Not all qualifiers of a gene have the name `'gene'`. Sometimes they are named `'note'` or `'standard_name'`. Adjust code to allow this.

###### 4. Convert the following sections to separate functions and write untitests for them:
* "3.1. Extraction of charset symbols", with the following input: `seq_record.features[1:]`, `['gene', 'note']`

###### 5. Have the CLMODE automatically add non-mandatory qualifiers as separate column
* Ensure that all features that are not mandatory are added as separate columns into the checklist output (and not dropped, as they are now)

###### 6. Write a GUI interface for input
* The GUI should consist of just one Window, where all functions are immediately visible; the GUI should not have any dropdown-menus. In general, the simpler the interface, the better.


CHANGELOG
---------
###### Version 0.0.1 (2018.05.16)
* Added example input and example output
* Added setup.py
