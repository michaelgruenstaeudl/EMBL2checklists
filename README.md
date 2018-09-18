*EMBL2checklists*
===================
Converts EMBL- or GenBank-formatted flatfiles to submission checklists (i.e., tab-separated spreadsheets) for submission to [ENA](http://www.ebi.ac.uk/ena) via the interactive [Webin submission system](https://www.ebi.ac.uk/ena/submit/sra/#home).

## INPUT, OUTPUT AND PREREQUISITES
-------------------------------
* Input: EMBL- or GenBank-formatted flatfile
* Output: tab-separated spreadsheet ("checklist")
* Prerequisites: Input flatfiles must have the DNA marker name (e.g., "matK", "ITS") as qualifier value for any of the defined key_features ("gene", "note", "product" or "standard_name").

## FEATURES
--------
* Foo
* Bar
* Baz

## EXAMPLE USAGE
----------------
#### Commandline Interface
```
python2 scripts/EMBL2checklists_CMD.py \
-i example/example_trnKmatK.embl \
-o example/example_trnKmatK.tsv \
-c trnK_matK \
-e no
```
#### GUI Interface
```
python2 scripts/EMBL2checklists_GUI.py
```

## CHANGELOG
###### Version 0.0.5 (2018.09.18)
* Code cleanup
###### Version 0.0.4 (2018.09.17)
* Major revision of code
###### Version 0.0.3 (2018.09.07)
* Various improvements of code
* Inclusion of GUI written by Yannick Hartmaring
###### Version 0.0.2 (2018.05.22)
* Generated separate function to extract charset symbols
* Updated README
###### Version 0.0.1 (2018.05.16)
* Added example input and example output
* Added setup.py
