#!env python3

import os
import time
import ntplib
import socket

client = ntplib.NTPClient()
try:
    response = client.request('pool.ntp.org', version=3)
    tx_time = response.tx_time
    testTime = time.strftime('%m/%d/%Y %H:%M', time.localtime(tx_time))
except (ntplib.NTPException, socket.gaierror, OSError) as e:
    print(f"Warning: Could not get NTP time: {e}")
    testTime = time.strftime('%m/%d/%Y %H:%M', time.localtime())

question = os.getenv("CI", "Undefined")

print(f"Hello, world! The time is {testTime}")
print(f"Hello, Slurm! It's running inside CI - {question}")
