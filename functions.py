from constants import *
from countryinfo import *
import requests
import json

def nonAlphanumRemover(name):
	"""remove non-alphanumeric character(s) or Chinese ones"""
	# return clean and non-alphanumeric character(s)
	if not name.replace(" ","").isalnum() and len(name.split('(')[:-1]) > 0:
		# print('DEBUG: NAME CONTAINS NONALPHANUM CHARS', name)
		name = ' '.join(name.split('(')[:-1])
	return name

def countriesCheck(name):
	"""check investors name whether it contains regions name"""
	# return True if it contains regions name
	for country in LIST_OF_COUNTRIES:
		if name == country['continent'] or name == country['name']:
			# print('DEBUG: COUNTRIES CHECK FUNC RETURNING TRU FOR', name)
			return True

def nameAnalysis(name):
	"""analyse the name passed using probablepeople API and hardcode"""
	# because probablepeople library1 can't be easily installed in our machine
	# return True if it is a company, return False otherwise

	name = nonAlphanumRemover(name)
	
	for subName in name.split():
		# print('DEBUG: SPLITTING NAME: ', name)
		if subName in REJECTED_COMPANY_IDENTIFIERS:
			return False
		elif subName in APPROVED_COMPANY_IDENTIFIERS or '.' in subName or countriesCheck(subName):
			return True

	params = {'api_key': API_KEY, 'name': name, 'fmt': 'json'}
	response = requests.get(URL, params = params)
	if response.status_code != 200:
		# can be deleted for which below line of code is integrated
		print('DEBUG: API call {} ({}) for {}. Message: {}'.format(response.json()['meta']['status'],response.status_code, name, response.json()['meta']['message']))
		print('DEBUG: return False instead. Making a "Person"')
		return False

	try:
		return (response.json()['type'] == 'Corporation')
	except:
		return False

def nameRejectComparator(name):
	"""special name case which for different investors having the same first name"""
	# return True if it is rejected
	if name.split()[0] in REJECTED_COMPARED_COMPANY_IDENTIFIERS:
		# print('DEBUG: {} IS IN THE REJECTED COMPARED COMPANY IDENTIFIERS'.format(name))
		return True
	else:
		# print('DEBUG: {} IS NOT IN THE REJECTED COMPARED COMPANY IDENTIFIERS'.format(name))
		return False

def compareSubString(name, comparedName, minMatch):
	"""analyse the two strings passed to check the similarity between the two"""
	# return True if the both strings are not the same, False otherwisse
	similarity = 0

	for subComparedName in comparedName.split():
		if countriesCheck(subComparedName) or subComparedName in SKIPPED_COMPANY_IDENTIFIERS: 
			continue
		elif subComparedName in name: 
			similarity += 1
	# print('DEBUG: COMPARESUBSTRING FUNC WITH', name, comparedName)
	# print('DEBUG: COMPARESUBSTRING FUNC SIMILARITY {} AND MINMATCH {}'.format(similarity, minMatch))
	# print('DEBUG: COMPARESUBSTRING FUNC RETURN ', similarity >= minMatch)
	return (similarity < minMatch)

def hardCodeNameComparator(investorName, comparedInvestorName):
	"""hard coded comparison between two investors"""
	# return True if the compared investors are not the same, return False otherwise
	investorName = nonAlphanumRemover(investorName)
	comparedInvestorName = nonAlphanumRemover(comparedInvestorName)

	investorTemp = False
	comparedInvestorTemp = False
	for subInvestorName in investorName.split():
		if countriesCheck(subInvestorName): 
			investorTemp = True
	for subComparedInvestorName in comparedInvestorName.split():
		if countriesCheck(subComparedInvestorName): 
			comparedInvestorTemp = True

	if (investorTemp and comparedInvestorTemp) or ('University' in comparedInvestorName and 'University' in investorName):
		# print('DEBUG: COUNTRIES AND UNIVERSITIES NAME CHECK')
		if len(comparedInvestorName.split()) == 2 or len(investorName.split()) == 2:
			# print('DEBUG: COUNTRIES AND UNIVERSITIES WITH 2 WORDS')
			return compareSubString(investorName, comparedInvestorName, 1)
		else: 
			# print('DEBUG; COUNTRIES AND UNIVERSITIES WITH > 2 WORDS: ', investorName)
			return compareSubString(investorName, comparedInvestorName, 2)
	# print('DEBUG: COUNTRIES AND UNI INVESTOR ARENT THE SAME', investorName)
	if nameRejectComparator(comparedInvestorName) or investorName in REJECTED_COMPANY_IDENTIFIERS or abs(len(investorName.split()) - len(comparedInvestorName.split())) >= 3:
		# print('DEBUG: INVESTORNAME IS IN REJECTED_COMPANY_IDENTIFIERS: ', investorName)
		return True
