import feedparser as fp
import time

d = fp.parse('https://www.hempfieldsd.org/site/RSS.aspx?DomainID=4&ModuleInstanceID=1&PageID=2')
date = '4/8/2019'
foundDate = False
'''print(d['entries'][0]['published_parsed'])'''
for x in range(len(d['entries'])):
    title = d['entries'][x]['title']
    if date == title[0:(len(date))]:
        print(title[len(date)+1:])
        foundDate = True
    elif foundDate == True:
        break
