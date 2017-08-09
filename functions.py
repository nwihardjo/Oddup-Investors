from constants import *
from countryinfo import *
import requests
import json

def nameRejectComparator(name):
	"""special name case which for different investors having the same first name"""
	# return True if it is rejected
	if name.split()[0] in REJECTED_COMPARED_COMPANY_IDENTIFIERS:
		return True
	else:
		return False

def countriesCheck(name):
	"""check investors name whether it contains regions name"""
	# return True if it contains regions name
	for country in LIST_OF_COUNTRIES:
		if name == country['continent'] or name == country['name']:
			print('DEBUG: COUNTRIES CHECK FUNC RETURNING TRU FOR', name)
			return True

def nameAnalysis(name):
	"""analyse the name passed using probablepeople API and hardcode"""
	# because probablepeople library1 can't be easily installed in our machine
	# return True if it is a company, return False otherwise

	# for investor name which has non-alphanumeric case
	# exclude the characters in brackets because it will automatically recognised as Corporation
	if not name.replace(" ","").isalnum() and len(name.split('(')[:-1]) > 0:
		name = ' '.join(name.split('(')[:-1])
	
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

def hardCodeNameComparator(investorName, comparedInvestorName):
	"""hard coded comparison between two investors"""
	# return True if the compared investors are not the same
	if not investorName.replace(" ","").isalnum() and len(investorName.split('(')[:-1]) > 0:
		investorName = ' '.join(investorName.split('(')[:-1])

	if (countriesCheck(investorName.split()[0]) and countriesCheck(comparedInvestorName.split()[0])) or (investorName.split()[0] == 'University' and comparedInvestorName.split()[0] == 'University'):
		print('DEBUG: COUNTRIES AND UNIVERSITIES NAME CHECK')
		if ' '.join(comparedInvestorName.split()[1:]) in ' '.join(investorName.split()[1:]):
			print('DEBUG: COUNTRIES AND UNIVERSITIES INVESTOR NAME ARE SAME WITH: ', investorName)
			return False
		else: 
			print('DEBUG; COUNTRIES AND UNIVERSITIES INVESTOR NAME ARENT THE SAME WITH: ', investorName)
			return True

	if nameRejectComparator(comparedInvestorName) or investorName in REJECTED_COMPANY_IDENTIFIERS or abs(len(investorName.split()) - len(comparedInvestorName.split())) >= 3:
		# print('DEBUG: INVESTORNAME IS IN REJECTED_COMPANY_IDENTIFIERS: ', investorName)
		return True