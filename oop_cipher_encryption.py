'''This program uses Object Oriented Programming to create an object that uses a modified Ceaser Cipher. The basic idea is the following, given a message such as "hello world", the encryption should perform the following steps:**

Accept a string, such as: "hello world"
Add in a random letter in every other index position in the string, for example: 'hueqlzlpom cwgosrhlbdg'
Then reverse this string, for example: 'gdblhrsogwc moplzlqeuh'
Then create a shuffled version of the alphabet (remember to set a seed to the random.seed() so you can get this shuffled version again by providing the same seed number).
Just like a classic ceaser cipher, match up the index of each letter and then encrypt the letters using this shuffled alphabet.
The end result will be a string something like "divgkjocdze bcrgqghywk" for the previous example.'''

import string
import random

class Encryption():
    
    alphabet = list(string.ascii_lowercase)
    
    def __init__(self,seed):
        
        self.seed = seed
    
    def encrypt_msg(self, message):
        '''
        This method takes in a messsage, and the seed as parameters required for the correct decryption of the message.'''

        #create shuffled alphabet
        random.seed(self.seed)
        shffld_alphabet = random.sample(Encryption.alphabet,26)
        
        message = list(' '.join(message))
        msg = list(range(len(message)))
        
        #Add in a random letter in every other index position in the string,
        #   for example: message = "hello world" returns 'hueqlzlpom cwgosrhlbd' 
        for i,letter in enumerate(message):
            if i%2 == 1:
                msg[i] = random.choice(Encryption.alphabet)
            else:
                msg[i] = letter
        
        # reverse this string, for example: 'dblhrsogwc moplzlqeuh'
        rev_msg = ''.join(msg[::-1])
        
        # ceaser cipher encryption
        output = list(range(len(rev_msg)))
        for i,letter in enumerate(rev_msg):
            if letter.lower() in Encryption.alphabet:
                letter_index = Encryption.alphabet.index(letter.lower())
                output[i] = shffld_alphabet[letter_index]
            else:
                output[i] = letter
                
        return ''.join(output)
    
    def decrypt_msg(self,message,seed):
        '''This method takes in a message and encrypts it.'''

        #delete random alternate letters and reverse message
        message = list(message)
        rev_message = message[0::2][::-1]
        
        #recreate shuffled alphabet
        random.seed(seed)
        shffld_alphabet = random.sample(Encryption.alphabet,26)
        
         # ceaser cipher decryption
        decrypt_txt = list(range(len(rev_message)))
        for i,letter in enumerate(rev_message):
            if letter.lower() in shffld_alphabet:
                encrypt_index = shffld_alphabet.index(letter.lower())
                decrypt_txt[i] = Encryption.alphabet[encrypt_index]
            else:
                decrypt_txt[i] = letter
        
        return ''.join(decrypt_txt)


e = Encryption(5)
msg = e.encrypt_msg('I am a boy')
e.decrypt_msg(msg,9) # to test the security of the decryption method using an incorrect seed.
e.decrypt_msg(msg,5)