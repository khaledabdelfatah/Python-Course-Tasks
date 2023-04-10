# Write ping python program where first ask the user for input,
# and then perform the ping request to that host.

import subprocess

host = input("Enter host : ")
# host="www.google.com"
result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE)


print(result.stdout.decode('utf-8'))
