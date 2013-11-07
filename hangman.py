import fileinput
import linecache
import random

class WordList:
    _lines_used = []
    _num_used = 0
    _filename = "wordlist"
    _num_lines = 0
    _mode = ''

    def __init__(self, mode):
        self._mode = mode
        if mode == "sequential":
            return

        self._initRandom()

    def getPhrase(self):
        if self._mode == "sequential":
            for line in fileinput.input(self._filename):
                phrase = self._cleanPhrase(line)
                if not phrase:
                    continue

                yield phrase
        else:
            while self._num_used < self._num_lines:
                line_num = self._getRandomLineNum()
                line = linecache.getline(self._filename, line_num)

                phrase = self._cleanPhrase(line)
                if not phrase:
                    continue

                yield phrase

    def _initRandom(self):
        self._countLines()

    def _getRandomLineNum(self):
        while True:
            line_num = random.randint(1, self._num_lines)
            if line_num not in self._lines_used:
                self._num_used += 1
                self._lines_used.append(line_num)
                return line_num


    def _cleanPhrase(self, line):
        phrase = line.strip()
        if len(phrase) < 1 or phrase[0] == '#':
            return False
        
        return phrase

    def _countLines(self):
        for line in fileinput.input(self._filename):
            self._num_lines += 1


print "=================="
print "= Python Hangman ="
print "=================="

# constants
max_guess = 9

wordlist = WordList("random")

# START main loop
# Should be a random phrase from wordlist instead
for phrase in wordlist.getPhrase():
    print phrase
    continue
    wrong_guess = 0
    incorrect_guesses = set()
    correct_guesses = set()
    chars_in_phrase = set()

    # get unique characters into a set
    for char in phrase:
        if char != " " and char != "-":
            chars_in_phrase.add(char.lower())


    # START inner loop
    # While wrong guesses hasn't reached max guesses 
    # and not all the characters are guessed
    while wrong_guess < max_guess and chars_in_phrase != correct_guesses:
        # Show number of guesses used out of allowed guesses
        print "%d/%d" % (wrong_guess, max_guess)
        # Print the phrase
        for char in phrase:
            # Show word separators and guessed chars as is
            if char == " " or char == "-" or char.lower() in correct_guesses:
                print(char),
            else:
                print("_"),

        # New line
        print("")

        inchar = raw_input("Enter character: ")

        if len(inchar) < 1:
            continue

        inchar = inchar[0].lower()
        print "You entered: %s" % inchar

        # Check if the character is in the phrase
        if inchar in chars_in_phrase:
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
        print "Chars in phrase: %s" % chars_in_phrase
        
        # END inner loop

    print "Phrase: %s" % phrase

    # END main loop
