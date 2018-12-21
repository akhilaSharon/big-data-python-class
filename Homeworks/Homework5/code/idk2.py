import re
from collections import Counter
words = re.findall('\w+', open('a.txt').read())
print Counter(words)