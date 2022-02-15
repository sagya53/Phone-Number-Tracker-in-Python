import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

n = input("Enter your phone number: ")
number = "+91"+n
ch_number = phonenumbers.parse(number, "CH")
service_provider = phonenumbers.parse(number, "RO")

print(geocoder.description_for_number(ch_number, "en"))
print(carrier.name_for_number(service_provider, "en"))

