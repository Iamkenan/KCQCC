import urllib2
import urlparse
from bs4 import BeautifulSoup
import csv
import xml.dom.minidom
import urllib
import xml.etree.ElementTree as ET
import selenium


CIKpage = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany'
openCIK = urllib.urlopen(CIKpage).read()
soup = BeautifulSoup(openCIK)

document = soup.find_all('tr')
print document

inputFile = None
outputFile = None
#url = 'https://www.sec.gov/Archives/edgar/data/1541625/000154162517000006/fourthquarter2016.inftab.xml'
#url = 'https://www.sec.gov/Archives/edgar/data/1166559/000110465916156931/a16-21508_1informationtable.xml'
#url = 'https://www.sec.gov/Archives/edgar/data/1552999/000139834416019562/fp0021999_13fhr-table.xml'
#url = 'https://www.sec.gov/Archives/edgar/data/1416856/000141685617000002/fim-4q16final.xml'
#url = 'https://www.sec.gov/Archives/edgar/data/1541625/000154162515000009/secondqtr2015.inftab.xml'
url ='https://www.sec.gov/Archives/edgar/data/1598381/000139834416019446/fp0021945_13fhr-table.xml'
ns = {'sec':'http://www.sec.gov/edgar/document/thirteenf/informationtable'}
rootName = 'informationTable'

test = urllib.URLopener()
test.retrieve(url, "testfile.xml")
f = open('testfile.xml')

tree = ET.iterparse('testfile.xml')
for gone, hell in tree:
    if '}' in hell.tag:
        hell.tag = hell.tag.split('}',1)[1]
informationTable = tree.root
print informationTable.tag+'\n\n'

count = 0
headers = []
with open('testfiletab7777.csv', 'wb') as csvfile:

        for holdings in informationTable:
                for holdingInfo in holdings:
                    #print "{}. {}".format(count, holding.tag)
                    if (count == 0):
                        print holdingInfo.text
                        if not str(holdingInfo.text).strip() or holdingInfo.text == None:
                            for category in holdingInfo:
                                #print holding.tail
                                #print ("{}: {}".format(holding.tag,category.tag))
                                headers.append("{}: {}".format(holdingInfo.tag,category.tag))
                        else:
                                headers.append("{}".format(holdingInfo.tag))
                    writer = csv.writer(csvfile, delimiter='\t')
                    writer.writerow(headers)

                count+=1




                        #with open('testfiletab.csv', 'wb') as csvfile:
                        #    writer = csv.writer(csvfile, delimiter='\t')
                        #    writer.writerow(headers)


                        #csv.writer('testfile45.xml', delimiter='  ').writerow(headers)
                    #elif holding.text == None:
                        #for category in holding:
                            #print "{}. {}: {}: {}".format(count,holding.tag,category.tag,category.text)
                    #else:
                            #print "{}. {}: {}".format(count,holding.tag,holding.text)
                        #count+=1
print headers

"""
with open('holdings.tsv') as tsv:
    writer = csv.writer(ts, delimiter=' ')

test = urllib.URLopener()
test.retrieve(url,'thisiswhatyouget.xml')

f = open('thisiswhatyouget.xml')

tree = ET.parse('thisiswhatyouget.xml').findall('.//')
#root = tree.getroot()
#file = csv.writer('bam_bam')


#print tree

headers = []
holdings = []
#out = csv.open("output.csv", wb)

for infoTab in tree:
    holding =[]
    header =  infoTab.tag[62:]
    if header not in headers:
        headers.append(header)

print headers

with open('output.csv', 'wb') as csvfile:
    out = csv.writer(csvfile)
    out.writerow(headers)
"""













"""
#get search terms in CIK
def getSearchTerm(arg):
    pass

#parse file into tab delimited file
def parsefile(file):
    pass

#get file from website
def getfile(arg):
    pass

#open website and navigate between pages
def openWebsite(arg):
    #open the website using the url
    url = http://www.sec.gov/edgar/searchedgar/companysearch.html
    code = request.get(url)
    pass

def fname(arg):
    pass
"""
