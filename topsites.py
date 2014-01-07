#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import sys
import math

"""
http://en.wikipedia.org/wiki/ISO_3166-1
"""

BASE_URL='http://www.alexa.com/topsites/countries;%d/%s'

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: country-code(ISP 3166-1)] top-n\n')
        sys.exit(1)
    
    country_code = sys.argv[1].upper()
    number = int(sys.argv[2])

    page_numbers = int(math.ceil(number/25.0))

    for page_num in range(0, page_numbers): 
        response = requests.get(BASE_URL % (page_num, country_code))  
    
        soup = BeautifulSoup(response.text)
        bullets = soup.find_all('li', {'class':'site-listing'})
    
        for bullet in bullets:
            rank = bullet.div.contents[0]
            site = bullet.h2.a.contents[0]
            print('%s %s' % (rank, site))
