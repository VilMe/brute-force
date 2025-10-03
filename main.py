import itertools
import string
import time

def common_guesss(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()


    for i, match in enumerate(word_list, start=1):
        if match == word: 
            return f'Common match: {match} (#{i})'
        
def brute_force (word: str, length, int, digits: bool):
