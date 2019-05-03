def encrypt(text,shift):
    '''
    INPUT: TEXT as a string and an integer for the SHIFT value.
    OUTPUT: The shifted text after being run through the Caeser cipher.'''

    import numpy
    import string

    encrypted_text = list(range(len(text)))
    
    alphabet = list(string.ascii_lowercase)
        
    shifted_alphabet = list(numpy.roll(alphabet,shift))
    
    
    for i,letter in enumerate(text.lower()):
        
        if letter in alphabet:
            original_index = alphabet.index(letter)
            
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        
        else:
            encrypted_text[i] = letter
            
    return ''.join(encrypted_text)

def decrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''

    import string

    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    
    firsthalf = alphabet[:shift]
    secondhalf = alphabet[shift:]
    shifted_alphabet = secondhalf + firsthalf
    
    for i,letter in enumerate(text.lower()):
        if letter in alphabet:
            encrypted_index = shifted_alphabet.index(letter)
            decrypted_letter = alphabet[encrypted_index]
            
            decrypted_text[i] = decrypted_letter
            
        else:
            decrypted_text[i] = letter
            
    return ''.join(decrypted_text)


def brute_force(message):
    
    '''INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message. 
            One of the printed outputs should be readable.'''
        
    import string
    decrypted_text = list(range(len(message)))
    shift = list(range(0,27))
    
    alphabet = string.ascii_lowercase
    
    for num in shift:
        firsthalf = alphabet[:num]
        secondhalf = alphabet[num:]
        shifted_alphabet = secondhalf + firsthalf
    
        for i,letter in enumerate(message.lower()):
            if letter in alphabet:
                encrypted_index = shifted_alphabet.index(letter)
                decrypted_letter = alphabet[encrypted_index]
            
                decrypted_text[i] = decrypted_letter
            
            else:
                decrypted_text[i] = letter
        
        print('Using shift value of {}'.format(num))
        print(''.join(decrypted_text))
        print('\n')
        
            