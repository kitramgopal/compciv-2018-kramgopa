
import requests 
def print_hedz(url):
    txt= fetch.html(url)
    htags= parse_headline_tags(txt)
    for t in htags:
        hedtxt=extract_headline_text(t)
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
    line_list = txt.split('<h3>')
    del line_list[0] 
    length = len(line_list)
    print(len(line_list))


def parse_headline_tags(txt):
    head_start = txt.split('<head>')
    head = head_start[1].split(</head>)
    '''list_of_lines = txt.split[?]'''
    '''num_lines = list_of_lines.length'''
    for num_lines in list_of_lines:

    
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
    """
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"
    """




           



'''def extract_headline_text(txt):
    stuff= txt.split
    stuff[2]
    s.spli('>')[2]


for t in parse_headlines_tags
h3><a

for line in lines():