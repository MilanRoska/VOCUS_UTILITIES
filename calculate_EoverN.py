# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 11:28:16 2025

@author: m.roska
"""

# %% chanel
# votlage grad IMR
U = 510
kb = 1.380649*10**(-23)
# t in K
T = 273.15+60
# p in bar converted to pascal
p = 0.003 *10**5
# vocus imr 10 cm
l = 0.1

# in Td (V*cm**2)
EN = ((U / l)*kb *T/p ) / 10**(-21)

# %% aeromma

U = 500
kb = 1.380649*10**(-23)
T = 273.15+40
p = 0.0032 *10**5
l = 0.1
EN2 = ((U / l)*kb *T/p ) / 10**(-21)


