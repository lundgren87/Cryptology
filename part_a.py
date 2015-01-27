# coding: utf-8
'''
Created on 27 jan 2015

@author: Sven
'''

import sys

'''
Vigenere takes a text file and a key as input.
It converts all characters in the text file to lower case
and then encrypts it using the vigenere cipher with key key and saves it in file code.
'''
def vigenere(args):
    
    # Get argument files
    textfile = args[0]
    resultfile = args[1]
    keyfile = args[2]
    
    # Files to read and write from
    fr = open(textfile, 'r')
    fw = open(resultfile, 'w')
    fk = open(keyfile, 'r')
    
    # Read key
    key = fk.read()
    
    # Read text file and convert to lower case
    to_encrypt = fr.read()
    to_encrypt.lower()
    
    # The encrypted text
    encrypted = ''
    
    # The alphabet and a key index
    alphabet = 'abcdefghijklmnopqrstuvwxyzåäö '
    key_index = 0
    
    # Encrypt character by character
    for c in to_encrypt:
        # Get index of current character in alphabet
        index = alphabet.find(c)
        
        # If not part of alphabet, add as is to encrypted
        if index == -1:
            encrypted += c
            print("Not a charcter: ", c, index)
        # Else, encrypt and add to encrypted
        else:
            print("A character: ", c, index)
            # Calculate new index
            index += alphabet.find(key[key_index])
            print(index)
            index %= len(alphabet)
            encrypted += alphabet[index]
            
            # Increment and possibly reset key_index
            key_index += 1
            if key_index == len(key):
                key_index = 0
    
    # We're done, so write to output file
    fw.write(str(encrypted))
    print("Encryption done, result found in file", resultfile)
    

if __name__ == '__main__':
    vigenere(sys.argv[1:])