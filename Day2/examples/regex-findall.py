import re 

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())

else:
    print("no pattern found")