import pyautogui
import time
import os, re
import glob
import numpy as np
import argparse
from string import punctuation

def parse_args():
    parser = argparse.ArgumentParser(description="spam someone with text")
    parser.add_argument('-f', '--file', type=str, required=True, help="the file to spam line by line", dest='file')
    parser.add_argument('--mode', choices=['lines', 'words'], default='lines', help="lines or words")
    args = parser.parse_args()
    return args

def line_by_line(s):
    """print out a text document line by line"""
    with open(s, 'r') as f:
        for line in f:
            pyautogui.write(line.strip())
            pyautogui.press("enter")

def word_by_word(s):
    """print out a text document word by word"""
    with open(s, 'r') as f:
        for line in f:
            for word in line.strip().split(' '):
                pyautogui.write(word.strip())
                pyautogui.press("enter")

if __name__ == "__main__":

    args = parse_args()
    script = args.file

    match = glob.glob(os.path.join(os.path.abspath('./text'), f"{script}*"))
    
    if len(match) == 0:
        raise ValueError(f"No matching files for {script}")
    elif len(match) > 1:
        print("found multiple matching files. Choosing the first one!")

    fqfn = match[0]

    if not os.path.isfile(fqfn):
        raise FileNotFoundError(f"{fqfn} not found")
    print(f"Preparing to send {fqfn}")
    print("Starting in")
    for c in np.arange(5, 0, -1):
        print(c)
        time.sleep(1)
    
    if args.mode == 'lines':
        line_by_line(fqfn)
    elif args.mode == 'words':
        word_by_word(fqfn)
    else:
        pyautogui.write("you need to choose a mode")