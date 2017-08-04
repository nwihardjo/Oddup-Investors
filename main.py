import csv
import requests
import json

COMPANY_IDENTIFIERS = []
API_KEY = 'ac5e0a11-8406-4b94-a57f-b1a6661b0886'
URL = 'https://parserator.datamade.us/api/probablepeople/'

def nameAnalysis(name):
	# analyse the name passed using probablepeople API
	# because probablepeople library can't be easily installed in our machine
	# return True if it is a company, return False otherwise
	
	params = {'api_key': API_KEY, 'name': name, 'fmt': 'json'}

	response = requests.get(URL, params = params)
	if response.status_code != 200:
		print('API call failed. Check API call in nameAnalysis function')
	
	return (response.text.json()['type'] == 'Corporation')


class investor():
	def __init__(self, id, name, inputType, rootName = None):
		self.id = id
		self.name = name.title()
		self.inputType = inputType
		self.rootName = rootName

		#value is True if the investor is a company
		self.type = nameAnalysis(name)

		
	def get_name(self): return self.name
	def get_info(self): return [self.id, self.name, self.inputType, self.rootName]

	def compare(comparedInvestorName):
		# compare the investor's name with the existing ones
		# return True if compared investors are the same

		if not self.inputType:
			return False

		if comparedInvestorName.split()[0] in self.name:
			return True






def main():
	filename = input('Filename input: ')
	investors = []
	
	with open(filename, 'r') as f:
		reader = csv.DictReader(f)
		
		for row in reader:
			for singleInvestor in investors:
				if singleInvestor.compare(row['name'].title()):
					investors[index(singleInvestor)] = [singleInvestor, investor(row['id'], row['name'], row['input'], singleInvestor.get_name())]
				else:
					if nameAnalysis(row['name']):
						investors.append(investor(row['id'], row['name'], row['input']))

	with open('cleanedInvestor.csv','w', newline = '' ) as f:
		fieldnames = ['id','name','type','root']
		writer = csv.writer(f, filednames = fieldnames)
		writer.writeheader()

		for investor in investors:
			writer.writerow(investor.get_info())




if __name__ == '__main__':
	main()