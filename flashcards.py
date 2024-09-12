import random

#TODO: empty the dictionary after testing
flashcards = {
    "term1": "definition1",
    "term2": "definition2",
    "term3": "definition3",
    "term4": "definition4",
    "term5": "definition5",
}

# part 1
print("Let's build some unique flashcards")
stop1 = False
while stop1 == False:
    # ask for a term (input)
    u_term = input("Enter a term: ")
    # ask for a definition (input)
    u_def = input("Enter a definiton: ")
    # store those in the dictionary like this flashcards[key]=value (flashcards[term]=def)
    flashcards[u_term] = u_def
    print('Flashcard saved!') # optional
    # loop (part 1) until the user quits
    yes_no = input ('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop1 = True


# part 2
print("It's time for a pop quiz! I'll show you a term and you state the definition.")
stop2 = False
while stop2 == False:
    # randomly select a card (term)
    rand_term = random.choice( list(flashcards.keys() ) )
    # show the term (print)
    print("Here is the term: {}".format(rand_term) )
    # show "ready?" and then wait fo the Enter key
    input("Ready? (Press Enter when ready)" )
    # show the definition (print)
    print("Here is the definition: {}".format( flashcards[rand_term] ) )
    # put that (just part 2) in a loop until the user wants to quit
    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop2 = True