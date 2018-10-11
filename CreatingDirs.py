# -*- coding: utf-8 -*-
"""
Folder creating
"""

import os


for i in range(2009, 2015):
    if not os.path.exists('D:/NYTaxi/NYTaxi_' + str(i)):
        os.makedirs('D:/NYTaxi/NYTaxi_' + str(i))
        