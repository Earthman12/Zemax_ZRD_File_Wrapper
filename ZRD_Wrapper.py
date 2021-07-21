# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:15:13 2021

@author: Earthman
"""

import pyzdde.zfileutils as zfu
import matplotlib.pyplot as plt

filePath = './assym_v3_uncompressed.ZRD'

try:
    zrd = zfu.readZRDFile(filePath)
    
except Exception as e:
    print(e)
    
print("Number of rays in the uncompressed ZRD file = ", len(zrd))
zrdList = zrd[0]

print(zrdList.intensity)