import pandas as pd

"""
STEP 1 from openapc database extract every journals with the amount paid in APC for each years.
STEP 2 if apc in 2015 and in 2017 and no value in 2016 then fill 2016 with 2015 value (assuming a journal cannot flip 2 times less than 5 years)
"""


#____STEP 1____ get journal APC info from openapc per year
"""
df = pd.read_csv("./source/openapc.csv")
print(f"nb of articles w APC {len(df.index)}")

#extract csv per year to visualize data
#year = 2012
#snapshot = df[ df["period"] == year]
#snapshot.to_csv(f"openapc_{year}.csv")
#print(len(snapshot))

df = df.loc[ df["is_hybrid"] == False]
issns_l = df["issn_l"].tolist()
issn_price = dict.fromkeys(issns_l) #remove duplicate
print(f"nb of non hybrid journals finded\t{len(issn_price)}\n\n")

for i, item in enumerate(issn_price) : 
	issn_price[item] = []
	for year in range(2015, 2021):
		mean = df.loc[ (df["issn_l"] == item) & (df["period"] == year), "euro" ].mean()
		issn_price[item].append(mean)
	
	#if i > 20 : break

	#print(f"the apc average for this issn {item}  is {mean}€")

out = pd.DataFrame.from_dict(issn_price, orient='index')
out.to_csv("./source/temp_journals_in_openapc.csv") # !!caution!! the issn_l column is the index
exit()
"""


#____STEP 2____ fill NA values if appropriate
df = pd.read_csv("./source/temp_journals_in_openapc.csv")

# overwrite columns name
temp_col = [str(y) for y in range(2015, 2021)]
col = ["issn_l"]
col.extend(temp_col) 
df.columns = col
#print(col)
print(f"nb of journals\t{len(df)}")

#remove journals where APC is NA for all years
df.dropna(subset = temp_col, how = 'all', inplace = True)
print(f"nb of journals w value in period\t{len(df)}")


# get data as dict
data = df.to_dict("index")

for index, val in data.items() :
	bottom_val, up_val = None, None
	nan_idx = [year for year in range(2015, 2021) if pd.isna(val[str(year)])]

	#get the first year were value is present
	for year in range(2015, 2021) :
		if pd.notna(val[str(year)]) : 
			bottom_val = year
			break

	#get the last year were value is present
	for year in range(2020,2014, -1) :
		if pd.notna( val[str(year)]) : 
			up_val = year
			break

	# if nan between bottom_val and up_val then duplicate bottom_val
	#print(f"{val}\n{bottom_val}\tbottom_val\n{up_val}\tup_val\n{nan_idx}\tnan_idx\n\n")
	if nan_idx :
		for year in nan_idx : 
			if year > bottom_val and year < up_val : 
				val[str(year)] = bottom_val
				#print(f"{year} mean is added {val}")
				
				
	#if index > 20 : break;
# view piece of data
"""for index, val in data.items() : 
	print(index, val)
	if index > 5 : break"""

journals = pd.DataFrame.from_dict(data, orient="index")

#ajout des colonnes issn_print et issn_electronic et journal_title
openapc = pd.read_csv("./source/openapc.csv", usecols=["issn_l", "issn", "issn_print", "issn_electronic", "journal_full_title"])
openapc.drop_duplicates(subset="issn_l", inplace = True)
journals = journals.merge(openapc, how="left", on= "issn_l")
#print(journals.info())


#reorder columns
temp_col.insert(0, "journal_full_title")
temp_col.extend(["issn", "issn_print", "issn_electronic", "issn_l"])
journals = journals[temp_col] 
journals.to_csv("openapc_journals.csv", index=False)






#2290