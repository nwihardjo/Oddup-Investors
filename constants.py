API_KEY = 'ac5e0a11-8406-4b94-a57f-b1a6661b0886'
URL = 'https://parserator.datamade.us/api/probablepeople/'

"""
Below list is due to different companies with the same first name
and also inaccuracy of probablepeople library differentiating people and investor
"""

# investor in this list only be rejected when compared, it still can be make as a corporation
REJECTED_COMPARED_COMPANY_IDENTIFIERS = ['Social', 'Stein', 'Startup', 'Star', 'Start', 'Suzhou', 
'Sb', 'S.', 'Sigma', 'Shenzhen', 'Silicon', 'Right', 'Real', 'Rising','Red', 'Pt', 'Project',
'Pejman', 'Prime', 'Peak', 'N', 'Nanjing', 'National', 'New', 'Next', 'Zhuhai', 'Yunnan', 'York', 'Wu', 'Quest', 'University', 
'William', 'Tom', 'T.']

#investor in this list, can't be made into root nor corporation
REJECTED_COMPANY_IDENTIFIERS = ['White Unicorn Ventures', 'Times Mirror Corporation','Time Warner Investments', 
'Surya Ventures Pte Ltd', 'Gegax', 'Tan' , 'Sun', 'Sunil', 'William', 'Vijay', 'Vikram', 'Shubhas',
'Sandeep', 'Praveen', 'Pradeep', 'Pawan', 'Nagendra', 'Nishant', 'Oleg']

APPROVED_COMPANY_IDENTIFIERS = ['Tencent', 'tiange.com', 'Xiaomi', 'Innopark', 'Capital', 'International', 
'Holdings', 'Pharmaceutical', 'Broadcasting', 'Fund', 'Sports', 'Music', 'Inc', 'Angel', 'Angels', 'Ventures',
'Investment', 'Accelerator', 'Venture', 'Textile', 'Holding','Corporation', 'Company', 'and', 'Media',
'Friends', 'Growth', 'Enterprises', 'Labs', 'Key', 'Group', 'Insurance', 'Property', 'Vc', 'Tank', 'Paytm']

"""
ASSUMPTIONS:
- Investors which first name has non-alphanumeric characters can't be differentiated
- Typo between 2 investors can't be differentiated
- Space is limited
- probablepeople library is bad at recognising Indian name
- Cities comparison only applies for cities with one word
"""
