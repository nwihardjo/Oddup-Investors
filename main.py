import csv
import requests
import json
import re

REJECTED_SPECIAL_IDENTIFIERS = ['Zhuhai', 'Yunnan', 'York', 'Wu','William']
APPROVED_SPECIAL_IDENTIFIERS = ['Xiaomi']
API_KEY = 'ac5e0a11-8406-4b94-a57f-b1a6661b0886'
URL = 'https://parserator.datamade.us/api/probablepeople/'

def nameAnalysis(name):
	"""analyse the name passed using probablepeople API and hardcode"""
	# because probablepeople library can't be easily installed in our machine
	# return True if it is a company, return False otherwise


	# for investor name which has non-alphanumeric case
	# exclude the characters in brackets because it will automatically recognised as Corporation
	name = ' '.join(name.split('(')[0])

	params = {'api_key': API_KEY, 'name': name, 'fmt': 'json'}
	response = requests.get(URL, params = params)

	if response.status_code != 200:
		print('DEBUG: API call failed for {}. Check API call in nameAnalysis function'.format(name))

	if name in APPROVED_SPECIAL_IDENTIFIERS:
		return True

	try:
		return (response.json()['type'] == 'Corporation')
	except:
		return False

class Investor:
	
	def debugInvestor(self):
		if self.type == True: x = 'Corporation'
		else: x = 'Person' 
		
		if self.rootName:
			print("DEBUG: CREATING & ADDING {} NAMED {}, ROOT: {}".format(x, self.name, self.rootName))
		else:
			print("DEBUG: CREATING & ADDING {} NAMED {}".format(x, self.name))
	
	def get_name(self): return self.name
	def get_info(self): return [self.id, self.name, self.inputType, self.rootName]

	def __init__(self, _id, name, inputType, rootName = None):
		self.id = _id
		self.name = name.title()
		self.inputType = inputType
		self.rootName = rootName

		#type value is True if the investor is a company
		self.type = nameAnalysis(name)
		self.debugInvestor()

	def compare(self, comparedInvestorName):
		"""compare the investor's name with the existing ones"""
		# return True if compared investors are the same

		if not self.type or comparedInvestorName.split()[0] in REJECTED_SPECIAL_IDENTIFIERS or abs(len(self.name.split()) - len(comparedInvestorName.split())) >= 3 :
			return False

		for subName in self.name.split():
			# splitting existing investor name prevent chinese name overlap (Zhengjiang and Zheng)
			if comparedInvestorName.split()[0] == subName:
				return True


def main():
	investors = []
	
	with open("output.csv", mode = 'r', encoding = 'utf8') as f:
		reader = csv.DictReader(f)
		
		for num in range(0, 37):
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