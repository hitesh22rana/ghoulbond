"""Modules"""
import platform
from colorama import Fore
import psutil


"""Monitor CPU Times"""
def monitor_cpu_times():
    cpu_times = psutil.cpu_times()
    user_time = round(cpu_times.user/3600)
    system_time = round(cpu_times.system/3600)
    idle_time = round(cpu_times.idle/3600)
    print(Fore.RED + "Time spent on processes by the User : " + Fore.GREEN + f"{user_time} hrs")
    print(Fore.RED + "Time spent on processes by the System : " + Fore.GREEN + f"{system_time} hrs")
    print(Fore.RED + "Time spent on processes by Idle : " + Fore.GREEN + f"{idle_time} hrs")


"""Measure CPU Utils"""
def monitor_cpu_utils():
    print(Fore.RED + "CPU Percentage Utilization : " + Fore.GREEN + f"{psutil.cpu_percent()} %")


"""Count Working CPU Cores"""
def monitor_cpu_cores():
    print(Fore.RED + "CPU CORES : " + Fore.GREEN + f"{psutil.cpu_count()}")


"""Measure CPU Frequencies"""
def monitor_cpu_freq():
    print(Fore.RED + "CPU Frequency : " + Fore.GREEN + f"{psutil.cpu_freq().current} Mhz")


"""Monitor RAM Usage"""
def monitor_ram():
    virtual_memory = psutil.virtual_memory()
    print(Fore.RED + "Total Memory : " + Fore.GREEN + f"{round(virtual_memory.total/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Available Memory : " + Fore.GREEN + f"{round(virtual_memory.available/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Used Memory : " + Fore.GREEN + f"{round(virtual_memory.used/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Percentage Used : " + Fore.GREEN + f"{virtual_memory.percent} %")


"""Monitor Disk"""
def monitor_disk():
    """All Partitions"""
    disk_usage = psutil.disk_usage('/')
    print(Fore.RED + "Total Memory : " + Fore.GREEN + f"{round(disk_usage.total/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Free Memory : " + Fore.GREEN + f"{round(disk_usage.free/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Used Memory : " + Fore.GREEN + f"{round(disk_usage.used/(1024*1024*1024),2)} GB")
    print(Fore.RED + "Percentage Used : " + Fore.GREEN + f"{disk_usage.percent} %")


"""Monitor Network Requests"""
def monitor_network():
    io_stats = psutil.net_io_counters()
    print(Fore.RED + "Total Bytes Sent : " + Fore.GREEN + f"{io_stats.bytes_sent} Bytes")
    print(Fore.RED + "Total Bytes Recieved : " + Fore.GREEN + f"{io_stats.bytes_recv} Bytes")


"""Monitor Batter Usage"""
def monitor_battery():
    battery_info = psutil.sensors_battery()
    print(Fore.RED + "Battery Percent : " + Fore.GREEN + f"{battery_info.percent} %")
    print(Fore.RED + "Time Left : " + Fore.GREEN + f"{round(battery_info.secsleft/60 , 2)} minutes / {round(battery_info.secsleft/3600 , 2)} hrs")

"""All System Information Combined"""
def sys_info(): 
    try:
        my_system = platform.uname()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    try:
        print(Fore.MAGENTA + "System Architecture Information")
        """Host name"""
        if(my_system.node == ""):
            print(Fore.RED + "Host Name is not found")
        else:
            print(Fore.RED + "Host name : " + Fore.GREEN + f"{my_system.node}")
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    """System"""
    try:
        if(my_system.system == ""):
            print(Fore.RED + "System : " + Fore.GREEN + "Others")
        else:
            print(Fore.RED + "System : " + Fore.GREEN + f"{my_system.system}")
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    """Release""" 
    try:
        if(my_system.release == ""):
            print(Fore.RED + "No System Released is found!")
        else:
            print(Fore.RED + "Release (Version) : " + Fore.GREEN + f"{my_system.release}")
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    """Platform"""
    try:
        if(platform.platform() == ""):
            print(Fore.RED + "Platform could not be found!")
        else:
            print(Fore.RED + "Platform : " + Fore.GREEN + f"{platform.platform()}")
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    """Architecture"""
    try:
        if(platform.architecture() == ""):
            print(Fore.RED + "Machine's Architecture could not be found!")
        else:
            print(Fore.RED + "Machine's Architecture : " + Fore.GREEN + f"{platform.architecture().__getitem__(0)} , {platform.architecture().__getitem__(1)}" )
        print()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    try:
        print(Fore.MAGENTA + "Processor's Information")
        """Processor"""
        if(my_system.processor == ""):
            print(Fore.RED + "Unable to find Processor's Infromation!")
        else:
            print(Fore.RED + "Architecture : " + Fore.GREEN + f"{my_system.processor}")
            monitor_cpu_cores()
            monitor_cpu_freq()
            monitor_cpu_times()
            monitor_cpu_utils()
            print()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")
        
    try:
        print(Fore.MAGENTA + "Virtual Memory (RAM) Information")
        """RAM"""
        monitor_ram()
        print()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    try:
        print(Fore.MAGENTA + "Disk Storage Information")
        monitor_disk()
        print()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")
    
    try:
        print(Fore.MAGENTA + "Network Requests Information")
        monitor_network()
        print()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

    try:
        print(Fore.MAGENTA + "Battery Information")
        monitor_battery()
    except Exception as e:
        print(Fore.RED + "Error Occured : " + Fore.GREEN + f"{e}")

if __name__ == '__main__':
    sys_info()