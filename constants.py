API_KEY = 'ac5e0a11-8406-4b94-a57f-b1a6661b0886'
URL = 'https://parserator.datamade.us/api/probablepeople/'

"""
Below list is due to different companies with the same first name
and also inaccuracy of probablepeople library differentiating people and investor
"""

# investor in this list only be rejected when compared, it still can be make as a corporation
REJECTED_COMPARED_COMPANY_IDENTIFIERS = ['Social', 'Stein', 'Startup', 'Star', 'Start', 'Suzhou', 
'Sb', 'S.', 'Sigma', 'Shenzhen', 'Silicon', 'Right', 'Real', 'Rising','Red', 'Pt', 'Project',
'Pejman', 'Prime', 'Peak', 'N', 'New', 'Next', 'Nirvana', 'Orient', 'One', 'Magic',
'Marc', 'Media', 'Jardine', 'Jason', 'K', 'Kaiwu', 'Kamal', 'Legend', 'Liberty', 'Lightspeed',
'Id', 'Idea', 'Impact', 'Industrial', 'Infinity', 'Innovation', 'Investor', 'Frontline', 
'Full', 'Future', 'Gabriel', 'Galaxy', 'General', 'Global', 'Golden', 'Good', 'Grand', 
'Gray', 'Great', 'Green', 'Hong', 'Hua', 'Hui'
'Zhuhai', 'Yunnan', 'York', 'Wu', 'Quest', 'University', 'William', 'Tom', 'T.']

# investor in this list, can't be made into root nor corporation
REJECTED_COMPANY_IDENTIFIERS = ['White Unicorn Ventures', 'Times Mirror Corporation','Time Warner Investments', 
'Surya Ventures Pte Ltd', 'Michael R. Sutcliff', 'John S. Hendricks', 'Joseph N. Sanberg', 'Lim Swee Yong', 
'Gegax', 'Tan', 'Sun', 'Sunil', 'William', 'Vijay', 'Vikram', 'Shubhas', 'Sandeep', 'Praveen', 'Pradeep', 'Pawan',
'Nagendra', 'Nishant', 'Oleg', 'National', 'Nitin']

# investor which name contains words in this list will be skipped in the compareSubString function
SKIPPED_COMPANY_IDENTIFIERS = ['Private']


# investor in this list has some investors which first name are the same but different investor, and some
# are the same. Can compare the 2 words
TEMP_COMPANY_IDENTIFIERS = ['Legend', 'Lightspeed', 'Infinity', 'Innovation']

# investor which name is in this list, automatically become a corporation
APPROVED_COMPANY_IDENTIFIERS = ['Tencent', 'tiange.com', 'Xiaomi', 'Innopark', 'Capital', 'International', 
'Holdings', 'Pharmaceutical', 'Broadcasting', 'Fund', 'Sports', 'Music', 'Inc', 'Angel', 'Angels', 'Ventures',
'Investment', 'Accelerator', 'Venture', 'Textile', 'Holding','Corporation', 'Company', 'and', 'Media',
'Friends', 'Growth', 'Enterprises', 'Labs', 'Key', 'Group', 'Insurance', 'Property', 'Vc', 'Tank', 'Paytm', 'Seed']

"""
ASSUMPTIONS:
- Investors which first name has non-alphanumeric characters can't be differentiated
- Typo between 2 investors can't be differentiated
- Space is limited
- probablepeople library is bad at recognising Indian name
- Cities comparison only applies for cities with one word
- Same investors which differs than 3 words is assumed to be different
"""
