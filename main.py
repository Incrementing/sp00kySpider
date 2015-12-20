#!/usr/bin/env python3
import os
import time

class Config():
    @classmethod
    def name(self):
        return "sp00kySpider"

    def __init__(self, output_path, output_name):
        print("Checking if output file exists...")
        if (not os.path.isfile(output_path + output_name)):
            print("File doesn't exists. Making it...")
            try:
            	if (not os.path.exists(output_path)):
            		os.makedirs(output_path)
                file_ = open(output_path + output_name, 'w')
                file_.write("Log file created by " + self.name() + " on " + time.strftime("%d/%m/%Y @ %I:%M:%S") + ".")
                print("File created (\""+output_path+output_name+"\").")
            except OSError:
                print("\nError: Failed to create file (Errno 13: Permission denied)!")
        else:
            print("File exists.")

def main():
    config = Config(output_path="/home/ad/Desktop/", output_name="crawl_log.txt")

if __name__ == '__main__':
    main()