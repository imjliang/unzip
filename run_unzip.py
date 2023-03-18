# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:59:51 2023

@author: Jinjin
"""

import os
from rarfile import RarFile
    
path = r"H:\TV\[狂飙][2023][39集全][国产剧][4K]"   
dir_list = os.listdir(path)

for dirs in dir_list:
    if not dirs.startswith("Punch"):
        continue
    rar_path = path + '//' + dirs
    for f in os.listdir(rar_path):
        if f[-3:] != 'rar': continue
        print(f)
        f_path = rar_path + '//' + f
        with RarFile(f_path, 'r') as myrar:
            myrar.extractall(path=path, pwd='123456')