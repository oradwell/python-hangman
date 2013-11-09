from fileinput import input
from linecache import getline
from random import randint

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

        self._init_random()

    def get_phrase(self):
        if self._mode == "sequential":
            for line in input(self._filename):
                phrase = self._clean_phrase(line)
                if not phrase:
                    continue

                yield phrase
        else:
            while self._num_used < self._num_lines:
                line_num = self._get_random_line_num()
                line = getline(self._filename, line_num)

                phrase = self._clean_phrase(line)
                if not phrase:
                    continue

                yield phrase

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
