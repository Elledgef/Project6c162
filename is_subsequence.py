# Author: Faith Elledge
# Date: 11/5/22
# user: elledgef
# Description: This code takes two strings as parameters and returns True if string A is subsquence of
#string B or returns false if otherwise


def is_subsequence(string_a, string_b):
    """ This function returns true if string A is subsquence of string B or returns False if not
    subsquence """
    if string_a == "":
        return True
    if string_b == "":
        return False
    if string_a[0] == string_b[0]:
        return is_subsequence(string_a[1:], string_b[1:])
    else:
        return is_subsequence(string_a, string_b[1:])



