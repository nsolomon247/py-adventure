import random
import time


class Intro():
    def displayIntro():
        time.sleep(2)
        print("Loading game...")
        time.sleep(3)
        print("Are you ready?")
        time.sleep(3)
        print("It is the end of a long year of fighting space criminals")
        time.sleep(2)
        print("you come to crossroads on your trip home, one path leads home")
        time.sleep(2)
        print("where you will be handsomly rewarded for a job well done")
        time.sleep(1)
        print("and the other leads through a gamma ray burst that will disentigrate you")
        print()


def choosePath():
    path = ""
    while path != "1" and path != "2":  # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path


def TEST_LOG(choice):
    logfile = open("MY_TEST_LOG_FILE.txt", mode="a")
    logfile.write(choice + "\n")
    logfile.close()


def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home! Now onto your adventure.\n Which path do you choose to take off into(3/4)")
        correctPath = input()

        if correctPath == "3":
            print("You are going at the speed of light")
            time.sleep(2)
            print("You have arrived at planet NX-857 - Nirvanna")
            time.sleep(2)
            print(
                "Do you want to land or keep flying into the space-time continuum?(land/fly)")
            correctPath = input()
            TEST_LOG(correctPath)

            if correctPath == "land":
                print("You have arrived at the Nirvanna that Buddha spoke of...")
                time.sleep(1)
                print("you live the rest of your life in eternal bliss. You Won!")
                time.sleep(2)
            else:
                print("You're flesh disintegrates from the strenousness of the trips.")
                time.sleep(1)
                print("Better luck in the next life!")
                time.sleep(2)
        else:
            print("You have entered an unknown galaxy")
            print("Aliens of different sizes and shapes are around you...")
            print("You die a gruesome death! Sorry, you lose!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    Intro.displayIntro()
    choice = choosePath()
    TEST_LOG(choice)
    checkPath(choice)  # choice is equal to "1" or "2"
    playAgain = input(
        "Do you want to play again? (yes or y to continue playing): ")
    TEST_LOG(playAgain)
