from data_helper import get_html
from bs4 import BeautifulSoup



def get_and_parse_inmate_rows():
    txt = get_html()   #str: the contents of the file at DATA_FILEPATH as a big text string
    soup = BeautifulSoup(txt, 'lxml')
    records = soup.select('tr')[1:]
    return records

    """
    Uses get_html() -- via data_helper module --
      to get HTML for parsing. Then uses BeautifulSoup
      to parse it. Then uses the .select() method to
      pick the Tag elements that contain inmate info

    Args:
        none

    Returns:
        <list>: a list of <bs4.Element.Tag> objects, each one looking like:

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
    """

    ## fill this out for yourself...



def count_inmates():
    rows= get_and_parse_inmate_rows()
    return len(rows)
    """
    Counts the inmates on Texas death row based on the data
     parsed via get_and_parse_inmate_rows()

    Args:
        None

    Returns:
        <int>
    """
