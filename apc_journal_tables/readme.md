# Goal

Produce journal tables to know if an article journal has recquired Article Processing charges (APC)


# Sources used

the folder `source` must contains two files : 

**doaj_journals.csv**

DOAJ dump at doaj.org/csv
(see also this [public-data-dump/](https://doaj.org/docs/public-data-dump/) )


**openapc.csv**

openapc dump
[github.com/OpenAPC/openapc-de/blob/master/data/apc_de.csv](https://github.com/OpenAPC/openapc-de/blob/master/data/apc_de.csv)



# code

`extract_part_of_csv.py` script to have smaller table than the sources

`get_journal_apc_info.py` script to get the mean of APC cost for each year

`is_doaj_jn_inside_openapc.py` curiosity : how many journals from DOAJ are present in OpenAPC


# produced files

**openapc_journals.csv**

non hybrid journals inside openapc database, where for each years we have calculated the mean of APC cost

columns

`journal_fill_title, 2015, 2016, 2017, 2018, 2019, 2020, issn_print, issn_electronic`



**doaj_apc_journals.csv**

A list of APC journals indexed in  DOAJ with APC informations

columns

`Journal title, Journal ISSN (print version), Journal EISSN (online version),	APC amount, APC currency`



**openapc_dois.csv**

simple list of DOIs inside openapc.

columns
`doi, apc_amount_euros, institution`



# see also

this repo contains some data on APC price evolutions

https://github.com/lmatthia/publisher-oa-portfolios/