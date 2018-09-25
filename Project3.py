#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:22:26 2018

COSC 1010 - Project 3 (WordFinder)
<>
@author: jackdansbury
"""

import string
from itertools import chain

#Method removes all punctuation from a string
def remove_punctuation(s1):
    #returns the string with all punctuation removed
    return ''.join(word for word in s1 if word not in string.punctuation)

#print(remove_punctuation("@Hel%lo!! how are you?"))

def get_file_name_input(): #takes file input, opens file, preprocesses, returns line num dict 
    user_input=input('Give me a file name with extension: ')
    try:
        with open(user_input,'r') as f:
            proc_lines = f.readlines()                                              #lowercase
            proc_lines = [remove_punctuation(line).lower() for line in proc_lines]  #and no punctuation
            global line_num_dict                   #key=linenum value=[list of words in line]
            line_num_dict = {i:line.split() for (i,line) in enumerate(proc_lines, start = 1)}
            lnd_values = [s1 for s1 in line_num_dict.values()] #nested lists of each line in one list
            all_words = set(list(chain(*lnd_values))) #combines nested lists into a set (no duplicates)  
            global word_dict #creates dict for each word:set of line numbers where word found 
            word_dict = {word:set(i for i in line_num_dict 
                                if word in line_num_dict[i])
                                for word in all_words}
        return word_dict
    except OSError:
        print('***Error: File not found. Try Again.***')
        return get_file_name_input() #runs itself until it opens a file
        
        
def find_input_location(user_input): #searches input from word_seach()
    user_input = user_input.lower()
    try:
        location = word_dict[user_input]
        return location
    except KeyError:
        words = user_input.split()
        location = set(i for i in line_num_dict 
                       if all(word in line_num_dict[i] for word in words))
        return location
    
def word_search(): #takes input and either quits program or searches words
        user_input = str(input('''Enter the word(s) you want to look up, seperated by a white space.
                           \nYou may quit by entering 'q':'''))
        if user_input in 'qQ':
            pass 

        else:
            result = sorted(list(find_input_location(user_input)))
            print('\n\t\tFound in Line(s): ',result)
            return word_search()

def main_2(): #call to run
    get_file_name_input() #opens file, returns word dict
    word_search() #takes word(s) as input, returns its location in a sorted list 
        

 main_2()



#test with files

#1. prob3.txt
#2. HP_and_the_Sorcerers_Stone.rtf


####Print full {Word:{LineNumber(s)}} for any file
   ###chronological order:
#print(get_file_name_input)
   ###alph. order:
#get_file_name_input()
   

