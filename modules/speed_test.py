"""Moudles"""
import colorama
import speedtest
from colorama import Fore

speedTester = speedtest.Speedtest()


"""Get Servers Details"""
def serverDetails():
    """Gets List of Servers"""
    print(Fore.RED + "Loading Server List...")
    speedTester.get_servers()

    """Choose Best Servers"""
    print(Fore.RED + "Choosing Best Server...")
    best = speedTester.get_best_server()

    print(Fore.RED + "\nBest Server Found")
    print(Fore.LIGHTMAGENTA_EX + f"""
Host : {best['host']}
Network Sponsor : {best['sponsor']}
Location : {best['name']} , {best['country']}
Country Code : {best['cc']}
URL : {best['url']}    
Co-Ordinates : Lat : {best['lat']} , Lon : {best['lon']}
Latency : {best['latency']}
""")

"""Get Download and Upload Speed"""
def downloadAndUploadTest():
    print(Fore.RED + "Performing Download Speed Test...")
    downloadSpeed = speedTester.download()
    print(Fore.RED + "Performing Upload Speed Test...")
    uplaodSpeed = speedTester.upload()
    ping = speedTester.results.ping

    print(Fore.GREEN + f"Download Speed : {round(downloadSpeed/1024/1024 , 2)} Mbit/s")
    print(Fore.GREEN + f"Upload Speed : {round(uplaodSpeed/1024/1024 , 2)} Mbit/s")
    print(Fore.GREEN + f"Ping : {ping} ms")
    print(Fore.RESET)

"""Main Function"""
def speedTestResult():
    serverDetails()
    downloadAndUploadTest()

if __name__ == '__main__':
    speedTestResult()