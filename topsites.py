#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil

BASE_URL='http://www.alexa.com/topsites/countries;%d/%s'

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: COUNTRY-CODE TOP-N\n')
        sys.exit(1)
    
    country_code = sys.argv[1].upper()
    number = int(sys.argv[2])
    delimiter = ' '

    page_numbers = int(ceil(number/25.0))

    for page_num in range(0, page_numbers): 
        response = requests.get(BASE_URL % (page_num, country_code))  
    
        soup = BeautifulSoup(response.text)
        bullets = soup.find_all('li', {'class':'site-listing'})
    
        for bullet in bullets:
            items = bullet.find_all('div')
            rank = items[0].get_text().strip()
            site = items[1].p.get_text().strip()
            print('%s%s%s' % (rank, delimiter, site))
