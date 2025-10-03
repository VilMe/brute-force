import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()


    for i, match in enumerate(word_list, start=1):
        if match == word: 
            return f'Common match: {match} (#{i})'
        
def brute_force (word: str, length, int, digits:bool = False, symbol:bool = False):
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols;
        chars += string.punctuation


    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess; str = ''.join(guess)


        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        
        print(guess, attempts)

        
    



if __name__ == '__main__':
    print(common_guess('carrot'))