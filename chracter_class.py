import re

pattern = "[A-Z][A-Z][0-9]"

if re.search(pattern,"AA2"):
    print("found")

else:
    print("go to hell")


License_Plate = "MH[0-9]"

if re.search(License_Plate , "MH1234"):
    print("found")

else:
    print("not found")