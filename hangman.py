print "=================="
print "= Python Hangman ="
print "=================="

# START main loop

# Need to get this from wordlist
phrase = "python hangman"

# START inner loop
# get unique characters into a set
incorrect_guesses = set()
correct_guesses = set()
chars_in_phrase = set()
for char in phrase:
    if char != " " and char != "-":
        chars_in_phrase.add(char)

max_guess = 9
cur_guess = 0
wrong_guess = 0



# While wrong guesses hasn't reached max guesses
while wrong_guess < max_guess and chars_in_phrase != correct_guesses:
    # Show number of guesses used out of allowed guesses
    print str(wrong_guess) + "/" + str(max_guess)
    # Print the phrase
    for char in phrase:
        # Show word separators as is
        if char == " " or char == "-" or char in correct_guesses:
            print(char),
        else:
            print("_"),

    # New line
    print("")

    inchar = raw_input("Enter character: ")

    if len(inchar) > 1:
        inchar = inchar[0]
    print "You entered: %s" % inchar

    # Check if the character is in the phrase
    if inchar in chars_in_phrase:
        print "correct!"
        correct_guesses.add(inchar)
    else:
        # If incorrect - increment wrong guesses
        print "incorrect!"
        wrong_guess += 1
        incorrect_guesses.add(inchar)

    print "Correct guesses: %s" % correct_guesses
    print "Incorrect guesses: %s" % incorrect_guesses
    print "Chars in phrase: %s" % chars_in_phrase
    
    # END inner loop

print "Phrase: %s" % phrase

# END main loop
