import wordlist

print "=================="
print "= Python Hangman ="
print "=================="

# constants
max_guess = 9

wl = wordlist.WordList("random")

# START main loop
# Should be a random phrase from wordlist instead
for phrase in wl.getPhrase():
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
