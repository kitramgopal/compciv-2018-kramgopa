#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """
    return type(ez_list)



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
   return ez_list[0]



def foo_b():
   a= ez_list[1]
   b= ez_list[3]
   c= a +b
   return c



def foo_c():
    return ez_list[-1]
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """


def foo_cx():
    return type(ez_list[-2])
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """


def foo_d():
    sequence = ez_list[-2]
    return sequence[-1]
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """


def foo_e():
    return len(ez_list)
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """


def foo_f():
    sixth_member = ez_list[5]
    semicolon_string=';'.join(sixth_member)
    return semicolon_string

    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """


def foo_g():
    list1 = []
    for i in range(1,5):
        list1.append(ez_list[i])
    return list1
    """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """


def foo_h():
    list2 = []
    for i in range(1,4):
        list2.append(ez_list[-i])
    return list2
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """

