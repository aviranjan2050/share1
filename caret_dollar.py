import re
pattern = r"^avin..sh$" #pattern that starts with g and ends with y,number of dots represent number of chracters

if re.match(pattern,"avinaash"):
    print("found")

else:
    print("not found")

if re.search(pattern,"avinaash"):
    print("found")

else:
    print("not found")
