# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:59:51 2023

@author: Jinjin
"""

import os
from rarfile import RarFile
from zipfile import ZipFile
import py7zr
            
def extractProtectedRAR(path, prefix=None, pwd=None):
    dir_list = os.listdir(path)
    for dirs in dir_list:
        if prefix and not dirs.startswith(prefix):
            continue
        rar_path = path + '//' + dirs
        for f in os.listdir(rar_path):
            if f[-3:] != 'rar': continue
            print(f)
            f_path = rar_path + '//' + f
            with RarFile(f_path, 'r') as myrar:
                myrar.extractall(path=path, pwd=pwd)
    return

def extractZIP(dirPath):
    files = os.listdir(dirPath)
    for fname in files:
        print(fname)
        p =  os.path.join(dirPath, fname)
        with ZipFile(p, 'r') as zObject:        
            # Extracting all the members of the zip 
            # into a specific location.
            zObject.extractall(
                path=dirPath)            
    return

def extract7z(dirPath, pwd):
    files = os.listdir(dirPath)
    for fname in files:
        print(fname)
        p =  os.path.join(dirPath, fname)
        if p[-3:] != '.7z': 
            continue
        with py7zr.SevenZipFile(p, mode='r', password=pwd) as z:
            z.extractall(dirPath)
    return

if __name__ == '__main__':
    
    path = r"H:\TV\[狂飙][2023][39集全][国产剧][4K]"
    # extractProtectedRAR(path, prefix = 'Punch', pwd = '123456')
    
    path = r"H:\TV\[韩国] [黑暗荣耀][全网最强版][两季全16集][2022][超清4K][单集6G][韩语中字][MKV]\S01.2160p.2022"
    path = r"H:\TV\[韩国] [黑暗荣耀][全网最强版][两季全16集][2022][超清4K][单集6G][韩语中字][MKV]\S02.2160p.2023"
    # extractZIP(path)
    
    path = r'H:\综艺节目\[大陆] [脱口秀大会第1季][12期全][2017][国语中字][mkv12.52G][1080P]'
    extract7z(path, 'ROCKandROAST') 