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
-e examples/input/trnL-trnF.embl
-o examples/output/trnL-trnF_SubmissionChecklist.tsv
-c IGS
```


TO DO
-----

###### 1. Have the code automatically write the column names in the output
* See ´examples/Checklists_empty/´ for examples on what a final (but empty) checklist is supposed to look like

Example:
After the following code snippet, the variable `out_string` is a tab-delimited table. The output needs to have a standardize name for each column included (i.e., it needs to have a title row). The column names should - for now - be identical to the variable names of `out_list`.
```
        out_list = [entrynumber,
                    organism_name,
                    env_sam,
                    gene1,
                    g1present,
                    gene2,
                    g2present,
                    isolate,
                    spec_vouch,
                    country,
                    sequence
                    ]
        out_string = '\t'.join(out_list) + '\n'
```

###### 2. An error in processing a sequence should break only the iteration of the loop, not the entire code execution.

###### 3. Not all qualifiers of a gene have the name `'gene'`. Sometimes they are named `'note'` or `'standard_name'`. Adjust code to allow this.

###### 4. Write untitests for the functions in `ChecklistOps.py`

###### 5. Have the code automatically add non-mandatory qualifiers as separate columns
* Ensure that all features that are not mandatory are added as separate columns into the checklist output (and not dropped, as they are now)

###### 6. Write a GUI interface for input
* The GUI should consist of just one Window, where all functions are immediately visible; the GUI should not have any dropdown-menus. In general, the simpler the interface, the better.


CHANGELOG
---------
###### Version 0.0.2 (2018.05.22)
* Generated separate function to extract charset symbols
* Updated README
###### Version 0.0.1 (2018.05.16)
* Added example input and example output
* Added setup.py
