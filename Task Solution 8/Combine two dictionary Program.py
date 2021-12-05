# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:26:27 2021

@author: Guruprasada Shridhar Hegde
"""
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

