# -*- coding: utf-8 -*-

# Common functions used throughout the project
# Created for https://github.com/queengooborg/Bambu-Lab-RFID-Library

import subprocess
import os
import sys
import struct
from pathlib import Path
from datetime import datetime

if not sys.version_info >= (3, 6):
  raise Exception("Python 3.6 or higher is required!")

# Byte conversions
def bytes_to_string(data):
    return data.decode('ascii').replace('\x00', ' ').strip()

def bytes_to_hex(data, chunkify = False):
    output = data.hex().upper()
    return " ".join((output[0+i:2+i] for i in range(0, len(output), 2))) if chunkify else output

def bytes_to_int(data):
    return int.from_bytes(data, 'little')

def bytes_to_float(data):
    return struct.unpack('<f', data)[0]

def bytes_to_date(data):
    string = bytes_to_string(data)
    parts = string.split("_")
    if len(parts) < 5:
        return string # Not a date we can process, if it's a date at all
    return datetime(
        year=int(parts[0]),
        month=int(parts[1]),
        day=int(parts[2]),
        hour=int(parts[3]),
        minute=int(parts[4])
    )
