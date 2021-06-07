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

## Corpus files
| Domain        | Type | Simple-words | English-words |
|---------------|------|--------------|---------------|
| Full          | AL   | 52265        | 78827         |
| Full Filtered | A    |              |               |
| Covid^        | A    |  9405        | 13079         |
| Stubs^        | A    | 19584        | 38944         |
| Medicine^     | A    | 13775        | 22834         |
| Pain^         | A    |  1151        |  2433         |
| Symptoms^     | A    |  5878        | 10446         |

## Corpus filtering
| Full Corpus     | Semantic Similarity filter per utt           |
|                 | >0       |>2.35**      | >2.5      | >3      |
|-----------------|----------|-------------|-----------|---------|
| Mean similarity | 2.85     | 3.21        | 3.25      | 3.50    |
| N sentences     | 478      | 375         | 361       | 231     |
| N words         | 132k     | 112k        | 108k      | 69k     |
| % of original   | 100%     | 85.0%       | 82.1%     | 52.3%   |

### Key to corpus types
    A = Aligned, AL= Aligned and URLs*, AS= Aligned and Scores*, L = Labelled (monolingual)
    * -480 for accurate word count
    ** 2.35 is the lowest similarity score where the English equivalent article isn't a blank article
    ^ Included in the "full" corpora

## Corpora
    `./wikipedia/parallel-[labelled-]corpus-health.tsv`: 
