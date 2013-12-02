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

    def get_char(self, guessed_chars):
        for char in self.text:
            if char in self._chars_as_is or char in guessed_chars:
                yield char
            else:
                yield "_"

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

class HangmanGame:
    max_guess = 9

    def __init__(self, phrase):
        self.wrong_guess = 0
        self.incorrect_guesses = set()
        self.correct_guesses = set()
        self.phrase = phrase

    def is_finished(self):
        return (self._is_max_guess_reached() or 
            self._is_phrase_guessed_correctly())

    def get_result(self):
        if self._is_phrase_guessed_correctly():
            return 'correct'
        if self._is_max_guess_reached():
            return 'max_reached'

        return False

    def guess(self, char):
        if char in self.phrase.chars:
            self.correct_guesses.add(char)
            return True

        self.incorrect_guesses.add(char)
        self.wrong_guess = len(self.incorrect_guesses)

        return False

    def hint(self):
        pos_chars = self.phrase.chars\
            - self.correct_guesses - self.incorrect_guesses
        c_index = randint(0, len(pos_chars))
        char = pos_chars[c_index]
        print(char)
        self.correct_guesses.add(char)

    def _is_max_guess_reached(self):
        return self.wrong_guess >= self.max_guess

    def _is_phrase_guessed_correctly(self):
        return self.phrase.chars == self.correct_guesses

print "=================="
print "= Python Hangman ="
print "=================="

wl = WordList("random")

# START main loop
for phrase in wl.get_phrase():
    game = HangmanGame(phrase)

    # START inner loop
    while not game.is_finished():
        # Show number of guesses used out of allowed guesses
        print "%d/%d" % (game.wrong_guess, game.max_guess)
        
        for char in phrase.get_char(game.correct_guesses):
            print(char),
        print("")

        inchar = raw_input("Enter a character (or quit / hint): ")
        inchar = inchar.strip()
        if not inchar:
            continue

        inchar = inchar.lower()
        if inchar == 'quit' or inchar == 'exit':
            break
        elif inchar == 'hint':
            game.hint()
        else:
            inchar = inchar[0]
            print "You entered: %s" % inchar

            # Check if the character is in the phrase
            if game.guess(inchar):
                print "correct!"
            else:
                print "incorrect!"


        print "Correct guesses: %s" % ', '.join(game.correct_guesses)
        print "Incorrect guesses: %s" % ', '.join(game.incorrect_guesses)
        print "Chars in phrase: %s" % ', '.join(phrase.chars)
        
        # END inner loop

    result = game.get_result()
    if result == 'correct':
        print "You have successfully guessed the phrase %s." % phrase
    elif result == 'max_reached':
        print "Maximum guesses reached. Phrase was %s." % phrase
    else:
        print "Phrase was %s." % phrase
        break
    # END main loop
