
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
    """
    The `url` argument should be string, representing a URL for a webpage

    This function returns another string -- the raw text (i.e. HTML) found at the given URL
    """ 

def parse_headline_tags(txt):
    headline_list = [] 
    total_lines  = txt.splitlines() 
    for line in total_lines:
        if '<h3><a' in line: 
            headline_list.append(line) 
    return headline_list

    """
    The `txt` argument is a string, ostensibly text that looks like the raw HTML
      that can be found at https://wgetsnaps.github.io/stanford-edu-news/news/simple.html

1- find the sections with the headlines h3
    This function returns a list of strings, each string
        should look like the raw HTML for a standard Stanford news headline, e.g.

          [
            '<h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>',
            '<h3><a href='https://news.stanford.edu/2018/01/1/bye-stanford>Bye Stanford</a></h3>'
          ]
    """
    

    def extract_headline_text(txt):
        split_url = txt.split('>') 
        url_text_1 = split_url[2] 
        url_text_2 = url_text_1.split('<') 
        url_text_final = url_text_2[0] 
        return(url_text_final) 

    """
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"
    """
