import pandas as pd

openapc = pd.read_csv("journal_apc_per_year.csv",index_col=False)
#openapc = openapc.loc[ openapc["2015"].notna() ]

openapc_issns = openapc["issn"].tolist()
print(f"nb of journals in OpenApc\t{len(openapc_issns)}")


doaj = pd.read_csv("doaj_journals.csv", index_col=False,quotechar = "\"", encoding = 'utf8')
print(f"nb of journals in DOAJ\t{len(doaj.index)}")
doaj_w_apc = doaj.loc[ doaj["Journal article processing charges (APCs)"] == "Yes"]
print(f"nb of APC journals in DOAJ\t{len(doaj_w_apc.index)}")

doaj_apc_j_in_openapc = 0
for row in doaj_w_apc.itertuples() : 
	if row._4 in openapc_issns or row._5 in openapc_issns : 
		doaj_apc_j_in_openapc += 1

print(doaj_apc_j_in_openapc)
print("\n\nnb of daoj journal not in openapc", (len(doaj_w_apc.index) - doaj_apc_j_in_openapc))
