# Author: Faith Elledge
# Date: 11/5/22
# user: elledgef
# Description:


def is_subsequence(string_a, string_b):

    if string_a == "":
        return True
    if string_b == "":
        return False
    if string_a[1] == string_b[1]:
        return is_subsequence(string_a[1:], string_b[1:])
    else:
        return is_subsequence(string_a, string_b[1:])



