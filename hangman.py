

word = "mynameisibg"


def charposition(string, char):
    pos = []  # list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


counter = 0
guess_word = "-" * len(word)
word_trace = list(guess_word)
flag = False
while True:
    if (counter == 6 or flag):
        if(not flag):
            print("The game is over . :(")
            print("The word was ", word)
        break

    input_letter = input("Guess a letter !")

    if input_letter in word:
        places = charposition(word, input_letter)
        for i in places:
            word_trace[i] = input_letter
            if list(word) == word_trace:
                print("Congratulations You Guessed It Right :)")
                flag = True
                break
        print(*word_trace, sep="")
    else:
        counter += 1
        remain = 6 - counter
        print("The remaining attempts ", remain)
