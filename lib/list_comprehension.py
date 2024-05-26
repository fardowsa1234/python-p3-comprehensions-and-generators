#!/usr/bin/env python3

def return_evens(num_list):
    # Use a list comprehension to filter out even numbers
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # Use a list comprehension to add an exclamation mark to each sentence
    return [sentence + "!" for sentence in sentence_list]

def test_return_empty_list_if_odds():
    '''returns empty list when num_list has no evens'''
    num_list = range(1, 10, 2)
    assert return_evens(num_list) == []

def test_return_evens():
    '''returns evens from num_list'''
    num_list = range(10)
    assert return_evens(num_list) == [0, 2, 4, 6, 8]

def test_return_empty_list_if_empty_input():
    '''returns empty list when sentence_list is empty'''
    assert make_exclamation([]) == []

def test_return_exclamation_list():
    '''returns list of sentences with exclamation marks'''
    sentence_list = [
        "I like computers",
        "I require coffee",
        "Live long and prosper",
    ]
    assert make_exclamation(sentence_list) == [
        "I like computers!",
        "I require coffee!",
        "Live long and prosper!",
    ]



