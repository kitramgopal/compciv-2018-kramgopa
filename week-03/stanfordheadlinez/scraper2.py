
import requests 


def print_hedz(url):
    html_txt= fetch.html(url)
    htags_url_list= parse_headline_tags(txt)  #stores list of headline htmls
    for i in htags_url_list:
        hedtxt=extract_headline_text(i)
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
    line_list = txt.splitlines() #creates a list with every line
    headline_lines = [] #initializes empty list to store headlines
    for line in line_list: #reads every line in line list
        if '<h3><a' in line_list: #sees if headline marker is there 
            headline_lines.append(line_list(line)) #stores relevant line in list
    return headline_lines #returns list--> save as variable

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
        url_text_2 = url_text_raw.split('<')
        url_text_final = url_text_2[1]
        return(url_text_final)

    """
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"
    """



'''def scraper(url):
html_block = printhez(url)
headline_html = parse_headline_tags (html_block) #stores list of headline htmls
list_length = len(headline_html) #integer length of string
headline_text = [] #initiates a list for headline text
for i in range(list_length):
    headline = headline_html[i] #gets the next headline html in the list
    textOnly = extract_headline_text(headline) #saves the headline text for the url
    headline_text.append() #adds it to the list

    '''