"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item_str = str(item)
        frequencies.setdefault(item_str, 0)
        frequencies[item_str] += 1
    return frequencies
