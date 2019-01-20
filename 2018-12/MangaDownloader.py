"""
MangaDownloader.py
Crawl manga from an arabic website manga.ae and download it
"""
#TODO Donwload manga from various websites

import urllib
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import re

URL = "https://www.manga.ae/the-promised-neverland/"
FILE_PATH = r"C:\Users\User\Desktop\PySenpai\MangaDownloaded"

class MangaAe:

    def __init__(self):
        self.links = []
        os.chdir(FILE_PATH)

    def grab_pages(self, url, max_chapters):
        chapter = 1  # What chapter you want to start from
        while chapter <= max_chapters:
            _url = url + "/" + str(chapter) + "/0/full"
            source_code = requests.get(_url).text
            soup = BeautifulSoup(source_code, "html.parser")

            for img in soup.select('#showchaptercontainer img'):
                link = img.get('src')
                print(link)
                #self.links.append(link)

#            self.create_manga_chapter_folder(_url, chapter)
            chapter += 1


    def create_manga_chapter_folder(self, url, chapter):
        pattren = re.compile(r"(\w+)://(\w+).(\w+).(\w+)/(.*)/(\d+)/(\d+)/full")
        regex = re.match(pattren, url)
        manga = regex.group(5)

        self.change_path(FILE_PATH, manga, chapter)
        #self.download_chapter(chapter)

    def change_path(self, file_path, manga, chapter):
        file_path = file_path + "\\" + str(manga) + "\\" + str(chapter)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        os.chdir(file_path)

    def download_chapter(self, chapter):
        page = 1
        err = 0
        for link in self.links:
            try:
                img = "00" + str(page) + ".png"
                urllib.request.urlretrieve(link, img)
                page += 1
            except IOError:  # Urllib raise 404 error when the page doesn't exist
                err += 1
                #with open("Errors.txt", "wt") as errors:
                print("Couldn't download page " + str(page) + " from chapter " + str(chapter) + " link: " + str(link) + "\n")
                page += 1
            #errors.close()

        if err == 0:
            print("All pages of chapter " + str(chapter) + " have been downloaded")
        else:
            print("You got " + str(err) + " errors in chapter " + str(chapter) + ", please check file 'errors.txt'")


Ae = MangaAe()
Ae.grab_pages(URL, 2)
