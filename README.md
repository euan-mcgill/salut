# README
    Task is to collect health, including COVID-19-specific, data 

## Scraping Wikipedia
    Originally basing web scrape from https://simple.wikipedia.org/wiki/Coronavirus_disease_2019 - but yields a lot of duplicate and mismatched pages between EN and Simplified
    Instead, health category gives a broad basing - either to collect parallel data, or to simply gather a lot of English language resources to later be run through a simplifier model.
        e.g https://simple.wikipedia.org/wiki/Category:Medicine_stubs

### Scripts
    `multiscrape.py` Base URL is a simple English Wikipedia article. Gathers all URLs within the article body, then adds article URL suffixes to both. Follow with `> outputfile.txt` to write the console-printed output to a file.
    `messyscrape.py` As above, but automatically writes to file.
    `wikisc.py` (WIP) Arranged into functions, should handle input of a base article or categories with flags to that effect.