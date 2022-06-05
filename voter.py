import datetime
from dateutil import relativedelta
sdob = input('Enter you date of birth (dd/mm/yyyy): ')
cd = datetime.datetime.now()
dob = datetime.datetime.strptime(sdob,"%d/%m/%Y")
# Get the relativedelta between two dates
age = relativedelta.relativedelta(cd, dob).years
Eligibility = "ELIGIBLE" if age> 18 else "NOT eligible"
print(f"Your age is: {age} and you are {Eligibility} for voting")