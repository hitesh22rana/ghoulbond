"""Modules"""
import geocoder
import folium
from colorama import Fore

def target_location():
    
    try:
        ip_address = input(Fore.RED + "\n[+] Enter Public IP Address of the target : ")
        geo_location = geocoder.ip(ip_address)
        if(geo_location == None):
            print(Fore.RED + "Invalid Public IP Address\n")
        
        else:
            print(Fore.RED + "\nCity : " + Fore.GREEN + geo_location.city)
            print(Fore.RED + "\nCountry : " + Fore.GREEN + geo_location.country)

            geo_address = geo_location.latlng

            target_map = folium.Map(location = geo_address , zoom_start = 16)
            folium.CircleMarker(location = geo_address , radius = 50 , color = "red").add_to(target_map)
            folium.Marker(geo_address).add_to(target_map)
            folium.Marker(geo_address , popup = "Yorkshire").add_to(target_map)

            target_map.save("target_location.html")
            print(Fore.RED + "\nMap of the target is saved as : " + Fore.GREEN + "target_location.html\n")

    except:
        print("Invalid Public IP Address")

if __name__ == '__main__':
    target_location()
