# Investors

The project tries to group same corporate (investors invest in startups) which has different names or duplicates.
It takes OOP approach and uses probablepeople library, NLP-based python library which uses to distinguish whether a name is person or corporation.
In addition, the project also consists of several hard codes since there are multiple different investors sharing the same first name and mistakes due to the library. 

Some assumptions taken in this project:
- Same investors with 2 different names that accounts for typo is assumed different
- Same investors with 2 different names that the total word difference is more or greater than 3 is assumed different
- Same investors with 2 different names due to abbreviation is assumed different
- probablepeople library isn't reliable to distinguish non-English name
- Location is only assumed to have one word
