#write python script to check if http server is installed on  your linux system if not install it.

import subprocess

def check_http_isinstalled():
    try:
        output = subprocess.check_output(["apache2", "-v"])
        print("Apache HTTP server is already installed.")
    except subprocess.CalledProcessError:
        print("Apache HTTP server is not installed.")
        install_http()

def install_http():
        subprocess.check_call(["sudo", "apt-get", "update"])
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "apache2"])
        print("Apache HTTP server installed successfully.")


check_http_isinstalled()
