import re

text = "The quick brown fox jumped over the lazy dog"

pattern = r"brown"

replacement = "red"

new__text = re.sub(pattern, replacement, text)
print("Modified text:" , new__text)