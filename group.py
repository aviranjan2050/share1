import re
#() defines a group and a star after that says that it can be repeated as many times as possible
pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggsbread"):
    print("found")

else:
    print("sorry")