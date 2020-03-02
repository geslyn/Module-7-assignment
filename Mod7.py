import datetime
from datetime import datetime, timedelta
data = datetime.now()
print(data)

#Subtract 60 seconds
print(data - timedelta(seconds=60))

#Add 2 years
print(data + timedelta(days=730))
