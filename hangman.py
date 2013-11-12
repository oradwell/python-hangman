from fileinput import input
from linecache import getline
from random import randint

class Phrase:
    _chars_as_is = [" ", "-"]

    def __init__(self, text):
        self.text = text

        self.chars = set()
        for char in text:
            if char not in self._chars_as_is:
                self.chars.add(char.lower())

    def __str__(self):
        return self.text

    def show(self, guessed_chars):
        for char in self.text:
            if char in self._chars_as_is or char in guessed_chars:
                print(char),
            else:
                print("_"),

        print("")

class WordList:
    _filename = "wordlist"

    def __init__(self, mode):
        self._lines_used = []
        self._num_used = 0
        self._num_lines = 0
        self._mode = mode
        if mode == "sequential":
            return

        self._init_random()

    def get_phrase(self):
        if self._mode == "sequential":
            for line in input(self._filename):
                text = self._clean_phrase(line)
                if not text:
                    continue

                yield Phrase(text)
        else:
            while self._num_used < self._num_lines:
                line_num = self._get_random_line_num()
                line = getline(self._filename, line_num)

                text = self._clean_phrase(line)
                if not text:
                    continue

                yield Phrase(text)

    def _init_random(self):
        self._count_lines()

    def _get_random_line_num(self):
        while True:
            line_num = randint(1, self._num_lines)
            if line_num not in self._lines_used:
                self._num_used += 1
                self._lines_used.append(line_num)
                return line_num

    def _clean_phrase(self, line):
        phrase = line.strip()
        if len(phrase) < 1 or phrase[0] == '#':
            return False
        
        return phrase

    def _count_lines(self):
        for line in input(self._filename):
            self._num_lines += 1


print "=================="
print "= Python Hangman ="
print "=================="

# constants
MAX_GUESS = 9

wl = WordList("random")

quit = False
# START main loop
for phrase in wl.get_phrase():
    wrong_guess = 0
    incorrect_guesses = set()
    correct_guesses = set()

    # START inner loop
    # While wrong guesses hasn't reached max guesses 
    # and not all the characters are guessed
    while wrong_guess < MAX_GUESS and phrase.chars != correct_guesses:
        # Show number of guesses used out of allowed guesses
        print "%d/%d" % (wrong_guess, MAX_GUESS)
        
        phrase.show(correct_guesses)

        inchar = raw_input("Enter character (or quit): ")
        inchar = inchar.strip()
        if not inchar:
            continue

        inchar = inchar.lower()
        if inchar == 'quit' or inchar == 'exit':
            quit = True
            break

        inchar = inchar[0]
        print "You entered: %s" % inchar

        # Check if the character is in the phrase
        if inchar in phrase.chars:
            print "correct!"
            correct_guesses.add(inchar)
        elif inchar not in incorrect_guesses:
            print "incorrect!"
            wrong_guess += 1
            incorrect_guesses.add(inchar)
        else:
            print "incorrect!"

        print "Correct guesses: %s" % correct_guesses
        print "Incorrect guesses: %s" % incorrect_guesses
        print "Chars in phrase: %s" % phrase.chars
        
        # END inner loop

    print "Phrase: %s" % phrase
    if quit:
        break
    # END main loop
