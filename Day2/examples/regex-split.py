import re

text = "apple,mongo,grapes,orangge"

pattern = r','

split_reaults = re.split(pattern, text)
print(split_reaults)