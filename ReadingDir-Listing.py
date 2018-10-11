# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import os

g_list = []
for x in os.listdir('D:/NYTaxi/NYTaxi_2016'):
    if x.endswith(".csv"):
        g_list.append(x)

'''
Using list comprehension
'''

c_list = [x for x in os.listdir('D:/NYTaxi/NYTaxi_2016') if x.endswith(".csv")]

print(g_list == c_list)