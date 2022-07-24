import phonenumbers
from phonenumbers import timezone,geocoder,carrier,parse
number=input("Enter a your phone number with+__ : ")
phone=parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)  #print continent name or calautta
print(car)    #print sim company name
print(reg)   #print registered country name
