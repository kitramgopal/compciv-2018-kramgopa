from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso


def get_inmate_data():
    """
    A convenient wrapper function that wraps up all the other sub/helper
        functions so that the user of the scraper.py script need only
        to invoke this to get the nice and clean data.

        import scraper
        data = scraper.get_data()

    Returns:
        <list>: A list of dict objects, with the dict objects as defined in
            the documentation of the wrangle_inmate_data_from_tag()
            function
    """
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data


def get_and_parse_inmate_rows():
    txt = data_helper.get_html()  #str: the contents of the file at DATA_FILEPATH as a big text string
    soup = BeautifulSoup(txt, 'lxml')
    records = soup.select('tr')[1:]
    return records



def wrangle_inmate_data_from_tag(rowtag):
    d = {}

    cols = rowtag.select('td')
    d['tdcj_id'] = cols[0].text.strip()
    d['url'] = make_absolute_url(cols[1].a['href'])
    d['last_name']= cols[2].text.strip()
    d['first_name']= cols[3].text.strip()
    d['birthdate']= txdate_to_iso(cols[4].text.strip())
    d['gender']= cols[5].text.strip()
    d['race']= cols[6].text.strip()
    d['date_received']= txdate_to_iso(cols[7].text.strip())
    d['county'] = cols[8].text.strip()
    d['date_offense']= txdate_to_iso(cols[9].text.strip())
    d['age_at_offense']=round(calc_years_diff(d['birthdate'],d['date_offense']))
    d['years_before_death_row']= float(calc_years_diff(d['date_offense'], d['date_received']))
    return d



    """
    'years_before_death_row', which is a float
                              (rounded to nearest tenth) derived
                              from date of offense and date received, i.e.
                              number of years between commission of crime and entering
                              death row.
    Args:
        rowtag: a BeautifulSoup <Tag> object, ostensibly representing a table row
            from a parsed Texas death row HTML table, e.g.

            <tr>
            <td>999608</td>
            <td align="center"><a href="dr_info/hudsonwilliam.html" title="Offender Information for William Hudson">Offender Information</a></td>
            <td>Hudson</td>
            <td>William</td>
            <td>07/03/1982</td>
            <td align="center">M</td>
            <td>White</td>
            <td>11/16/2017</td>
            <td>Anderson</td>
            <td>11/14/2015</td>
            </tr>

    Returns:
        <dict>: A dictionary object that contains some of the values in
            the HTML, with formatting where standardization is needed --
            e.g. for dates and for the inmate's URL (absolute vs relative)
            and some derived attributes, e.g. 'age_at_offense'

            The value for 'url' should be an absolute URL, i.e. a valid
               URL on the Web, not a relative one.

            'birthdate', date_received', 'date_offense' should be in 'YYYY-MM-DD'
                format

            All values are strings except for:
               'age_at_offense', which is an integer derived from birthdate and
                                 date of offense

               'years_before_death_row', which is a float
                              (rounded to nearest tenth) derived
                              from date of offense and date received, i.e.
                              number of years between commission of crime and entering
                              death row.

    ### fill in yourself
    ### (this one will be pretty long, though it's mostly tedious/repetitive steps)



**   resp= requests.get(DATA_SRC_URL)
    resp_text = resp.text
    soup = BeautifulSoup(BeautifulSoup(resp_text))
    return resp_text
    soup= 
    rows = soup.select('tr')
    for r in rows:
        r =rows[5]
        tag = r.select('td a')[1]
        tag.attrs['href']
        urljoin('fullurl', tags.attrs)





        e.g.
            {
                'tdcj_id': '999608',
                'url': 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html',
                'last_name': 'Hudson',
                'first_name': 'William',
                'birthdate': '1982-07-03',
                'gender': 'M',
                'race': 'White',
                'date_received': '2017-11-16',
                'date_offense': '2015-11-14',
                'age_at_offence': 33,
                'years_before_death_row': 2.0
            }
    """
