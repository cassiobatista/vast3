#!/usr/bin/env python3
#
# VAST Challenge 2019: Disaster at St. Himark!
# https://vast-challenge.github.io/2019/index.html
#
# Federal University of Pará (UFPA)
#
# author: june 2019
# cassio batista - cassio.batista.13@gmail.com
# edwin jueda - 
# erick campos - 

from termcolor import cprint

TAG = 'cfg'

DO_LEMMATIZE = True
if not DO_LEMMATIZE:
    cprint('%s: lemmatize step will be skipped to speed up processing' % TAG, 
            'red', attrs=['bold'])

NUM_WORDS = 10
MIN_WLEN  = 3

SVGFILE = '../MC3/maps/custom/neigh_labels.svg'
SVGTEST = '../MC3/maps/mapa_vast_vetorizado.svg'
SVG_NODE_HIERARCHY = ['svg', 'g', 'path', 'text', 'tspan']

DATA_CSVFILE = '../MC3/data/YInt.csv'
REPLACE_FILE = '../src/replace.txt'
USELESS_FILE = '../src/w_useless.txt'
USEFUL_FILE  = '../src/w_useful.txt'
