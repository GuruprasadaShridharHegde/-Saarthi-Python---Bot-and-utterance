# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:04:05 2021

@author: Guruprasada Shridhar Hegde
"""
# Python3 code to demonstrate working of
# Unique dictionary filter in list
# Using map() + set() + items() + sorted() + tuple()

# Initialize list
dict_list = Input
            dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

            output=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}]

# printing original list
print("The original list is : " + str(test_list))

# Unique dictionary filter in list
# Using map() + set() + items() + sorted() + tuple()
res = list(map(dict, set(tuple(sorted(sub.items())) for sub in test_list)))

# printing result
print("The list after removing duplicates : " + str(res))


