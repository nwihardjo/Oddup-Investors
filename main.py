import csv
import xlrd
import requests
import json

COMPANY_IDENTIFIERS = []
API_KEY = 'ac5e0a11-8406-4b94-a57f-b1a6661b0886'
URL = 'https://parserator.datamade.us/api/probablepeople/'

def nameAnalysis(name):
	# analyse the name passed using probablepeople API
	# because probablepeople library can't be easily installed in our machine
	# return True if it is a company, return False otherwise
	params = {'api_key': API_KEY, 'name': name, 'fmt' = 'json'}

	response = requests.get(URL, params = params)
	if response.status_code != 200:
		print('API call failed. Check API call in nameAnalysis function')
	
	return (response.text.json()['type'] == 'Corporation')

class investor:
	def __init__(self, id, name, inputType):
		self.id = id
		self.name = name.title()
		self.inputType = inputType
		self.type = nameAnalysis(name)

	def compare(comparedInvestorName):
		# compare the investor's name with the existing ones
		# return True if compared investors are the same

		for subname in comparedInvestorName.split():
			if subname in self.name:
				return False






def main():
	filename = input('Filename input: ')
	
	with open(filename, 'r') as f:
		writer = csv.DictReader(f)
		investors = []
		
		for row in reader:
			for singleInvestor in investors:
				if type(singleInvestor) is not list:
					if singleInvestor.compare(row['name'].lower()):
						investors[index(singleInvestor)] = [singleInvestor, investor(row['id'], row['name'], row['input'])]
					else:
						investors.append(investor(row['id'], row['name'], row['input']))
				else if type(singleInvestor) is list:
					if singleInvestor[0].compare(row['name'].lower()):
						investors[index(singleInvestor)].append(investor(row['id'], row['name'], row['input']))
					else:
						investors.append(investor(row['id'], row['name'], row['input']))

	resultFilename = 'cleanedInvestor.csv'





if __name__ == '__main__':
	main()