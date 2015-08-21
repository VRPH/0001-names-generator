# -*- coding: utf-8 -*-

from os import path
from random import randint
from sys import argv
from sys import exit as close

try:
	script, filename = argv
except Exception:
	script = argv
	filename = raw_input("Please enter name of file to be written.\n")

txt = open(filename, 'w+')

def main():
        for i in ['prefix.txt', 'infix.txt', 'suffix.txt']:
                if filename == i:
                        print "Cannot pass reserved files to script."
                        close(1)
                        
        prompt = "Enter number of names to write to {0}: \n".format(filename)
        try:
                answer = int(raw_input(prompt))
                generate_names(answer)
                raw_input('\nPress any key to continue.')
                close(0)
        except Exception as e:
                print e
                print "Try again. \n"
                main()

# get_lines :: IO() -> [Char] or something like that
def get_lines(path):
        try:
                f = open(path)
        except IOError:
                f = ['']
                pass
        lister = [i.strip() for i in f]
        return lister

# generate_names :: IO() -> [Char]
def generate_names(n):
        prefix = sorted(get_lines("prefix.txt"))
        infix = sorted(get_lines("infix.txt"))
        suffix = sorted(get_lines("suffix.txt"))

        lister = [a + " " + b + " " + c for a in prefix for b in infix for c in suffix]

        counter = 0
        while counter < n:
                line = "あ    " + lister[randint(0, len(lister))] + "\n"
                print line.strip()
                txt.write(line)
                counter += 1

        return ''


main()
