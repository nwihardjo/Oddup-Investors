import csv
import requests
import json
from countryinfo import *
from constants import *

def nameRejector(name):
	"""special name case which for different investors having the same first name"""
	# return Ture if it is rejected
	if name.split()[0] in REJECTED_SPECIAL_IDENTIFIERS:
		return True
	else:
		return False

def nameAnalysis(name):
	"""analyse the name passed using probablepeople API and hardcode"""
	# because probablepeople library can't be easily installed in our machine
	# return True if it is a company, return False otherwise
	for subName in name.split():
		if subName in APPROVED_COMPANY_IDENTIFIERS or '.' in subName:
			return True
		if nameRejector(subName):
			return False
			
	# for investor name which has non-alphanumeric case
	# exclude the characters in brackets because it will automatically recognised as Corporation
	if not name.replace(" ","").isalnum():
		name = ' '.join(name.split('(')[:-1])

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
	"""hard codes of the comparison between two investors"""
	# return True if the compared investors are not the same

	if nameRejector(comparedInvestorName) or investorName in REJECTED_COMPANY_IDENTIFIERS or abs(len(investorName.split()) - len(comparedInvestorName.split())) >= 3:
		return True

class Investor:
	def __init__(self, _id, name, inputType, rootName = None):
		self.id = _id	
		self.inputType = inputType
		self.rootName = rootName

		#remove 'the' in the naming
		if name.split()[0].lower() == 'the':
			self.name = ' '.join(name.split()[1:])
		else:
			self.name = name.title()

		#type value is True if the investor is a company
		if rootName is not None: 
			self.type = True
		else: 
			self.type = nameAnalysis(self.name)
		
		self.print_status()
	
	def print_status(self):
		if self.type == True: x = 'Corporation'
		else: x = 'Person' 
		
		print("CREATING {}; NAME: {}; ROOT: {}".format(x, self.name, self.rootName))

	def get_name(self): return self.name
	def get_info(self): return [self.id, self.name, self.inputType, self.rootName]


	def compare(self, comparedInvestorName):


		"""compare the investor's name with the existing ones"""
		# return True if compared investors are the same
		if comparedInvestorName.split()[0].lower() == 'the':
			comparedInvestorName = ' '.join(comparedInvestorName.split()[1:])

		if not self.type or hardCodeNameComparator(self.get_name(), comparedInvestorName):
			return False

		for subName in self.name.split():
			# splitting existing investor name prevent chinese name overlap (Zhengjiang and Zheng)
			if comparedInvestorName.split()[0] == subName:
				return True


def main():
	investors = []
	
	with open("output.csv", mode = 'r', encoding = 'utf8') as f:
		reader = csv.DictReader(f)
		
		for num in range(0, 210):
			reader.__next__()

		for row in reader:
			if not investors:
				# first investor in the list
				investors.append(Investor(row['id'], row['name'], row['type']))
			else:
				isCompared = False
				for singleInvestor in reversed(investors):
					if singleInvestor.compare(row['name'].title()):
						investors.append(Investor(row['id'], row['name'], row['type'], singleInvestor.get_name()))
						isCompared = True
						break
				if not isCompared:
					investors.append(Investor(row['id'], row['name'], row['type']))

	with open('cleanedInvestor.csv','w', newline = '' ) as f:
		fieldnames = ['id','name','type','root']
		writer = csv.writer(f, filednames = fieldnames)
		writer.writeheader()

		for investor in investors:
			writer.writerow(investor.get_info())



if __name__ == '__main__':
	main()