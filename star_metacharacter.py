import re

pattern = r"eggs(bacon)*"  # * defines that zero , one or multiple repetition of expression before  is allowed

if re.match(pattern , "eggseggseggsbacon"):
    print("found")

else:
    print("u r not so lucky")