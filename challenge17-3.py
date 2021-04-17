import re

text = """The ghost that says boo haunts the loo"""
matches = re.findall(".o{2}", text, re.IGNORECASE)
print(matches)
