#!/usr/bin/python
#coding:utf-8
import string
def vulcan(s1,s2):
    S1 = str.capitalize(s1)
    S2 = str.capitalize(s2)
    if S1 < S2:
	return -1
    if S1 > S2:
	return 1
    return 0


print sorted(['bob','about','Zoo','Credit'],vulcan)

