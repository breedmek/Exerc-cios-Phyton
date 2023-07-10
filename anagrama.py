# 5°. Desafio

class PalavrasAnagrama:

    def anagrama(palavra1,palavra2):

        palavraAnagrama = False
        palavra1Ordenada = sorted(palavra1)
        palavra2Ordenada = sorted(palavra2)

        if palavra1Ordenada == palavra2Ordenada:
            palavraAnagrama = True
        return palavraAnagrama

    palavra1 = input('Digite uma palavra: ')
    palavra2 = input('Digite outra palavra: ')
    palavraAnagrama = anagrama(palavra1,palavra2)
    print(palavraAnagrama)