import pandas as pd

##___________________ from openapc extract DOI, APC cost
df = pd.read_csv("./source/openapc.csv")
print("nb of item ", len(df))
df = df[ df["doi"].notna()]
print("nb of item w dois", len(df))
openapc = pd.DataFrame({"doi" : df["doi"].str.lower(),  "apc_amount_euros" : df["euro"], "institution" : df["institution"]})
openapc.to_csv("dois_in_openapc.csv")

exit()


#____________________ from DOAJ extract j title, issn eissn and apc amount and currency
#APC journal in DOAJ in 2020-11 : 4259 
"""
df = pd.read_csv("./source/doaj_journals.csv")
doaj_w_apc = df.loc[ df["Journal article processing charges (APCs)"] == "Yes"]
doaj_w_apc = doaj_w_apc[["Journal title", "Journal ISSN (print version)", "Journal EISSN (online version)", "APC amount", "Currency"]]

print("nb of apc journal in doaj", len(doaj_w_apc))
doaj_w_apc.to_csv("apc_journals_in_doaj.csv")
exit()
"""