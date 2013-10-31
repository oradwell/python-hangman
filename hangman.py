print "=================="
print "= Python Hangman ="
print "=================="

# START main loop

# Need to get this from wordlist
phrase = "python hangman"

# START inner loop

# Show number of guesses used out of allowed guesses
# Show the characters guessed

# Print the phrase
for char in phrase:
    # Show word separators as is
    if char == " " or char == "-":
        print(char),
    else:
        print("_"),

# New line
print("")

inchar = raw_input("Enter character: ")

print "You entered: %s" % inchar

# Check if the character is in the phrase
# If incorrect - increment wrong guesses
# Check if number of wrong guesses is equal to number of allowed guesses
# Exit showing the full phrase and characters guessed

# END inner loop

# END main loop
