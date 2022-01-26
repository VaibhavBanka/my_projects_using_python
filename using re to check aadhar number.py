import re
adhar=input("Enter your adhar number:")
if re.match('^[1-9][0-9]{11}',adhar):
    print("Valid")
else:
    print("Invalid")
