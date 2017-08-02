import csv
import xlrd

COMPANY_IDENTIFIERS = []

class investor:
	def __init__(self, id, name, inputType):
		self.id = id
		self.name = name.lower()
		self.inputType = inputType

	def compare(comparedInvestorName):
		# compare the investor's name with the existing ones
		# return False if compared investors are the same


def main():
	filename = input('Filename input: ')
	
	with open(filename, 'r') as f:
		writer = csv.DictReader(f)
		investors = []
		
		for row in reader:
			for singleInvestor in investors:
				if type(singleInvestor) is not list:
					if not singleInvestor.compare(row['name'].lower()):
						investors[index(singleInvestor)] = [singleInvestor, investor(row['id'], row['name'], row['input'])]
					else:
						investors.append(investor(row['id'], row['name'], row['input']))
				else if type(singleInvestor) is list:
					if not singleInvestor[0].compare(row['name'].lower()):
						investors[index(singleInvestor)].append(investor(row['id'], row['name'], row['input']))
					else:
						investors.append(investor(row['id'], row['name'], row['input']))

	resultFilename = 'cleanedInvestor.csv'





if __name__ == '__main__':
	main()
