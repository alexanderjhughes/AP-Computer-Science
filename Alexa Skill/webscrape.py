import feedparser as fp
import time

d = fp.parse('https://www.hempfieldsd.org/site/RSS.aspx?DomainID=4&ModuleInstanceID=1&PageID=2')
date1 = '2019-04-30'
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
date = date1[-2:] + ' ' + months[int(date1[6:7])-1] + ' ' + date1[0:4]
print(d['entries'][1])
entries = d['entries']
foundDate = False
for x in range(len(entries)):
    entry = entries[x]
    if date in entry['published']:
        print(entry['title'])
        foundDate = True
    elif foundDate == True:
        break
if foundDate == False:
    print(date + " has no events scheduled.")
