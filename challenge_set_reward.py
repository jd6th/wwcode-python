# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:10:07 2018

@author: Majoy
"""
txt = input('Please enter text: ')

num = txt[0]
txt = txt[:-1]
txt = txt[1:]
txt = txt.strip()


rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]

print('Hi {}! You have successfully redeem reward #{}-{}! Thank you for choosing Aling Nena’s Sari-sari store.'.format(txt.title(), num, rewards[int(num)]))
