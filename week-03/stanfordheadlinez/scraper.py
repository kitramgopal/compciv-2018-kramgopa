def print_hedz (url):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)
    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)


def fetch_html(url):
    import requests 
    a = requests.get(url)
    txt= a.text  
    return txt 


def parse_headline_tags(txt):
    mylist = [] 
    lines  = txt.splitlines() 
    for line in lines:
        if '<h3><a' in line: 
            mylist.append(line) 
    return mylist

def extract_headline_text(txt):
        split_url = txt.split('>') 
        url_text_1 = split_url[2] 
        url_text_2 = url_text_1.split('<') 
        url_text_final = url_text_2[0] 
        return(url_text_final) 

