# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:03:10 2021

@author: Dom Horard
Class for an entry object that will have methods to count words
"""
import string

class Entry():
    '''Entry class with 4 methods'''
    
    #Constructor that calls on the object itself, and there is a default
    #value for sentence of an empty string
    def __init__(self, entry = ''):
        '''initializer for the Class Object instance'''
        #defing an empty list to append words from the sentence into in a list
        #for the other object methods
        self.word_list = [word for word in entry.split()]
        
        #Calculate the length of the entry list
        self.entry_len = len(self.word_list)
        

        #self is referring to the relevant, calling, object
        #assigning input argument to instance variable as a private attribute
        self.__entry = entry
        
    
    #Object method to get all the words in the sentence
    def get_all_words(self):
        '''Get all the words from the sentence list'''
        import string
        
        #Using the string module, stripping the words in the list of any
        #punctuation marks
        self.pure_word_list = [word.strip(string.punctuation) for word in \
                               self.word_list]
        
        #Returning the list of words to the user
        return f'List of words from the sentence: {self.pure_word_list}'
    
    #Method that will return to the user an overview of how many words are
    #in their entry, and if it is considered paragraph length
    def is_paragraph_length(self):
        
        # #Calculate the length of the entry list
        # self.entry_len = len(self.word_list)
        
        #halfway point of the entry
        self.half_len = self.entry_len % 2
        
        #Average length of a paragraph in words
        avg_paragraph_length = 200
        
        #Difference of the length of the entry and the average paragraph
        word_diff = self.entry_len - avg_paragraph_length
        
        if word_diff > 0:
            return 'Your entry is longer than a paragraph'
        
        if word_diff < 0:
            return 'Your entry is shorter than a paragraph'
        
        if word_diff == 0:
            return 'Your entry is exactly the length of a paragraph'
    
    
    def __get_word(self, index):
        '''Get a specific word from the index in the pure word list'''
        
        #Using the string module, stripping the words in the list of any
        #punctuation marks
        self.pure_word_list = [word.strip(string.punctuation) for word in \
                               self.word_list]
        
        #Defining variable that is the value of a word in the pure word list
        #that the user entered an idex value for
        self.pure_word_list[index]
        
        #Return the word at the specified index
        return f'{self.pure_word_list[index]}'
        
    def __repr__(self):
        #Calculate the length of the entry list
        self.entry_len = len(self.word_list)
        '''Used to print entry object'''
        # return 'The original sentence was: ', self.__sentence
        # return 'The new sentence is: ', ' '.join(self.pure_word_list)
        return f'Your entry is {self.entry_len} words long'