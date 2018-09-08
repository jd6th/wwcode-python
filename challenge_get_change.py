# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:44:44 2018

@author: Majoy
"""

totalbill = input('How much is your total bill?')
payment = input('How much is your payment?')

change =  float(payment) - float(totalbill)

print('Hi! Your change is {}'.format(change, '.2f'))  
