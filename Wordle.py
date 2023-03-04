## importing necessary package

import pandas as pd
import random
from colorama import Fore, Style, Back


def gaming(str1="", str2="", count=0):
    res = ""
    for i in range(len(str1)):
        if str2[i] == str1[i]:
            res += Fore.GREEN + Style.BRIGHT + str2[i] + Style.RESET_ALL + "  "
            correct.append(str2[i])
        elif str2[i] in str1 and str2[i] != str1[i]:
            if str1.count(str2[i])==1 and str2[i] in correct and str2.count(str2[i]) != 1:
                res += Style.DIM + str2[i] + Style.RESET_ALL + "  "

            else:
                res += Fore.YELLOW + Style.BRIGHT + str2[i] + Style.RESET_ALL + "  "

        else:
            res += Style.DIM + str2[i] + Style.RESET_ALL + "  "

    result.append(res)
    for i in range(len(result)):
        print(result[i])

    if str1 == str2:
        return True, count
    else:
        return False, count


## Downloaded a dataset from Kagle.com to get list of meaningful 5 letter words
## Using pandas saving the dataset into our variable


dfs = pd.read_html("https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt")
df_words = dfs[0]
df_words.to_csv("df_words.csv", index = False)
df_words = pd.read_csv("df_words.csv", index_col = 0)
words = df_words["1"].to_list()  # -- storing list of 5 letter words as list in python for further calculatiions.
play = True
while play:
    print("\n")
    print("\t\t\t\t\t\tWORDLE\n")
    print("Wordle is a single player game where player should guess the 5 letter words within 5 chances")
    x = str.upper(random.choice(words))
    correct = []
    #print(x)
    count = 0
    game_done = False
    result = []
    while not game_done:
        win = False
        if count == 5:
            print("Word is: ", x)
            print("Better luck next time")
            again = input("Do you want to play another game (y/n)?:")
            if again.lower() == 'y':
                game_done = True
                print("restarting...")
            else:
                print("thanks for playing..")
                play = False
                break

        else:
            word = str.upper(input("Enter your word: "))
            print(word)
            if len(word) != 5:
                print("Please enter a 5 letter word")
            else:

                win, num = gaming(x, word, count)
                count += 1

            if win == True:
                game_done = True
                if num == 0:
                    print("Amazing..!!")
                elif num == 1:
                    print("Woww..!!")
                elif num == 2:
                    print("Superb..!")
                elif num == 3:
                    print("Good..!")
                else:
                    print("Finallyy...")

                again = input("Do you want to play another game (y/n)?:")
                if again.lower() == 'y':
                    print("restarting...\n")
                else:
                    print("thanks for playing..\n")
                    play = False

