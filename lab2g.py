#!/usr/bin/env python3

# Author: Azhar Shaikh
# Author ID: aashaikh9
# Date Created: 2026/06/19

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
