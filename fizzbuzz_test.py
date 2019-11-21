#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fizzbuzz import fizzbuzz

def test_passing_3_returns_fizz():
    assert fizzbuzz(3) == 'FIZZ'
    assert fizzbuzz(99) == 'FIZZ'
    assert fizzbuzz(15) == 'FIZZ'
    
def test_passing_5_returns_buzz():
    assert fizzbuzz(5) == 'BUZZ'
    assert fizzbuzz(10) == 'BUZZ'
    assert fizzbuzz(20) == 'BUZZ'
    
def test_passing_other_number_returns_itself():
    assert fizzbuzz(4) == 4
    assert fizzbuzz(1) == 1
    assert fizzbuzz(23) == 23