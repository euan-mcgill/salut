#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re
import sys

with open(sys.argv[1], 'r') as read, open(sys.argv[2], 'w') as write:
    for line in read:
        write.write((re.sub('https', '\nhttps', line)))
