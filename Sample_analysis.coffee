import re

with open('sample-log.log') as fh:
  logfile = fh.readlines()

log_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\d+)'

match = re.match(log_pattern, logfile)
if match:
    ip_address = match.group(1)
    country_code = match.group(4)
    timestamp = match.group(5)
    requested_url = match.group(6)
    response_size = match.group(8)
    bytes_transferred = match.group(9)