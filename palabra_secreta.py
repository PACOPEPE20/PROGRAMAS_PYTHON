
secret_word = "vegetta777"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guesses_count < guess_limit:
            guess = input("Palabra secreta: ")
            guess_count += 1
    else:
        out_of_guesses =True


if out_of_guesses:
    print("Te has quedado sin oportunidades")
else:
    print("Muy bien, la has acertado")
