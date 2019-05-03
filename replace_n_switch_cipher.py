def replace_n_switch(name):
    '''This function that takes in a string name (e.g. "Joyner", "Maisie", etc...) and replaces all vowels with the letter x. (Vowels: [a,e,i,o,u]). Then switch the position of the first and last letters.'''
   
    name = list(name)
    vowel = ['a','e','i','o','u']
        
    for i,letter in enumerate(name):
        if letter.lower() in vowel:
            name[i] = 'x'
        else:
            pass
        
    c = name[0]
    name.remove(c)
    
    d = name[-1]
    name.remove(d)
    
    name.append(c)
    name.insert(0,d)

    return ''.join(name)

replace_n_switch('Joyner')