"""
Dans cet exercice un cherche a savoir si le nombre entier est premier
avec les fonction  isprime(p) et main()
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Cette fonction nous permet de retourner un booléen 
    si l'entier mis en argument "p" est premier(True) ou non (False)
    """
    premier = True
    b= int(sqrt(p))
    if p ==1 :
        premier = False
    elif p==2:
        premier = True
    else:
        for i in range (2,b+1):
            if p % i == 0 :
                premier = False
                break
    return premier
#### Fonction principale


def main():
    """
    main() est la fonction principale qui print les nombre premier
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
