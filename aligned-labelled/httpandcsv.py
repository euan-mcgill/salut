#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re
import sys

def httpsplit():
    with open(sys.argv[1], 'r') as read, open(sys.argv[2], 'w') as write:
        for line in read:
            write.write((re.sub('https', '\nhttps', line)))

def csvmaker():
    with open('aligned-simp.txt', 'r') as simp, open('aligned-english.txt', 'r') as en, open('parallel-en-simp-corpus.tsv','w') as tsv:
        for simpline, enline in zip(simp,en):
            # tsv.write(simpline+'\t'+enline)
            print(simpline+'\t'+enline)

def gatherlinks():



