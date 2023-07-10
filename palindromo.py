# 3° Desafio

class palavraPalindromo:

    def palindromo(palavra):

        pl = []
        for p in palavra:
            pl.append(p)
        if pl[0:5:1] == pl[-1:-6:-1]:
            #pl == palavra
            print(palavra + ' é palindomo!')
            
        else:
            #pl != palavra
            print(palavra +' não é palindomo!')
            
        return pl

    palavra = input('Digite uma palavra: ')
    pl = palavra
    palavraPalindomo = palindromo(pl)