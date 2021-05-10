# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:45:32 2021

@author: Dom Horard
"""

from Entry import Entry

if __name__ == '__main__':
    entry = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'+ \
        ' Sed vel nunc quis elit cursus posuere a vitae ligula.'+ \
            ' Suspendisse luctus.'
    
    entry = Entry(entry)
    print(entry.get_all_words())
    print(entry.is_paragraph_length())
    print(entry)
    print(entry._Entry__get_word(3))
    
    #Asserting that the length of the entry is only 3 words
    #Present custom message to test wrong assertion
    assert entry.entry_len == 3, 'Not the length of the string'
    
    #Asserting the wrong text is the entry instance
    assert entry == 'This is not the entry', 'Not the entry'