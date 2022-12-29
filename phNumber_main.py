import phonenumbers
from test_phNumber import number

from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"ta")) # finding the place for the phone number

from phonenumbers import carrier


service_number=phonenumbers.parse(number,"R0")
print(carrier.name_for_number(service_number,"en"))# finding the service provider for the phone number

from phonenumbers import timezone
phnumber=phonenumbers.parse(number)
timezone=timezone.time_zones_for_number(phnumber)# finding the timezone for the phone number
print(timezone)


