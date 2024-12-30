#!/bin/python3


from time import time
from datetime import datetime


seconds_since_epoch = time()

formatted_string = "{:,.4f}".format(seconds_since_epoch)
scientific_notation = "{:e}".format(seconds_since_epoch)
formatted_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_string}\
      or {scientific_notation} in scientific notation\n{formatted_date}")
