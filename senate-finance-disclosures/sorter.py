#From pathLib import Path
from bs4 import BeautifulSoup
import scraper

def make_url_list():
    cur_sen = filter_senators()
    name_list = tally_names (cur_sen)
    new_sen_list = [] #a new list of dictionaries with (senator name, a list of dictionaries with url-date)
    for name in name_list: #runs through name list
        sen_dict = {} #creates a new senature
        sen_dict['name'] = name 
        report_list = []
        for sen in cur_sen: #checks every dict per name in name list, isolates each dict
            if name == sen['name']: #isolates 
                report_list.append(sen['report_dict'])
        sen_dict['report list']=report_list
        new_sen_list.append(sen_dict)
    return new_sen_list #returns a list of dicts with senators and a list of their URLS to annual reports
            
def filter_senators():
    all_sen = scraper.scrape_site() #get list with dictionary for every report row
    sen_ar_cy = find_asset_reports(all_sen) # list of dictionaries, filters out all non-annual reports
    #cur_sen = find_current_sen(all_sen)
    return sen_ar_cy

def find_asset_reports(all_sen):
    ar_only_list=[]
    for sen_dict in all_sen:
        report_dict = sen_dict['report_dict']
        url = report_dict['url']
        if '/search/view/annual/' in url:
            ar_only_list.append(sen_dict)
    return ar_only_list

def find_current_sen(all_sen):
    curr_only_list=[]
    for row in all_sen:
        if row['category'] == ('Senator'):
            del row['category'] #unnecessary
            curr_only_list.append(row)
    return curr_only_list

def tally_names (cur_sen):
    names = []
    for row in cur_sen:
        if row['name'] in names:
            continue
        else:
            names.append(row['name'])
    return names





#_
