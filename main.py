#!/usr/bin/env python3
import os

class Config():

	def __init__(self, output_path, output_name):
		print(output_path)
		print(output_name)

def main():
    config = Config(output_path="/home/ad/Desktop/", output_name="crawl_log.txt")

if __name__ == '__main__':
    main()