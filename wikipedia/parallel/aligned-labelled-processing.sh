#!/usr/bin/env bash
# -*- coding: UTF-8 -*-

#  Replace all newline chars w/ a space
tr '\n' ' '  < aligned-labelled-english*.txt > temp-en.txt
tr '\n' ' '  < aligned-labelled-simple*.txt > temp-simp.txt

# Create new line breaks on 'https'
python3 http-splitter.py temp-en.txt aligned-labelled-english.txt
python3 http-splitter.py temp-simp.txt aligned-labelled-simp.txt

# Gather links only
