import bs4
import urllib3
import re

pm = urllib3.PoolManager()

def compute_distance(lat1, lon1, lat2, lon2):
    html = pm.urlopen(url='http://boulter.com/gps/distance/?from='+lat1+'%2C+'+lon1+'&to='+lat2+'%2C+'+lon2+'&units=m', method='GET').data
    soup = bs4.BeautifulSoup(html ,'lxml')
    tag = soup.find_all('td')[-3]
    match = re.search('[\d.]+', str(tag))
    return match.group()

