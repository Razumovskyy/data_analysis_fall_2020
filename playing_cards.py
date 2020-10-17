# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:03:32 2020

@author: Razumovskiy Mikhail
"""

import random as rd
import scipy.special as spp

N = 100000 
rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'hearts', 'diamonds', 'clubs'] 
deck = [] 

for i in rank:
    for j in suits:
        deck.append (i + '_' + j)

count = 0
sub_suits = []

for i in range (N):
    rd.shuffle(deck)
    for j in range (3):
        sub_suits.append(deck[j].partition('_')[2])
    if sub_suits[0] == sub_suits [1] == sub_suits[2]:
        count += 1
    sub_suits.clear()

print ('Number of experiments is {}. Experimental probability is {:.4f}'.format(N, count/N))
print ('Theoretical probability is {:.4f}'.format((4 * spp.binom(13, 3))/spp.binom(52, 3)))

    