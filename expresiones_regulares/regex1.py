import re

text = "the quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$",text)

if x:
    print("si")
else:
    print("no")
    
    