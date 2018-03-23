from pathlib import Path
from bs4 import BeautifulSoup
import os.path
import requests


DATA_SRC_URL = 'http://stash.compciv.org/senate/ca-senate-disclosures-index.html'
# the filename of the saved page
DATA_FILEPATH = 'ca-senate-disclosures-index.html'

def scrape_site():
    fetch_data_from_web()
    html = get_html()
    data = extract_senate_list(html)
    return data


def fetch_data_from_web():
    resp = requests.get(DATA_SRC_URL)
    txt = resp.text
    if resp.status_code != 200:
        errmsg = 'Did not get an OK status when requesting: ' + DATA_SRC_URL
        raise RuntimeError(errmsg)
    else:
        print("Requested page successfully.")
        txt = resp.text
        print("Length of text:", len(txt))
        print('Saving to:', DATA_FILEPATH)
        f = open(DATA_FILEPATH, 'w')
        f.write(txt)
        f.close()

def get_html():
    if not os.path.exists(DATA_FILEPATH):
        fetch_data_from_web()
    f = open(DATA_FILEPATH, 'r')
    txt = f.read()
    f.close()
    return txt

def extract_senate_list(html):
    soup= BeautifulSoup (html, 'lxml')
    tags = soup.select('tbody tr')
    mydata= []
    for row in tags:
        d = extract_senate_row(row)
        mydata.append(d)
    return mydata

def extract_senate_row(row):
    cols = row.select('td')
    d = {}
    first_name = cols[0].text.strip().lower()
    if first_name[-2]==' ':
        split_name = first_name.split(' ')
        first_name = split_name[0]
    last_name= cols[1].text.strip().lower()
    d['name']= last_name+ ', '+ first_name
    d['category']= cols[2].text.strip()
    d['report_type'] = cols[3].text.strip()
    link = cols[3].select_one('a')
    report_dict = {}
    report_dict['url'] = link.attrs['href']
    report_dict['date'] = cols[4].text.strip()
    d['report_dict']= report_dict 
    return d
