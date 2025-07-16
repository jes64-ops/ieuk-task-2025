# Need to read the file
# extract ip addresss
#save the output in csv file 
import re

with open('sample-log.log') as fh:
  logfile = fh.readlines()
pattern = re.compile(r'''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

# extracting the IP addresses
valid_ip = []
possible_bot_ip = []

# Extracting IP addresses
for log in logfile:
    log = log.rstrip()
    match = pattern.search(log)
    ip = match.group()
    if match:
       
        valid_ip.append(ip)
    else:
        possible_bot_ip.append(log)
print("Valid IPs:")
print(valid_ip)
print("BOT IP:")
print(possible_bot_ip)