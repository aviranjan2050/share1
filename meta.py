import re

pattern = r"gr.y" # at the place of dot any chracter can come in

if re.match(pattern, "gray"):
    print("match found")
else:
    print("match not found")

if re.search(pattern,"grey"):
    print("match found")
else:
    print("match not found")

