Goal
-----
Produce journal tables to know if a journal publication has recquired Article Processing charges (APC)


output tables
---------------

## openapc_journals.csv

desciption

non hybrid journals inside openapc database, where for each years we have calculated the mean of APC cost

columns

journal_fill_title, 2015, 2016, 2017, 2018, 2019, 2020, issn_print, issn_electronic


## doaj_apc_journals.csv

description

a list of APC journals indexed in  DOAJ with APC informations

columns

Journal title, Journal ISSN (print version), Journal EISSN (online version),	APC amount	Currency


## openapc_dois.csv

description

simple list of DOIs inside openapc.

columns
doi, apc_amount_euros, institution


