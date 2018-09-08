# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:10:07 2018

@author: Majoy
"""

txt = input('Please enter text: ')
reward = "coke sakto"
num = txt[0]
txt = txt[:-1]
txt = txt[1:]
txt = txt.strip()

print('Hi {}! You have successfully redeem reward #{}-{}! Thank you for choosing Aling Nena’s Sari-sari store.'.format(txt.title(), num, reward))