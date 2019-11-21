#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fizzbuzz(number):
    if number % 3 == 0:
        return "FIZZ"
    elif number % 5 == 0:
        return "BUZZ"
    else:
        return number