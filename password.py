# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 Création d'une liste qui contiendra les lettres d'un mot de passe.
    found = False
    i=len(pwd)-1
    if i<0:
        raise ValueError("Mot de passe d'entrée trop court")
    if password == len(pwd)*'z':
        raise ValueError("Mot de passe d'entrée trop 'haut'")

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 Si la lettre courante n'est pas un 'z', on 'incremente' à la 
		                                # lettre suivante, sinon on passe à la lettre précedente du mot de passe.  
           found = True             
        else:
            pwd[i] = 'a'
            i = i-1
            
    
    return ''.join(pwd) #3 On renvoi une chaine de caracteres composée des lettes de la liste pwd(aucun séparateur).



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import unittest
    unittest.main()
