import csv
from functions import *

class Investor:
	def __init__(self, _id, name, inputType, rootName = None):
		self.id = _id	
		self.inputType = inputType
		self.rootName = rootName

		#remove 'the' in the naming
		if name.split()[0].lower() == 'the':
			self.name = (' '.join(name.split()[1:]))
		else:
			self.name = name.lstrip().rstrip()

		#type value is True if the investor is a company
		if rootName is not None: 
			self.type = True
		else: 
			self.type = nameAnalysis(self.name.title())
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
		investorName = self.name.title()
		
		# compare if the difference in the name solely on the chinese names
		# print('DEBUG:', comparedInvestorName, 'and', self.name)
		# print('DEBUG: the equivalence of', nonAlphanumRemover(self.name), 'and', nonAlphanumRemover(comparedInvestorName), 'returns', nonAlphanumRemover(comparedInvestorName) == nonAlphanumRemover(self.name))
		if nonAlphanumRemover(comparedInvestorName).lstrip().rstrip() == nonAlphanumRemover(investorName).lstrip().rstrip():
			# print('DEBUG: NAMES ARE THE SAME BUT DIFF ONLY CHINESE CHARS')
			return True

		if not self.type and investorName == comparedInvestorName:
			# allow the person type solely to have roots if the name are exactly the same
			return True
		elif not self.type or hardCodeNameComparator(investorName, comparedInvestorName):
			return False

		for subName in investorName.split():
			# splitting existing investor name prevent chinese name overlap (Zhengjiang and Zheng)
			# with the ASSUMPTION:existing investor in the list has longer name (reversely sorted)
			if comparedInvestorName.split()[0] == subName:
				return True


def main():
	investors = []

	with open("output.csv", mode = 'r', encoding = 'utf-8') as f:
		reader = csv.DictReader(f)
		
		# for _ in range(0, 4500):
		# 	reader.__next__()
		for row in reader:
			temp = 0
			if temp > 1000:
				break
			else:
				temp += 1

			if not investors:
				# first investor in the list
				investors.append(Investor(row['id'], row['name'], row['type']))
			else:
				isCompared = False
				temp = 0
				for singleInvestor in reversed(investors):
					if temp > 50: break
					else: temp += 1
					if singleInvestor.compare(row['name'].title()):
						investors.append(Investor(row['id'], row['name'], row['type'], singleInvestor.get_root()))
						isCompared = True
						break
				if not isCompared:
					investors.append(Investor(row['id'], row['name'], row['type']))

	with open('cleanedInvestor.csv','w', newline = '', encoding = 'utf-8' ) as f:
		writer = csv.writer(f)
		writer.writerow(['id', 'name', 'type', 'root'])

		for investor in investors:
			writer.writerow(investor.get_info())

if __name__ == '__main__':
	main()