import csv
from functions import *

class Investor:
	def __init__(self, _id, name, inputType, rootName = None):
		self.id = _id	
		self.inputType = inputType
		self.rootName = rootName

		#remove 'the' in the naming
		if name.split()[0].lower() == 'the':
			self.name = (' '.join(name.split()[1:])).title()
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
	def get_root(self):
		if self.rootName is not None: return self.rootName
		else: return self.name

	def compare(self, comparedInvestorName):
		"""compare the investor's name with the existing ones"""
		# return True if compared investors are the same
		if comparedInvestorName.split()[0].lower() == 'the':
			comparedInvestorName = ' '.join(comparedInvestorName.split()[1:])
		
		if not self.type and self.name == comparedInvestorName:
			# allow the person type solely to have roots if the name are exactly the same
			return True
		elif not self.type or hardCodeNameComparator(self.get_name(), comparedInvestorName):
			return False

		for subName in self.name.split():
			# splitting existing investor name prevent chinese name overlap (Zhengjiang and Zheng)
			# with the ASSUMPTION:existing investor in the list has longer name (reversely sorted)
			if comparedInvestorName.split()[0] == subName:
				return True


def main():
	investors = []

	with open("output.csv", mode = 'r', encoding = 'utf8') as f:
		reader = csv.DictReader(f)
		
		for num in range(0, 1750):
			reader.__next__()

		for row in reader:
			if not investors:
				# first investor in the list
				investors.append(Investor(row['id'], row['name'], row['type']))
			else:
				isCompared = False
				for singleInvestor in reversed(investors):
					if singleInvestor.compare(row['name'].title()):
						investors.append(Investor(row['id'], row['name'], row['type'], singleInvestor.get_root()))
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