"""
GeniusSenpai.py
A simple code that grabs lyrics from Genius.com and counts words occurrences and saves the result in a text file.

My first code that I'm not ashamed of sharing with the world.
It doesn't really matter whether other people read it or not since it's for future me. UwU
"""

from collections import Counter
from operator import itemgetter
import re
import requests
from bs4 import BeautifulSoup

TESTING = False
LINK = "https://genius.com/Pewdiepie-bitch-lasagna-lyrics"  # Should be obtained from the user

class GeniusSenpai:

    def __init__(self, url):
        self.wordlist = []
        self.lyrics = self.grab_lyrics(url)

    def grab_lyrics(self, url):
        if TESTING:
            with open("lyrics.txt", "rt") as f:
                lyrics = f.read()
            f.close()
            return lyrics

        source_code = requests.get(url).text
        soup = BeautifulSoup(source_code, "html.parser")
        lyrics = soup.find("div", {"class":"lyrics"}).get_text()
        lyrics = re.sub(r"\[(\w+)|(\d+)|(])", '', lyrics)
        lyrics = re.sub(r"\n\n", '', lyrics)
        return lyrics

    def clean_list(self):

        words = self.lyrics.lower()
        words = re.sub(r'\'ll', ' will', words)
        words = re.sub(r'\'re', ' are', words)
        words = re.sub(r"\'it's", 'it is', words)
        words = re.sub(r'[^a-zA-Z\s\'-]', "", words)

        for word in words.split():
             self.wordlist.append(word)

        self.count_using_counter()
        #self.count_using_itemgetter()


    def count_using_counter(self):

        with open("lyrics-wordlist.txt", "wt") as fw:
            for word, count in Counter(self.wordlist).most_common():
                print(word, ":", count)
                fw.write(word + " : " + str(count) + "\r\n")
            fw.close()


    # unused
    def count_using_itemgetter(self):
        wordcounter = {}

        for word in self.wordlist:
            if word not in wordcounter:
                wordcounter[word] = 1
            else:
                wordcounter[word] += 1
        for key, value in sorted(wordcounter.items(), key=itemgetter(1), reverse=True):
            print(key, value)


senpai = GeniusSenpai(LINK)
senpai.clean_list()
