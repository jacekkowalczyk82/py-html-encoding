# This is a sample Python script.

import urllib.parse
import sys

def getHtmlEncoded(text):
    # URL encoding a space character
    encoded_text = urllib.parse.quote(text)
    print(encoded_text) # Outputs: %20 for space
    return encoded_text
 
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('HTML encoded text provided as argument: ')
    # getHtmlEncoded("hasL0!@#") #  prints hasL0%21%40%23
    if len(sys.argv[1]) > 1 :
      getHtmlEncoded(sys.argv[1])
    else:
      print("Please provide a string to encode as a command line argument.")
      getHtmlEncoded("NO_PARAM_PROVIDED")
 
