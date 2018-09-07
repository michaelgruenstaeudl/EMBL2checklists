*EMBL2checklists*
===================
Converts EMBL flatfiles to submission checklists (i.e., tab-separated spreadsheets) for submission to [ENA](http://www.ebi.ac.uk/ena) via the [Webin submission system](https://www.ebi.ac.uk/ena/submit/sra/#home).

INPUT
-----
* EMBL-formatted flatfile

PREREQUISITES
-------------
* Input files must have the name of the DNA marker (e.g., "matK", "ITS") as qualifier value for a feature named "gene", "note" or "standard_name"

FEATURES
-------------
* Checks if the type of DNA marker specified by the user is indeed present in the embl-input file (specifically in as qualifier value for a qualifier named "gene", "note" or "standard_name")

EXAMPLE USAGE
-------------

###### Checklist 'trnK_matK'
```
python2 scripts/EMBL2checklists_CMD.py
-e examples/input/matK.embl
-o examples/output/matK_SubmissionChecklist.tsv
-c trnK_matK
```

###### Checklist 'IGS'
```
python2 scripts/EMBL2checklists_CMD.py
-e examples/input/trnL-trnF.embl
-o examples/output/trnL-trnF_SubmissionChecklist.tsv
-c IGS
```

CHANGELOG
---------
###### Version 0.0.3 (2018.09.07)
* Various improvements of Python code
* GUI written by Yannick Hartmaring
###### Version 0.0.2 (2018.05.22)
* Generated separate function to extract charset symbols
* Updated README
###### Version 0.0.1 (2018.05.16)
* Added example input and example output
* Added setup.py
