import re
import ipaddress
from collections import Counter
status_code_counter = Counter()

with open('sample-log.log') as fh:
    logfile = fh.readlines()

log_pattern = re.compile(
    r'(\d{1,3}(?:\.\d{1,3}){3})\s+-\s+(\w{2})\s+-\s+'
    r'\[([^\]]+)\]\s+'                                # IP, country, timestamp
    r'"(\w+)\s+([^\s]+)\s+(HTTP/\d\.\d)"\s+'         # Method, URL, HTTP version
    r'(\d{3})\s+(\d+)\s+"([^"]*)"\s+"([^"]*)"\s+(\d+)'  # Status, size, referer, UA, last number
)

valid_ip = []
possible_bot_ip = []
post_requests =[]


for line in logfile:
    match = log_pattern.match(line)
    if match:
        ip_address = match.group(1)
        country_code = match.group(2)
        timestamp = match.group(3)
        method = match.group(4)
        requested_url = match.group(5)
        http_version = match.group(6)
        status_code = match.group(7)
        response_size = match.group(8)
        referer = match.group(9)
        software_used = match.group(10)
        response_time = match.group(11)
        
        #checking for the status codes which increaments by 1 
        status_code_counter[status_code] += 1

        # Check IP format with ipaddress module
        try:
            ipaddress.IPv4Address(ip_address)
            valid_ip.append(ip_address)
        except ValueError:
            possible_bot_ip.append(ip_address)
        if method == "POST":
            if status_code == "429":
                post_requests.append({
                    'ip': match.group(1),
                    'timestamp': match.group(3),
                    'url': match.group(5),
                    'software': match.group(10)
                

            })
print("Valid IPs:")
print(valid_ip)
print("Possible Bot IPs :")
print(possible_bot_ip)

for entry in post_requests:
    print(f"IP: {entry['ip']}, Time: {entry['timestamp']}, URL: {entry['url']}, SOftware Used: {entry['software']}")

print("Status Code Frequencies:")
for code, count in status_code_counter.items():
    print(f"{code}: {count} times")