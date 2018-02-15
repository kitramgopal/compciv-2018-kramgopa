from datetime import datetime
from urllib.parse import urljoin
import data_helper


def txdate_to_iso(datestr):
    m,d,y = datestr.split('/')

    if len(y) != 4:
        y = '19' + y

    return '-'.join([y,m,d])



def calc_years_diff(start_date, end_date):
   sd = datetime.strptime(start_date, '%Y-%m-%d')
   ed = datetime.strptime(end_date,'%Y-%m-%d')
   diff = ed - sd
   diffyears= diff.days/365
   
   return round(diff.days / 365, 1)



def make_absolute_url(href):
    return urljoin(data_helper.DATA_SRC_URL, href)



 
        
