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