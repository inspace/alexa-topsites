#Alexa Top Sites Scraper

This script does not use the official [Alexa API](http://docs.aws.amazon.com/AlexaTopSites/latest/) but is a page scraper. Anyone looking for a robust solution should use the official API since all page scrapers are fragile to page changes.

###Requirements
The [Requests](http://docs.python-requests.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) libraries are required.

###Usage
```python
python topsites.py COUNTRY-CODE TOP-N
```

- COUNTRY-CODE: should be the 2 character [ISO_3166-1 style](http://en.wikipedia.org/wiki/ISO_3166-1)
- TOP-N: the number of top sites to fetch
- Results are a space separated RANK, URL pair per line

Example
```
./topsites.py ZA 25
```

Output
```
1 google.co.za
2 google.com
3 facebook.com
4 youtube.com
5 yahoo.com
6 wikipedia.org
7 gumtree.co.za
8 bidorbuy.co.za
9 linkedin.com
10 news24.com
11 fnb.co.za
12 twitter.com
13 blogspot.com
14 amazon.com
15 standardbank.co.za
16 pinterest.com
17 ask.com
18 absa.co.za
19 live.com
20 wordpress.com
21 iol.co.za
22 imdb.com
23 olx.co.za
24 kickass.to
25 junkmail.co.za
```
