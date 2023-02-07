# -*- encoding: utf-8 -*-
'''
    @File    :   test1.py
    @Time    :   2023/02/07 23:21:49
    @Author  :   Tomas Wu 
    @Contact :   tomaswu@qq.com
    @Desc    :   
'''

import tqdm
import time

for i in tqdm.tqdm(range(100)):
    # print(i)
    time.sleep(0.1)