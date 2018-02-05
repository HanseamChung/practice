import re
data = """
parik 800905-1049118
kim 700905-1049119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
