#!/usr/bin/env python3
import os
import sys
import time
import urllib
import datetime
import urlparse
from bs4 import BeautifulSoup

class Utils():
    def __init__(self):
        pass

    @classmethod
    def compatible_input(self, a):
        if (sys.version_info >= (3, 0)):
            return input(a)
        else:
            return raw_input(a)

class Config():
    def __init__(self, output_path, output_name):
        self.setupFile(output_path, output_name)
        print("Checking if output file exists...")
        if (not os.path.isfile(output_path + output_name)):
            print("File doesn't exists. Making it...")
            try:
                if (not os.path.exists(output_path)):
                    os.makedirs(output_path)
                file_ = open(output_path + output_name, 'w')
                file_.write("Log file created by " + self.name() + " on " + time.strftime("%d/%m/%Y @ %I:%M:%S") + ".\n")
                print("File created (\""+output_path+output_name+"\").")
            except OSError:
                print("\nError: Failed to create file (Errno 13: Permission denied)!")
        else:
            print("File exists.")

    @classmethod
    def setupFile(self, a, b):
        self.output_path = a
        self.output_name = b

    @classmethod
    def name(self):
        return "sp00kySpider"

    @classmethod
    def file(self):
        return open(self.output_path + self.output_name ,'a')

class Crawl():
    def __init__(self):
        pass

    @classmethod
    def doCrawl(self, uri):
        self.uri = uri
        self.links = []
        print("Crawl on " + self.uri + " has started!")
        self.start_time = datetime.datetime.now()

        # This is going to get messy.
        # Crawl - Start
        html = urllib.urlopen(self.uri).read()
        soup = BeautifulSoup(html)
        i = 0
        for tag in soup.findAll('a', href=True):
            toAdd = urlparse.urljoin(self.uri, tag['href'])
            if (not toAdd in self.links):
                self.links.append(toAdd)
                i += 1
                print(str(i) + " links found.")
        # Crawl - End

        self.end_time = datetime.datetime.now()
        print("Crawl on " + self.uri + " is over!")

    @classmethod
    def save(self):
        elapsed = self.end_time - self.start_time
        elapsed = divmod(elapsed.total_seconds(), 60)
        file_ = Config.file()
        file_.write("\n\n")
        file_.write("Crawl on \"" + self.uri + "\" started on " + time.strftime("%d/%m/%Y @ %I:%M:%S"))
        file_.write("\nLinks found: %s" %', '.join(str(x) for x in self.links))
        file_.write("\nCrawl completed in %d seconds" %elapsed[1])
        print("Information about this crawl has been saved to \"" + Config.output_path + Config.output_name + "\".")

def main():
    config = Config(output_path="/home/ad/Desktop/", output_name="crawl_log.txt")
    Crawl.doCrawl(Utils.compatible_input("Please enter a URI to be crawled: "))
    Crawl.save()

if __name__ == '__main__':
    main()