"""Modules"""
import phonenumbers
from phonenumbers import carrier
from phonenumbers import timezone

"""Built in function for country name"""
from phonenumbers import geocoder
from colorama import Fore

def time_zone_details(number):
    """Provides Time zone details of the registered number"""
    ch_number = phonenumbers.parse(number)

    try:
        timeZone = timezone.time_zones_for_number(ch_number)
        print(Fore.RED + "TimeZone : " , end = "")

        for individual_time_zone in timeZone:
            print(Fore.GREEN + f"{individual_time_zone}" , end = " ")

    except:
        print(Fore.RED + "Does not seems like a valid number enter valid number")
        

def service_provider_details(number):
    """Provide service provider details"""
    try:
        service_number = phonenumbers.parse(number,"RO")
        print(Fore.RED + "Service Provider : ",end="")
        if(carrier.name_for_number(service_number,"en") != ""):
            print(Fore.GREEN + f'{carrier.name_for_number(service_number,"en")}')
        else:
            print(Fore.RED + "Entered number is wrong or no details of service provider is registered")

    except:
        print(Fore.RED + "Does not seems like a valid number enter valid number")


def country_history(number):
    
    try:
    
        """In CH ( C is for country and H is for history)"""
        ch_number = phonenumbers.parse(number,"CH")

        print(Fore.RED + f"Phone Number : {Fore.GREEN + number}")
        print(Fore.RED + "Country : ",end="")

        if((geocoder.description_for_number(ch_number,"en")) != ""): 
            print(Fore.GREEN + geocoder.description_for_number(ch_number,"en"),)
        else:
            print(Fore.RED + "Entered number is wrong /country code is missing no details of country is registered")

    except:
        print(Fore.RED + "Does not seems like a valid number enter valid number")
        exit(0)

def get_details():
    print()
    number = input(Fore.BLUE + "Enter your valid number along with country code : ").replace(" ","")

    print()
    country_history(number)
    service_provider_details(number)
    time_zone_details(number)
    print('\n')


if __name__ == '__main__':
    get_details()    