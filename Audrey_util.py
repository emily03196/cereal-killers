import bs4
import urllib3
import re
from math import radians, cos, sin, asin, sqrt

pm = urllib3.PoolManager()

def compute_distance(lat1, lon1, lat2, lon2):
    html = pm.urlopen(url='http://boulter.com/gps/distance/?from='+lat1+'%2C+'+lon1+'&to='+lat2+'%2C+'+lon2+'&units=m', method='GET').data
    soup = bs4.BeautifulSoup(html ,'lxml')
    tag = soup.find_all('td')[-3]
    match = re.search('[\d.]+', str(tag))
    return match.group()

def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the circle distance between two points 
    on the earth (specified in decimal degrees)
    '''
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6371 * c
    return km 
