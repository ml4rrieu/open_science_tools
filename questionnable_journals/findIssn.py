import requests, json, csv


def reqHal(title):
	url = "http://api.archives-ouvertes.fr/ref/journal/?q=title_t:\""+title+"\"&fl=title_s,issn_s,eissn_s"
	req = requests.get(url)
	req = req.json()
	try : 
		return req["response"]["docs"]
	except : 
		print("!! error with this title", title)
		return None
		

def reqCrossref(title):
	url = "http://api.crossref.org/journals?query="+title
	req = requests.get(url)
	req = req.json()
	# print( json.dumps(req, indent=4))
	try : 
		req['message']['items']
	except : 
		print('\n!! problem w this title >>',title)
		return None 
	# return only item with issn data
	else : 
		buff = []
		for item in req['message']['items'] : 
			if item['ISSN'] : 
				buff.append(item)

		return buff


def titlesComparison(title, result):
	title = title.lower()
	issnList = []
	itemNbMatch = []
	i = 0
	for item in result : 
		CRtitle = item['title'].lower()
		if title == CRtitle : 
			add = True
			for issn in item['ISSN'] : 
				if issn in issnList : add = False
			
			if add : 
				for issn in item['ISSN'] : issnList.append(issn)
				itemNbMatch.append(i)

		i+=1

	if not itemNbMatch : return None
	else : return itemNbMatch


def addIssnToList(issn_type):
	for i in issn_type : 
		if i['type'] == 'print' : 
			suspiciousIssns['print'].append(i['value'])
		elif i['type'] == 'electronic' : 
			suspiciousIssns['electronic'].append(i['value'])
		
		
suspiciousIssns = {'print':[], 'electronic':[]}
jnb = halMatch = crossrefMatch = 0

with open("journalsTitles.csv", 'r', encoding='utf8') as fh:
	reader = csv.reader(fh)
	next(reader) # escape header
	
	for row in reader :
		# if jnb > 50 : break 
		inCrossref = False
		title = row[1]

		
		## __1__ search Crossref
		result = reqCrossref(title.replace("&","%26"))
		if not result : 
			jnb+=1
			continue 

		if len(result) == 1 : 
			addIssnToList(result[0]['issn-type'])
			inCrossref = True
			crossrefMatch+=1
			print(jnb,'OK', title)
			
		# if many match verify titles
		elif len(result) > 1 : 
			itemNbs = titlesComparison(title, result)

			if not itemNbs : 
				jnb+=1
				continue 

			if len(itemNbs) == 1 : 
				addIssnToList(result[0]['issn-type'])
				inCrossref = True
				crossrefMatch+=1
				print(jnb,'OK', title)

			elif len(itemNbs) > 1 : 
				print('\n##verify manually\n',len(itemNbs),title,'\n')

		if inCrossref :
			jnb+=1
			continue


		## __2__ search Hal
		result = reqHal(title.replace("&","%26"))
		if not result : 
			jnb +=1
			continue

		if len(result) == 1 : 
			try : 
				suspiciousIssns['print'].append(result[0]['issn_s'])
			except : pass
			try : 
				suspiciousIssns['electronic'].append(result[0]['eissn_s'])
			except : pass
			halMatch +=1


		if len(result) > 1 : 
			print('\n##verify manually\n',len(result),title,'\n')

			

		jnb +=1
	
	
print("crossRef nb match", crossrefMatch)
print("hal nb match", halMatch)
with open('suspiciousIssns.json', 'w', encoding='utf-8') as fh : 
	json.dump(suspiciousIssns, fh, indent=4)

	
		

# if nb > 10 : break