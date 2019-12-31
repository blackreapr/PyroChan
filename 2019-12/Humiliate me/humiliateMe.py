import random
from playsound import playsound

"""
my easy approach: The insults in the audio file must be in the same order as in the text file
You can simply suggest timing for this script to run using windows task scheduler 
"""


# Using insults recorded by friend
def play_mp3(index):
    segment = str(index) + ".mp3"
    playsound("audio/" + segment)


def main():
    insults = []
    with open("Samples.txt", "rt") as roasts:
        for roast in roasts:
            insults.append(roast)

    index = random.randrange(len(insults))
    play_mp3(index)


if __name__ == "__main__":
    main()