from datastubs import PEOPLE_LIST

from operator import itemgetter

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return p['age']
    return sorted(PEOPLE_LIST, key =foolen)    
    

def oldest():
    """
    sort by age in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return p['age']
    return sorted(PEOPLE_LIST, key =foolen, reverse= True)    
    

def name_reverse_alpha():
    return sorted(PEOPLE_LIST, key=lambda x: x['name'], reverse=True)


def country_then_age():
    def ca(p):
        country = p['country']
        age = p['age']
        return (country, age)
    return sorted(PEOPLE_LIST, key = ca)

