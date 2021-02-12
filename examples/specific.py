#!/usr/bin/env python

from pms7003 import PMS7003

print("""specific.py - Continously print a specific data value.

Press Ctrl+C to exit!

""")

# Configure the pms7003 for Enviro+
pms5003 = pms7003(
    device='/dev/ttyAMA0',
    baudrate=9600,
    pin_enable=22,
    pin_reset=27
)

try:
    while True:
        data = pms7003.read()
        print("PM2.5 ug/m3 (combustion particles, organic compounds, metals): {}".format(data.pm_ug_per_m3(2.5)))

except KeyboardInterrupt:
    pass
