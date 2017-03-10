#!/usr/bin/env python
from bs4 import BeautifulSoup

f = open('git.html','r')
file = f.read()

soup = BeautifulSoup(file, 'lxml')
comb = []

def dayify(x):
  if 'weeks' in x:
    days = int(filter(str.isdigit, str(x))) * 7
  elif 'months' in x:
    days = int(filter(str.isdigit, str(x))) * 30
  else:
    days = int(filter(str.isdigit, str(x)))
  return days

for row in soup.findAll('table')[0].tbody.findAll('tr'):
    x = row.findAll('td')[0].text.strip()
    y = row.findAll('td')[4].text.strip()
    comb.append((x,dayify(y)))
    newlist = sorted(comb, key=lambda x: x[1])

for x in range(0, len(newlist)):
    print "%s : %s days ago" % (newlist[x][0], newlist[x][1])
