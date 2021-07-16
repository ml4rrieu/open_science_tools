import pandas as pd

##___________________ from openapc extract DOI, APC cost and insitution
# df = pd.read_csv("./source/openapc.csv")
# print("nb of item ", len(df))
# df = df[ df["doi"].notna()]
# print("nb of item w dois", len(df))
# openapc = pd.DataFrame({"doi" : df["doi"].str.lower(),  "apc_amount_euros" : df["euro"], "institution" : df["institution"]})
# openapc.to_csv("openapc_dois.csv", index = False)

#exit()


#____________________ from DOAJ extract j title, issn eissn and apc amount and currency
# nb of journal w APC in DOAJ {2021-07 : 4747, 2020-11 : 4259}

df = pd.read_csv("./source/journalcsv__doaj_20210715_1535_utf8.csv")
doaj_w_apc = df.loc[ df["APC"] == "Yes"]
doaj_w_apc = doaj_w_apc[["Journal title", "Journal ISSN (print version)", "Journal EISSN (online version)", "APC amount"]]

# 2021-16 column APC amount contain amount and currency
def extract_currency(row) :
	price_curren = str(row["APC amount"])
	cuta = price_curren.split(";") 

	if " " in cuta[0] : 
		cutb = cuta[0].split(" ")
		return cutb[1]
	else : 
		return cuta[0]
		
doaj_w_apc["APC currency"] = df.apply(lambda row : extract_currency(row), axis = 1)

def extract_price(row) :
	price_curren = str(row["APC amount"])
	cut = price_curren.split()
	return cut[0]
doaj_w_apc["APC amount"] = df.apply(lambda row : extract_price(row), axis = 1)


print("nb of apc journal in doaj", len(doaj_w_apc))
doaj_w_apc.to_csv("doaj_apc_journals.csv", index = False)
exit()
