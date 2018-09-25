#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:40:21 2018

@author: jackdansbury
"""
import sys
from operator import itemgetter


def get_input_letters(): #takes user input and verifies that it contains only letters and is ≤7, 
    input_is_only_letters=False #returns string converted to uppercase
    while not input_is_only_letters:
        letters = str.upper(input('Enter up to 7 letters:\n\n>>>'))
        if letters.isalpha() and len(letters) <= 7:
            input_is_only_letters = True
        elif len(letters)>7:
            print('Please enter no more than 7 letters')
        else:
            print('Please enter only letters A-Z (not case sensitive)')
    return letters

def list_words_from_file(): #opens wordlist.txt and generates list of words
    wordlist=[] #seperated by each line
    with open('wordlist.txt', 'r',encoding='utf-8') as f:
        wordlist=list(line.strip('\n') for line in f)
    return wordlist

def set_words_from_file(): #opens wordlist.txt and generates set of words
    with open('wordlist.txt','r',encoding='utf-8') as f:
        wordset=set(line.strip('\n') for line in f)
    return wordset

#OPTION_1
def verify_input_word(): #checks if input is in word set
    input_word=get_input_letters()
    word_set=set_words_from_file()
    if input_word in word_set:
        print('\n\t\t',input_word, 'is a valid word')
    else:
        print('\n\t\t',input_word, 'is invalid')

#OPTION_2
def word_finder(): #find words that match input letters
    words=[]
    input_letters=get_input_letters() 
    word_list=list_words_from_file()
    for word in word_list:
        match=True
        letterlist=list(input_letters) #convert input letters from str to list
        for letter in word:
            if letter not in letterlist:
                match=False #stops checking rest of the word's letters
                break #if word has a letter not in letterlist
            else:
                letterlist.remove(letter) #only for current word so no letter is used twice
        if match==True: #if all letters from word are in letterlist
            words.append(word) #add word to list of possible words               
    return words
#used w/ option 3 and 4
letter_score={'A':1,'B':3,'C':3,'D':2,'E':1,
              'F':4,'G':2,'H':4,'I':1,'J':8,
              'K':5,'L':1,'M':3,'N':1,'O':1,
              'P':3,'Q':10,'R':1,'S':1,'T':1,
              'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

def word_score(word): #finds sum of the scores for each letter of a word 
    word=str.upper(word)
    word_total=0
    for letter in word:
        word_total+=letter_score[letter]
    return word_total

#OPTION_3
def list_word_scores(): #prints score & word for all possible words
    words=word_finder() #by highest score
    word_scores=[(word_score(word),word) for word in words]
    for (points,word) in sorted(word_scores,reverse=True):
        print(points, word)
        
#OPTION_4
def get_best_word(): #prints score & word(s) for the highest value only
    words=word_finder()
    word_scores=[(word_score(word),word) for word in words]
    ordered_ws=[sorted(word_scores,reverse=True)]
    high_score=max(ordered_ws,key=itemgetter(1))[0]
    hs=high_score[0]
    final=[word for word in word_scores if word[0]==int(hs)]
    for (points,word) in final:
        print(points, word)
        
def get_OPTION_command(): #runs after options. takes 1 or 2 as input
    input_is_valid=False
    valid=['1','2']
    while not input_is_valid:
        user_input=input('Enter "1" to go again,\nEnter "2" to return to the main menu\n:')
        if user_input in valid:
            input_is_valid=True
        else:
            print('Please choose option "1" or "2"')
    return user_input
           
#WORD CHECk
def OPTION_1():
    exit_to_main=False
    print(60*'-')
    print("|{}{:17}{:^}{:16}{}|".format(3*'*',' ','WORD GAME ASSISTANT',' ',3*'*'))
    print(60*'-')
    print('{:<20}{}'.format('[1]','***WORD CHECK***'))
    verify_input_word()
    while not exit_to_main:
        user_command=get_OPTION_command()
        if int(user_command)==1:
            verify_input_word()
        elif int(user_command)==2:
            exit_to_main=True
            _MAIN_()
#WORD FINDER
def OPTION_2():
    exit_to_main=False
    print(60*'-')
    print("|{}{:17}{:^}{:16}{}|".format(3*'*',' ','WORD GAME ASSISTANT',' ',3*'*'))
    print(60*'-')
    print('{:<20}{}'.format('[2]','***WORD FINDER***'))
    print(word_finder())
    while not exit_to_main:
        user_command=get_OPTION_command()
        if int(user_command)==1:
            print(word_finder())
        elif int(user_command)==2:
            exit_to_main=True
            _MAIN_()

#WORD & SCORE FINDER   
def OPTION_3():
    exit_to_main=False
    print(60*'-')
    print("|{}{:17}{:^}{:16}{}|".format(3*'*',' ','WORD GAME ASSISTANT',' ',3*'*'))
    print(60*'-')
    print('{:<17}{}'.format('[3]','***WORD & SCORE FINDER***'))
    list_word_scores()
    while not exit_to_main:
        user_command=get_OPTION_command()
        if int(user_command)==1:
            list_word_scores()
        elif int(user_command)==2:
            exit_to_main=True
            _MAIN_()

#BEST WORD
def OPTION_4():
    exit_to_main=False
    print(60*'-')
    print("|{}{:17}{:^}{:16}{}|".format(3*'*',' ','WORD GAME ASSISTANT',' ',3*'*'))
    print(60*'-')
    print('{:<20}{}'.format('[4]','***BEST WORD***'))
    get_best_word()
    while not exit_to_main:
        user_command=get_OPTION_command()
        if int(user_command)==1:
            get_best_word()
        elif int(user_command)==2:
            exit_to_main=True
            _MAIN_()
      
#Takes 1,2,3,4,5 as valid input for main menu options
def get_MAIN_command():
    input_is_valid=False
    valid=['1','2','3','4','5']
    while not input_is_valid:
        user_input=input('>>>')
        if user_input in valid:
            input_is_valid=True
        else:
            print('Please choose option 1,2,3,4, or 5')
    return user_input
        

def execute_MAIN_command(command):
    user_input=int(command)
    exit_program = False
    while not exit_program:
        if user_input==5:
            exit_program=True
            print('\n\t\t\tGoodbye!')
            sys.exit()
        elif user_input==1:
            OPTION_1()
        elif user_input==2:
            OPTION_2()
        elif user_input==3:
            OPTION_3()
        elif user_input==4:
            OPTION_4()

def _MAIN_():
    print(60*'-')
    print("|{}{:17}{:^}{:16}{}|".format(3*'*',' ','WORD GAME ASSISTANT',' ',3*'*'))
    print(60*'-')
    print('|{:25}{:^}{:24}|'.format(' ','MAIN MENU',' '))
    print('|{:52}|{:60}|{:<20}|{:14}|{:3}|{:7}|{:45}|{:60}|'.format('\tOPTIONS:',
          '\n|','\n|  "1" to verify that you have a valid word\t\t   ',
          '\n|  "2" to find valid words from your letters\t\t   ',
          '\n|  "3" for all words in order by score from your letters   ',
          '\n|  "4" for just the highest scorer from your letters\t   ',
          '\n|  "5" to EXIT\t\t\t','\n|'))
    print(60*'-')
    execute_MAIN_command(get_MAIN_command())


_MAIN_()

