# Getting the location and service provider for a phone number

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Getting the phone number aw input 
number = input("Please enter your Phone Number: ")

# Getting the name of the place for the Phone number 
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# Getting the Service provider for the Phone number
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

# Getting the Timezone for the Phone number
time_number = phonenumbers.parse(number)
print(timezone.time_zones_for_number(time_number))
