# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:36:37 2021

@author: mcolwell
"""
import csv
import string
import random
  
CheckerA = ['Correctness']

def gen(flip_check_every, output_length):
  lettersA = ['LettersDisplayed']
  
  for idx in range(output_length):
    letter = random.choice(string.ascii_letters)
    if len(lettersA) < flip_check_every:
      lettersA.append(letter)
      CheckerA.append('None')
      continue
    elif random.choice([True, False]) and idx % flip_check_every == 0:
      lettersA.append(lettersA[-flip_check_every])
      CheckerA.append('space')
    else:
      lettersA.append(letter)
      CheckerA.append('None')

  return lettersA

ListA = gen(2, 50)
ListB = CheckerA

fl = open('Conditions/twoback.csv', 'w', newline='')

writer = csv.writer(fl)
writer.writerows(zip(ListA, ListB))##
    
fl.close()